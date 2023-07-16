import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(9, 13)))
print("İşte Güçlü Bir Şifre:" + password)
