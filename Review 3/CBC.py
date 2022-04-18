import os, binascii
from backports.pbkdf2 import pbkdf2_hmac
import matplotlib.pyplot as plt
from PIL import Image
import hashlib
my_img = Image.open('C:/Users/vishn/PycharmProjects/imo/dtjdtg/Enc images/JPG_8bit/dec_image_jpg_8bit_1.jpg')
# cv2_imshow(my_img)
plt.imshow(my_img)
pix = my_img.load()
row, col = my_img.size[0], my_img.size[1]

key = input()
size = my_img.size
mod = min(size)
print(mod)
enc_key = key
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = enc_key.encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 50, 2048)
print("Derived key:", binascii.hexlify(key))
key=binascii.hexlify(key)
key=str(key, 'UTF-8')
print(key);
key_length = len(key)
key_array = []
key_sum = sum(key_array)
key_arra = []
for key in key:
    key_arra.append(ord(key) % mod)
for i in range(len(key_arra) - 5):
    # adding the alternate numbers
    sum = key_arra[i] + key_arra[i + 1]+key_arra[i + 2]+key_arra[i + 3]+key_arra[i + 4]+key_arra[i + 5]
    key_array.append(sum % mod)
print(key_array)
res = []
#for i in key_array:
#    if i not in res:
#        res.append(i)
i =1
for q in range(size[0]):
    for r in range(size[1]):
        reds = pix[q, r][0] ^ pix[(q - i) % size[0], (r - i) % size[1]][0]
        greens = pix[q, r][1] ^ pix[(q - i) % size[0], (r - i) % size[1]][1]
        blues = pix[q, r][2] ^ pix[(q - i) % size[0], (r - i) % size[1]][2]
        pix[q, r] = (reds, greens, blues)
        reds = pix[q, r][0] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        greens = pix[q, r][1] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        blues = pix[q, r][2] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        # print(key_array[q*r%len(key_array)])
        pix[q, r] = (reds, greens, blues)
plt.imshow(my_img)
plt.show()
my_img.save('CBCoutput1.png')

key = input()
enc_key = key
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = enc_key.encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 50, 2048)
print("Derived key:", binascii.hexlify(key))
key=binascii.hexlify(key)
key=str(key, 'UTF-8')
print(key);
key_length = len(key)
key_array = []
key_arra = []
for key in key:
    key_arra.append(ord(key) % mod)
for i in range(len(key_arra) - 5):
    # adding the alternate numbers
    sum = key_arra[i] + key_arra[i + 1]+key_arra[i + 2]+key_arra[i + 3]+key_arra[i + 4]+key_arra[i + 5]
    key_array.append(sum % mod)
res = []
for i in key_array:
    if i not in res:
        res.append(i)
print(key_array)
i = 1
for q in range(size[0] - 1, -1, -1):
    for r in range(size[1] - 1, -1, -1):
        reds = pix[q, r][0] ^pix[(q-i)%size[0],(r-i)%size[1]][0]
        greens = pix[q, r][1]^pix[(q-i)%size[0],(r-i)%size[1]][1]
        blues = pix[q, r][2] ^ pix[(q-i)%size[0],(r-i)%size[1]][2]
        pix[q, r] = (reds, greens, blues)
        reds = pix[q, r][0] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        greens = pix[q, r][1] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        blues = pix[q, r][2] ^ (key_array[q*r%len(key_array)] ** 2 % 255)
        pix[q, r] = (reds, greens, blues)


plt.imshow(my_img)
plt.show()