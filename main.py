import os


def count_lines(file: str):
    with open(file, 'r') as f:
        return sum(1 for line in f if line.strip())


def format_with_apostrophe(number: int) -> str:
    return "{:,}".format(number).replace(",", "'")


def main():
    total_lines = 0
    dir = os.path.join(os.getcwd(), "data")

    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        lines = count_lines(file_path)
        print(f"{file}: {format_with_apostrophe(lines)} lines")
        total_lines += lines

    print(f"Total lines in {dir}: {format_with_apostrophe(total_lines)}")


if __name__ == "__main__":
    main()
