age = int(input())
balance = 9000
if 7<=age<=12:
    balance = 9000-650
elif 13<=age<=18:
    balance = 9000-1050
else:
    balance = balance-1250
print(balance)