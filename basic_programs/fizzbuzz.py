ip1 = 3
ip2 = 5
max = 1000

def fizzBuzz():
    for num in range(1,max):
        if num % ip1 == 0 and num % ip2 == 0:
            print("Fizzbuzz!")
        elif num % ip1 == 0:
            print("Fizz")
        elif num % ip2 == 0:
            print("Buzz")
        else:
            print(num)

fizzBuzz()
