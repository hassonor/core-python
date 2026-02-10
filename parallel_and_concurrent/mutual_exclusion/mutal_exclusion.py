"""
Critical Section
----------------
* Code segment that accesses a shared resource
* Should not be executed by more than one thread or process at a time

Mutex (Lock)
------------
* Mechanism to implement mutual exclusion
* Only one thread or process can possess at a time
* Limits access to critical section

Atomic Operations
-----------------
* Execute as a single action, relative to other threads
* Cannot be interrupted by other concurrent threads

Acquiring a Lock
-----------------
* If lock is already taken, block/wait for it to be available
"""

import threading
import time

"""Two shoppers adding items to a shared notepad"""

garlic_count = 0
pencil = threading.Lock()


def shopper():
    global garlic_count
    for i in range(5):
        print(threading.current_thread().name, 'is thinking.')
        time.sleep(0.5)
        pencil.acquire()
        garlic_count += 1
        pencil.release()


if __name__ == "__main__":
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print(f"We should buy {garlic_count} garlic.")
