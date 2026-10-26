from collections import deque


def is_palindrome(text):
    normalized_text = "".join(text.lower().split())

    characters = deque(normalized_text)

    while len(characters) > 1:
        first = characters.popleft()
        last = characters.pop()

        if first != last:
            return False

    return True


def main():
    text = input("Введіть рядок для перевірки: ")

    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()