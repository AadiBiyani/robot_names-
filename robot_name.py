import string 
import random


def robot_name():
        numbers = random.randint(0,999)
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        print (letters + str(numbers))
        
        pass
def rand_reboot():    
    if random.randint(0,1) == 1:
        robot_name()
    else:
        print ("No reboot!")

rand_reboot()
    

