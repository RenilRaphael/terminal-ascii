from PIL import Image, ImageOps
import numpy as np

def avgofpixels(rgbtuple):
    t=0.21*rgbtuple[0] + 0.72*rgbtuple[1] + 0.07*rgbtuple[2]
    return round(t/3)
while True:
    try:
        file=input("Enter name of file (do include the extension:.jpg, .png etc):")
        img=Image.open(file)
        break;
    except OSError:
        print("Could not retrieve file, file doesnt exist in the current folder or file name is wrong. Try again.")
    
if img.size[0] > 500 and img.size[1] > 500:
    img=ImageOps.contain(img,(800,800))
print(f'Image size:{img.size[0]} x {img.size[1]}')

img_x = img.size[0]
img_y = img.size[1]
char_dict = {
    0:'`', 1: '.',2: '^',3: '\\',4: '"',5: ',',6: ':',7: ';',8: 'I',9: 'l',10: '!',11: 'i',12: '~',13: '+',14: '_',15: '-',16: '?',17: ']', 18: '[',19: '}',
    20: '{',21: '1',22: ')',23: '(',24: '|',25: '/',26: 't',27: 'f',28: 'j',29: 'r',30: 'x',31: 'n',32: 'u',33: 'v',34: 'c',35: 'z',36: 'X',37: 'Y',38: 'U',
    39: 'J',40: 'C',41: 'L',42: 'Q',43: '0',44: 'O',45: 'Z',46: 'm',47: 'w',48: 'q',49: 'p',50: 'd',51: 'b',52: 'k',53: 'h',54: 'a',55: 'o',56: '*',57: '#',58: 'M',
    59: 'W',60: '&',61: '8',62: '%',63: 'B',64: '@',65: '$',66: '`'
}

imgmatrix=np.asarray(img)

avgofpxls=[[avgofpixels(imgmatrix[y][x]) for x in range(img_x)] for y in range(img_y)]

for y in range(img_y):
    for x in range(img_x):
        print(char_dict[round(avgofpxls[y][x]/3.86)],end='')
    print()
print("USE 'Ctrl' + '+' or '-' to zoom in or out in terminal to see the image")