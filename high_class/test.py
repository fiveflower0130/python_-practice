def find_max(a_list):
    if not a_list:
        return 0
    else:
        print(len(a_list), " ",a_list)
        num_max = a_list[0]
        for num in a_list:
            print(num , num_max)
            if num > num_max:
                num_max = num
        return num_max

def main():
    while True:
        input_list = input('please enter three number: ')

        if input_list == 'q':
            print("Exit process!!")
            break
        else:
            number_list = [int(number) for number in input_list.split()]
            num_max = find_max(number_list)
            print(num_max)

main()

# products = []

# while True:
#     name = input("please input name: ")
#     price = input("please input price: ")
#     end = input("continue? Y or N: ")
#     products.append([name, price])

#     if end == "N":
#         break
#     else:
#         continue
# print(f"produsts result: {products} ")


