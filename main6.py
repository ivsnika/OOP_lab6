import re
from OOP_lab6.laba5_s import Sentence


def main():
    filename = "text6.txt"

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        raw_words = re.findall(r'\w+', text, re.UNICODE)
        sentence = Sentence(raw_words)

        print("Слова за алфавітом:")
        for word in sentence:
            print(f" {word}")

    except FileNotFoundError:
        print(f"Помилка {filename}")


if __name__ == "__main__":
    main()