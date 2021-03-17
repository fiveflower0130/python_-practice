import time
import random


def run_floor(current_floor):
    start_time = time.time()
    while True:
        target_floor = random.randint(1, 10)
        print("要到", target_floor)
        if target_floor == current_floor:
            current_floor = target_floor
            continue
        elif target_floor < current_floor:
            print('電梯下樓')
            while target_floor < current_floor:
                print(current_floor)
                current_floor = current_floor - 1
                time.sleep(1)
            print(current_floor, "樓到了")
            time.sleep(1)
        else:
            print('電梯上樓')
            while target_floor > current_floor:
                print(current_floor)
                current_floor = current_floor + 1
                time.sleep(1)
            print(current_floor, "樓到了")
            time.sleep(1)
        print('共花費: ', round(time.time() - start_time), '秒')
        break


def main():
    current_floor = 1
    run_floor(current_floor)


main()
