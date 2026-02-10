"""Two shoppers adding items to a shared notepad"""

import threading

garlic_count = 0


def shopper():
    global garlic_count
    for i in range(10_000_000):
        garlic_count += 1


if __name__ == "__main__":
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print(f"We should buy {garlic_count} garlic.")
