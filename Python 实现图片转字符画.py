from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
print(len(ascii_char))
im = Image.open("111.jpg")
w, h = im.size
height = int(h * 0.3)
width = int(w * 0.3)
# rgb = im.getpixel((44,33))
print(w, h)
# print(rgb)
im = im.resize((width, height), Image.NEAREST)
txt = ""


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "

    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


# 遍历图片中的每一行
for i in range(height):
    for j in range(width):
        txt += get_char(*im.getpixel((j, i)))
    txt += "\t\n"
print(txt)
