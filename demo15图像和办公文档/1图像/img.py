"""


Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作。
可以使用下面的命令来安装Pillow。

pip install pillow
"""
# 导入Pillow库
from PIL import Image

# 打开一张图像，这里假设图像的文件名是image.jpg
img = Image.open("111.png")

# 将图像转换为灰度图像
img_gray = img.convert("L")

# 保存灰度图像为新的文件，这里假设新文件的文件名是image_gray.jpg
img_gray.save("new111.png")
