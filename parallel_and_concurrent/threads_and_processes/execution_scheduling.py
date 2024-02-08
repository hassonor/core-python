"""Two threads chopping vegetables"""

import threading
import time

chopping = True


def vegetable_chopper():
    name = threading.current_thread().getName()
    vegetable_count = 0
    while chopping:
        print(f"{name} chopped a vegetable!")
        vegetable_count += 1
    print(f"{name} chopped {vegetable_count} vegetables.")


if __name__ == "__main__":
    threading.Thread(target=vegetable_chopper, name="Barron").start()
    threading.Thread(target=vegetable_chopper, name="Olivia").start()

    time.sleep(2)  # chop vegetables for 1 second
    chopping = False  # stop both threads from chopping
