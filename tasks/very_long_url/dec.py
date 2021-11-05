#python3 dec.py < url.txt
url = input()
for i in range(3):
    url_rep = url.replace('o','0').replace('ο','1').replace('о','2').replace('ᴏ','3')[26:]
    url = bytearray.fromhex(hex(int(url_rep,4))[2:]).decode()
print(url[7:-1])