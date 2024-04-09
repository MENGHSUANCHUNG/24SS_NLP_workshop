num1 = float(input("請輸入第一個數字: "))
operator = input("請輸入運算符 (+, -, *, /): ")
num2 = float(input("請輸入第二個數字: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"結果: {result}")