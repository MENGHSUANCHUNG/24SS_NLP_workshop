a = int(input("請輸入數字一:"))
b = int(input("請輸入數字二:"))
c = input("請輸入一個運算符號(+,-,*,/):")
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("輸入錯誤符號，請重新輸入")