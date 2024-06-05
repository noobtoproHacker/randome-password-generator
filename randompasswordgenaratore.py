import random

alphabets = ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z").split()
symbols = ("+-*/=-():;'")
password = ""
len_of_symbols=len(symbols)-1


letters=int(input("How many letter would you like to have in your password ?\n"))
star=int(input("How many symbols would you like to have in your password ?\n"))

num=int(input("How many numbers would you like to have in your password ?\n"))


for x in range(1,letters+1):
    random1=random.randint(0,23)
    random2=random.randint(0,2)
    if(random2 == 1):
        password += (alphabets[random1]).lower()
    else:
        password += (alphabets[random2])

password=list(password)
length_of_password=int(len(password)-1)

for y in range (1,star+1):
    randomindex=random.randint(0,length_of_password)

    password.insert(randomindex,symbols[random.randint(0,10)])

for z in range (1,num+1):
    randomindex=random.randint(0,length_of_password)

    password.insert(randomindex,str(random.randint(0,num)))
password="".join(password)
print(password)



