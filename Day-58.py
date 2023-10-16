##65.Multithreading With "threading" Module.
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
