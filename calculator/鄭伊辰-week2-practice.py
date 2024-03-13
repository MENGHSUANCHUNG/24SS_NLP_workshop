print("請依序輸入數字 運算符號 數字")
n1 = int(input("Enter n1:"))
oprator = ord(input("Enter operator:"))
n2 = int(input("Enter n2:"))

if(oprator == 43):
    print(n1 + n2)
elif(oprator == 45):
    print(n1 - n2)
elif(oprator == 42):
    print(n1 * n2)
elif(oprator == 47):
    if(n2 == 0):
        print("除數不能為 0")
    else:
        print(n1 / n2)
else:
    print("可以好好打算式咪")
