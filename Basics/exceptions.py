try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
    print(f"Risk is {risk}")
except ValueError:
    print("Invalid age!")
except ZeroDivisionError:
    print("Age cannot be 0.")