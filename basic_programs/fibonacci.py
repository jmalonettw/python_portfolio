def fib():
    ip1 = 2
    ip2 = ip1
    while (ip1 < 1000):
        print(ip1)
        ip1= ip1 + ip2
        print(ip2)
        ip2= ip1 + ip2
fib()
