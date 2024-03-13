x = int(input("請輸入數字一:"))
y = int(input("請輸入數字二:"))
z = input("請輸入運算符號:")

if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
else:
    print("no")