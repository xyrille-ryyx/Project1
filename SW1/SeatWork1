def toRupee(dollar):
    return dollar * 88.16

def toPound(dollar):
    return dollar * 0.74

def toYuan(dollar):
    return dollar * 7.12

while True:
    dollar = input("Enter Dollar ($) (* to Exit): ")
    if dollar == "*":
        print("End of the Program.")
        break
    dollar = dollar.split("@")

    count = 0

    
    print("\nDollar ($) - Indian Ruppe (R) - British (Pound) - China (Y)")
    for x in range(count, len(dollar)):
        rupee = toRupee(int(dollar[count]))
        pound = toPound(int(dollar[count]))
        yuan = toYuan(int(dollar[count]))

        print(f"{dollar[count]} - {rupee : .2f} - {pound: .2f} - {yuan : .2f}")
        count += 1
    print()
