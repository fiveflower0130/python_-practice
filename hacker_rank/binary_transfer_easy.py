# binary transfer
n = int(input())
bin_list = str(bin(n))[2:].split('0')
print(bin_list)
print(max(bin_list))
print(len(max(bin_list)))