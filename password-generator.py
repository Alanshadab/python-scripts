import random 
import string

length = 12
charakters = string.asci_letters + string.digits + "!@#$%"
password = ''.join(random.choice(characters) for i in range(lenghth))
print("generator password:",password)
