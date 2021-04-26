import os


def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = [line.strip() for line in f]
        # strip()->去除頭尾的空格或是換行或是()裡面設定的東西 split->分割
    return lines


def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == "Allen":
            person = line
            continue
        elif line == "Tom":
            person = line
            continue

        if person:
            new.append(person + ": " + line)
    return new


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


def main():
    name = "input.txt"
    lines = read_file(name)
    news_lines = convert(lines)
    write_file("output.txt", news_lines)


main()
