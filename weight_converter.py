initial_weight = int(input("Your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = round(initial_weight * 0.45, 2)
    print(f'You are {converted} kilos')
elif unit.upper() == "K":
    converted = round(initial_weight / 0.45, 2)
    print(f'You are {converted} pounds')