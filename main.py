import random 
simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lends = int(input("введите длину пароля:"))
pasvord = ""
for i in range(lends):
    pasvord += random.choice(simvols)
print (pasvord)
