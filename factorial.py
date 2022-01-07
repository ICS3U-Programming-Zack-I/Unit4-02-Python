# Created by: Zack Isingoma
# Created on: 6th Jan 2022.
# the program finds the factorial of the given number
def main():
    num = input("enter a number: ")
    fac = 1
    i = 1
    print("")
    try:
        number = int(num)

        while i <= number:
            fac = fac * i
            i = i + 1

        print("factorial of ", number, " is ", fac)
    except Exception:
        print("{} is invalid input".format(number))


if __name__ == "__main__":
    main()
