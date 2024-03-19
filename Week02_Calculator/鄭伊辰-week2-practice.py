print("請依序輸入數字 運算符號 數字")
n1 = int(input("Enter n1:"))
oprator = input("Enter operator:")
n2 = int(input("Enter n2:"))

if(oprator == "+"):
    print(n1 + n2)
elif(oprator == "-"):
    print(n1 - n2)
elif(oprator == "*"):
    print(n1 * n2)
elif(oprator == "/"):
    if(n2 == 0):
        print("除數不能為 0")
    else:
        print(n1 / n2)
else:
    print("可以好好打算式咪")
