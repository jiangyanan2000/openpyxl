from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
count = len(ascii_char)

image_file = Image.open("222.png")
# print(image_file.size)
w, h = image_file.size
print(w, h)


def transform(image_file=image_file):
    codePic = " "
    imode = list(image_file.getbands())
    print(imode)
    print(imode[-1])
    for i in range(0, h):
        for j in range(0, w):
            if imode[-1] == "A":
                r, g, b, a = image_file.getpixel((j, i))
            elif imode[-1] == "B":
                r, g, b = image_file.getpixel((j, i))
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            # print(int(((count-1)*gray)/256))
            unit = (256.0 + 1) / count
            codePic += ascii_char[int(gray/unit)]
        codePic += "\t\n"
    print(codePic)

    return codePic


transform()
image_file = image_file.resize((int(image_file.size[0]*0.1),int(image_file.size[1]*0.1)))
tmp = open("mp.txt","w")
tmp.write(transform())
tmp.close()
# print("info:",image_file.size[0]," ",image_file.size[1]," ",count)
