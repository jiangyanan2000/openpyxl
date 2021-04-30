from PIL import Image
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
width = 80
height = 80
def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return " "

    length = len(ascii_char)
    gray = int(0.2126 * r+0.7152 * g+0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

im = Image.open("111.jpg")
im = im.resize((width,height),Image.NEAREST)
txt = ""

#遍历图片中的每一行
for i in range(width):
    for j in range(height):
        txt += get_char(*im.getpixel((i,j)))
        print(txt)
