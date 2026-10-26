from itertools import count
from queue import Queue

queue = Queue()
request_ids = count(1)

def generate_request():
    request = f"Заявка №{next(request_ids)}"
    queue.put(request)
    print(f"Створено: {request}")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється: {request}")
        queue.task_done()
    else:
        print("Черга порожня.")

def main():
    while True:
        command = input(
            "\nНатисніть Enter, щоб створити й обробити заявку, "
            "або введіть 'q' для виходу: "
        ).strip().lower()

        if command == "q":
            print("Програму завершено.")
            break

        if command != "":
            print("Невідома команда. Натисніть Enter або введіть 'q'.")
            continue

        generate_request()
        process_request()

if __name__ == "__main__":
    main()
