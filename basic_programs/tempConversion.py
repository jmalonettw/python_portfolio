def tempcon():
    def check_int():
        global temp
        temp = input("What temperature would you like to convert?")
        try:
            temp = float(temp)
        except ValueError:
            print("You need to enter a number.")
            check_int()
    check_int()

    def check_spelling():
        conTo = input("Would you like to convert it to Fahrenheit (F) or Celsius (C)")
        if conTo == "Celsius" or conTo == "C" or conTo == "c":
            convert_temp = (temp - 32) * .5556
            print(str(temp) + " Fahrenheit would be " + str("{0:.1f}".format(convert_temp)) + " in Celcius.")
        elif conTo == "Fahrenheit" or conTo == "F" or conTo == "f":
            convert_temp = temp * 1.8 + 32
            print(str(temp) + " Celcius would be " + str("{0:.1f}".format(convert_temp)) + " in Fahrenheit.")
        else:
            print('You need to input "Fahrenheit", "Celcius", "F", "C", "f", or "c".')
            check_spelling()
    check_spelling()

tempcon()
