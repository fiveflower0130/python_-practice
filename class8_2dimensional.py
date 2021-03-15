import os
# check and read data from csv file to  products list


def read_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價錢" in line:
                continue
            # strip()->去除頭尾的空格或是換行或是()裡面設定的東西 split->分割
            name, price = line.strip().split(",")
            products.append([name, price])
    return products

# add data to products list


def add_data(products):
    while True:
        name = input("please input product name: ")
        if name == "q":
            break
        price = input("please input product's proce: ")
        products.append([name, price])
    print(products)
    return products

# print all record


def print_products(products):
    for p in products:
        print(f"{p[0]}'s price is {p[1]}")

# write record to csv file


def write_file(file_name, products):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("商品,價錢\n")
        for p in products:
            f.write(f"{p[0]},{p[1]}\n")


def main():
    data_file = "products.csv"
    if os.path.isfile(data_file):
        print("File exist!!")
        products = read_file(data_file)
    else:
        print("File doesn't exist")

    products = add_data(products)
    print_products(products)
    write_file(data_file, products)


main()
