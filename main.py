def main():
    x = int(input("Enter your decimal number: "))
    binary = ""
    while x > 0:
        binary = str(x % 2) + binary
        x //= 2
    print(f"Your binary number is : {binary}")
    y = str(input("Wanna convert another decimal number? (Y/y):"))
    if y in ["Y", "y"]:
        main()
    else:
        print("Goodbye!")
        exit()
main()
