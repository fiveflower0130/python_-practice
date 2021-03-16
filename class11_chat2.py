import os


def convert(lines):
    allen_msg_count = 0
    allen_pic_count = 0
    allen_sticker_count = 0
    viki_msg_count = 0
    viki_pic_count = 0
    viki_sticker_count = 0

    new_lines = [line.split(' ') for line in lines]
    for line in new_lines:
        time = line[0]
        name = line[1]
        if name == 'Allen':
            msg = line[2]
            if msg == '圖片':
                allen_pic_count += 1
            elif msg == '貼圖':
                allen_sticker_count += 1
            else:
                for m in line[2:]:
                    allen_msg_count += len(m)
        elif name == 'Viki':
            msg = line[2]
            if msg == '圖片':
                viki_pic_count += 1
            elif msg == '貼圖':
                viki_sticker_count += 1
            else:
                for m in line[2:]:
                    viki_msg_count += len(m)
    print(
        f"Allen totally say {allen_msg_count} words, paste {allen_pic_count} pictures, paste {allen_sticker_count} stickers")
    print(
        f"Viki totally say {viki_msg_count} words, paste {viki_pic_count} pictures, paste {viki_sticker_count} stickers")


def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = [line.strip() for line in f]
        # strip()->去除頭尾的空格或是換行或是()裡面設定的東西 split->分割
    return lines


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


def main():
    name = "LINE-Viki.txt"
    lines = read_file(name)
    news_lines = convert(lines)
    # write_file("output.txt", news_lines)


main()
