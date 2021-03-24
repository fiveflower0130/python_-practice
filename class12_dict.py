import os
import time
import progressbar

def read_file(path, bar):
    data = []
    count = 0
    with open(path, "r", encoding="utf-8-sig") as f:
        for line in f:
            data.append(line)
            count += 1 
            bar.update(count)
            # if len(data) % 10000 == 0:
            #     print(len(data))
            
    return data

def count_file_word(data):
    wc = {}
    for line in data:
        words = line.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    for word in wc:
        if wc[word] > 1000000:
            print(word,": ", wc[word])
    return wc

def main():
    path = "read/reviews.txt"
    bar = progressbar.ProgressBar(max_value=1000000)
    start_time = time.time()
    file_data = read_file(path, bar)
    file_dict = count_file_word(file_data)
    # for word in file_dict:
    #     if file_dict[word] > 500000:
    #         print(word,": ", file_dict[word])
        
    end_time = time.time()
    print("Total time is", round(end_time - start_time))

main()
