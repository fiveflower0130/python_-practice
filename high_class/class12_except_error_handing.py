"""
error -> 所有的錯都是 error

exception -> 發生在runtime時候的error
runtime就是程式在執行的時候

try -> 正常執行可能會出錯的程式
except -> 當有錯誤發生時
else -> 如果沒有錯誤的話
finally -> 不管有沒有錯最後都會執行到這
"""
# try:
#     with open('f.txt', 'r') as f:
#         for line in f:
#             x = int(line.strip())
# except FileNotFoundError as err:
#     print(err)
# except ValueError:
#     print('ValueError!!')
# else:
#     print('no exception caught!')
# finally:
#     print('in finally!')


# s = input('enter a number:')

# try:
#     n = int(s)
# except ValueError:
#     print('ValueError!!! Please enter a number')
# except NameError:
#     print('NameError!!!')

# print('ajdsfjdfdjsfjdsiji')

"""
except error的寫法有兩種
1. except(ValueError, NameError) 用()內填入可能錯誤
2. 多個except EX: except ValueError: except NameError:
"""
i = 0
error_count = 0
while True:
    try:
        s = input('Please enter a number:')
        n = int(s)
        print(f'good, yoou entered {n}')
    except ValueError:
        error_count += 1
        if error_count >= 3:
            print("已經3次了，不讓你玩！")
        print('你怎麼沒輸入數字？')
    except KeyboardInterrupt:
        print('Game over')
        break
    finally:
        i = i+1
        print(f"這是第{i}次")