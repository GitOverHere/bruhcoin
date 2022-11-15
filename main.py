#generate sets of random strings
import string
import random
import hashlib


import string
import random
def randomstring(size=4, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))


with open("blockchain", 'r+') as f:
 f.truncate(0)
 f.close()




print("Hello! How many coins would you like to hash to craete the blockchain.")
coins = int(input())

f = open('blockchain','a')


while(coins > 0):
 hash = hashlib.sha256()
 coinstr = randomstring()
 hash.update(coinstr.encode('ascii'))
 f.write(hash.hexdigest()+"\n")
 coins -= 1
 
print("Done generating coins lol.")
 
 
