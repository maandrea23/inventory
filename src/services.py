from validation import choose
from main import ToDo

choose(ToDo)
def choose (c1):


    match c1:
        case 1:
            print("morning")
        case 2:
            print ("afternoon")
        case 3:
            print ("night")
        case 4:
            print ("bye")
        case _: 
            print("out of the time")