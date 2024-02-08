"""Two shoppers adding items to a shared notepad"""

import threading
import time

items_on_notepad = 0
pencil = threading.Lock()


def shopper():
    global items_on_notepad
    name = threading.current_thread().name
    items_to_add = 0
    while items_on_notepad <= 20:
        if items_to_add and pencil.acquire(blocking=False):  # add item(s) to shared items_to_add
            items_on_notepad += items_to_add
            print(f"{name} added {items_to_add} items(s) to notepad.")
            items_to_add = 0
            time.sleep(0.3)  # time spent writing
            pencil.release()
        else:  # look fo other things to buy
            time.sleep(0.1)  # time spent searching
            items_to_add += 1
            print(f"{name} found something else to buy.")


if __name__ == '__main__':
    barron = threading.Thread(target=shopper, name="Barron")
    olivia = threading.Thread(target=shopper, name="Olivia")
    start_time = time.perf_counter()
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    elapsed_time = time.perf_counter() - start_time
    print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))
