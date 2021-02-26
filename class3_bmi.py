weight = input('Please input your weight(kg): ')
height = input('Please input your height(cm): ')
if weight == '':
    print("Weight can't be null!!")
    raise SystemExit
if height == '':
    print("Height can't be null!!")
    raise SystemExit
height = float(height / 100)
BMI = float(weight) / (height * height)
if BMI != 0 and BMI != None:
    print(f'Yor BMI is {BMI}')
    if BMI < 18.5:
        print('You are light weight!')
    elif BMI >= 18.5 and BMI < 24:
        print('You are normal weight!')
    elif BMI >= 24 and BMI < 27:
        print('You are overweight!')
    elif BMI >= 27 and BMI < 30:
        print('You are mild obesity!')
    elif BMI >= 30 and BMI < 35:
        print('You are moderate obesity!')
    else:
        print('You are severe obesity!')
else:
    print('Incorrect number! Please try again.')
