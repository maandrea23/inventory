#Se crea una funcion la cual permita validar las condiciones necesarias
def inventory(Typeinput,msg,error_msg):
    user_input = input(msg)

    if Typeinput is str:
       if not user_input.strip():
        print(error_msg)
        return inventory(Typeinput, msg, error_msg)

    try:
        value = Typeinput(user_input)
        if Typeinput in (int, float) and value < 0:
            print(error_msg)
            return inventory(Typeinput, msg, error_msg)
        return value
    except ValueError:
        print(error_msg)
        return inventory(Typeinput, msg, error_msg)


name = inventory(str, 'Enter the Product name:  ', 'Error: The name can not be empty').strip()
price = inventory (float, 'Enter the price:  ' , 'Error: The price may be higher than 0')
amount = inventory (int,' Enter the amount:  ', 'Error: The amount may be higher than 0')


costo_total = float (price * amount)
print('Product:', name)
print('Price:' , price)
print('Amount:' , amount)
print('The total price is: ', costo_total)
