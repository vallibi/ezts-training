#write a python p3rogram to make encryption and decryption with a key a value using functions
#   encryption=giving codes to char   char-ascii,   decryption=obtaining char from codes  ascii-char
#chr for decrypt(-), ord for encryption(+)

def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k      #Enter the key value:3#Enter string:vallibi#select operation:encrypt#ydoolel
        s1+=chr(x)                         
    print(s1)
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)     #Enter the key value:3#Enter string:vallibi#select operation:decrypt#s^iif_f                        
    print(s1)                               
k=int(input("Enter the key value:"))
s=input("Enter string:")
op=input("select operation:")
if op == "encrypt":
    encryption(s,k)
elif op == "decrypt":
    decryption(s,k)
else:
    print("inproper operation")
    
    

