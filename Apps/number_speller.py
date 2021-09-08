num_input = input("Number: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""

for characters in num_input:
    output += digit_mapping.get(characters, "Enter a number dummy!") + " "
print(output)