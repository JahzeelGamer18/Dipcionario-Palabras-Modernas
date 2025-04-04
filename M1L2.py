import random

longi = int(input("Ingresa la cantidad de letras que quieres que tenga la pasword: "))

pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña = ""

for i in range(longi):
    contraseña += random.choice(pw)

print("Tu contraseña generada es:", contraseña)


