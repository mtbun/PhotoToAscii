import os
from PIL import Image

def toascii(path,img): 
    currently_direc = os.getcwd()
    os.chdir(path)
    html_name = str(img[:-3]) + '.html'
    img = Image.open(img)
    width, height = img.size
    os.chdir(currently_direc)
    doc = open(html_name, 'w')
    doc.write('<pre style="font: 8px/4px monospace;">')

    for i in range(0, height, 5):
        for j in range(0, width, 5):
            a, b, c= img.getpixel((j, i));#a, b, c, d for png image files
            if (a, b, c) <= (100, 100, 100):#change the parameters according to darkness of the image
                doc.write('#')
            elif (a, b, c) <= (170, 170, 170):#change the parameters according to darkness of the image
                doc.write('+')
            elif (a, b, c) <= (180, 180, 180):#change the parameters according to darkness of the image
                doc.write("'")
            elif (a, b, c) <= (200, 200, 200):#change the parameters according to darkness of the image
                doc.write('.')
            else:
                doc.write(',')
        doc.write('\n')
    doc.write('</pre>')
    doc.close()


def toascii2(path,img): 
    currently_direc = os.getcwd()
    os.chdir(path)
    img = Image.open(img)
    width, height = img.size
    os.chdir(currently_direc)
    doc = open('deneme.txt', 'w')

    for i in range(0, height, 5):
        for j in range(0, width, 5):
            a, b, c= img.getpixel((j, i));#a, b, c, d for png image files
            if (a, b, c) <= (100, 100, 100):#change the parameters according to darkness of the image
                doc.write('#')
            elif (a, b, c) <= (170, 170, 170):#change the parameters according to darkness of the image
                doc.write('+')
            elif (a, b, c) <= (180, 180, 180):#change the parameters according to darkness of the image
                doc.write("'")
            elif (a, b, c) <= (200, 200, 200):#change the parameters according to darkness of the image
                doc.write('.')
            else:
                doc.write(',')
        doc.write('\n')
    doc.close()


if __name__ == "__main__":
    path = '../../../Downloads/'
    img = 'my-passport-photo.jpg'
    toascii(path,img)
