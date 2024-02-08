"""Three philosophers, thinking and eating sushi"""

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    sushi_eaten = 0
    while sushi_count > 0:  # eat sushi until it's all gone
        with first_chopstick:
            with second_chopstick:
                if sushi_count > 0:
                    sushi_count -= 1
                    sushi_eaten += 1
                    print(f"{name} took a piece! Sushi remaining: {sushi_count}")
    print(f"{name} took {sushi_eaten} pieces")


if __name__ == "__main__":
    for thread in range(50):
        threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Olivia', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_b)).start()
