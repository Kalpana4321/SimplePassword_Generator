# Simple Password Generator.....
import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '()[]{};_#*._!@$%&=+'
number = '0123456789'

all = lower + upper + number + symbol
#set password length 
length = 10
password = "".join(random.sample(all,length))
print("The Simple Password Generator is: ", password)