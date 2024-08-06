import os
import random


def generate_random_number():
    return random.randint(1, 10)


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    number = generate_random_number()
    print(f"Generated number: {number}")

    file_path = "test.txt"
    write_to_file(file_path, f"The number is: {number}")
    content = read_file(file_path)

    if content:
        print(f"File content: {content}")
    else:
        print("No content found.")


if __name__ == "__main__":
    main()
