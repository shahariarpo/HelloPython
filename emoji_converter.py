def emoji_converter(message):
    words = message.split(' ')
    emoji_mapping = {
        ":)": "🙂",
        ":(": "😔",
        ":P": "😛",
        ":p": "😛",
        "xd": "😆",
        "XD": "😆"
    }
    output = ""
    for word in words:
        output += emoji_mapping.get(word, word) + " "
    return output


message = input(">")
results = emoji_converter(message)
print(results)