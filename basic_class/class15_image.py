import os
from PIL import Image

# image_file = Image.open("read/convert_image.jpg")
# print(type(image_file))
# image_file = image_file.convert('L') #1也可以但是畫質不好所以用Ｌ
# image_file.save("read/result.png")

def trans_image_to_bw(file_path, output_path, file):
    image_file = Image.open(os.path.join(file_path, file)) # 可以用os.path.join將路徑合併
    image_file = image_file.convert('L') #1也可以但是畫質不好所以用Ｌ
    new_file = file[:-4]+'_bw.png' # file[:-4]是指只取.jpg之前的字串(名字)
    image_file.save(os.path.join(output_path, new_file))  

file_path = "./read"
output_path = "./output"
for file in os.listdir(file_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)
        trans_image_to_bw(file_path, output_path, file)