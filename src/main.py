from validation import getOption
from menu import menu
from services import choose

print ("Welcome to the inventory")
ToDo= getOption(menu)
print (ToDo)

choose(ToDo)