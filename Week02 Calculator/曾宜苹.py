print("請開始您的計算")
n1 = int(input("請輸入數字一: "))
n1 = int(n1)
c = input("請參考括號內符號選擇運算符號並則依輸入(+,-,*,/): ")
n2 = int(input("請輸入數字二: "))

if c == "+":
    print(n1 + n2)
elif c == "-":
    print(n1 - n2)
elif c == "*":
    print(n1 * n2)
elif c == "/":
    print(n1 / n2)
else:
    print("Error, 請從以下運算符號擇一輸入:+,-,*,/")
    
