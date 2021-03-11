# data = []
# with open('read/foods.txt', 'r') as foods:
#     for food in foods:
#         # strip() use to remove \n or space
#         data.append(food.strip())
# print(data)

data = []
path = "read/reviews.txt"
with open(path, "r") as f:
    for line in f:
        data.append(line)
        if len(data) % 1000 == 0:
            print(len(data))
print(f"All file has been done, total have {len(data)} datas")

sum_len = 0
for d in data:
    sum_len += len(d)

ave = sum_len/len(data)
print(f"message's average length is {ave}")

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print(f'There are {len(new)} messages length < 100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)

print(f"There are {len(good)} messages which has include the word 'good' ")

# 進階寫法

good = [d for d in data if 'good' in d]
print(good[0])
