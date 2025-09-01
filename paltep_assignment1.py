while True : 
    row = int(input("Enter Number Row : "))

    if row <= 0:
        print("Programs ends here")
        break

    col = int(input("Enter Number Column : "))

    if col <= 0:
        print("Programs ends here")
        break

    search = int(input("Search : "))

    for x in range(1, row + 1):
        for y in range(1, col + 1):
            if x * y == search:
                print(f"[{x * y}]", end=" ")
            else : 
                print(f"{x * y}", end=" ")

        print()
