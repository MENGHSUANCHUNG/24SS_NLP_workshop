num = input("請輸入兩個數字，請用空格連接：").split()
n1 = int(num[0])
n2 = int(num[1])
op = input("請輸入運算符號 (+, -, *, /)：")
if op == '*':
    print(f"答案是：{n1*n2}")
elif op == '/':
    print(f"答案是：{n1/n2}")
elif op == '-':
    print(f"答案是：{n1-n2}")
elif op == '+':
    print(f"答案是：{n1+n2}")
else:
    print("輸入符號須為 +, -, *, /, 重來ㄅ")
