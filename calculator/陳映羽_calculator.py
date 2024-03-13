n1 = int(input("請輸入數字一: "))
w = input("請輸入運算符號: ")
n2 = int(input("請輸入數字二: "))

if w == "+" :
    print(n1 + n2)

elif w == "-" :
#print("數字一 - 數字二 =")
    print(n1 - n2)

elif w == "*" :
#print("數字一 * 數字二 =")
    print(n1 * n2)

elif w == "/" :
#print("數字一 / 數字二 =")
    print(n1 / n2)

else :
    print("error")