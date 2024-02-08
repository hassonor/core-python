"""
* New threads will inherit daemon status from their parent
* Set the daemon property to change status before starting thread
* When the program ends, remaining daemon threads are abandoned
"""

import threading
import time

"""Barron finishes cooking while Olivia cleans"""


def kitchen_cleaner():
    while True:
        print("Olivia cleaned the kitechen.")
        time.sleep(1)


if __name__ == "__main__":
    olivia = threading.Thread(target=kitchen_cleaner)
    olivia.daemon = True
    olivia.start()

    print("Barron is cooking...")
    time.sleep(0.6)
    print("Barron is cooking...")
    time.sleep(0.6)
    print("Barron is cooking...")
    time.sleep(0.6)
    print("Barron is done!")
