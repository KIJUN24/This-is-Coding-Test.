while True:
    num = input().strip()
    if num == "0":
        break
    if num == num[::-1]:
        print("Yes")
    else:
        print("No")