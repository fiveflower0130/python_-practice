import os

products = []
# check and read data from csv file to  products list
if os.path.isfile("products.csv"):
    print("File exist!!")
    with open ("products.csv", "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價錢" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    print(products)
else:
    print("File doesn't exist")

# add data to products list
while True:
    name = input("please input product name: ")
    if name == "q":
        break
    price = input("please input product's proce: ")
    products.append([name, price])
print(products)

# print all record
for p in products:
    print(f"{p[0]}'s price is {p[1]}")

# write record to csv file
with open("products.csv", "w", encoding="utf-8") as f:
    f.write("商品,價錢\n")
    for p in products:
        f.write(f"{p[0]},{p[1]}\n")
