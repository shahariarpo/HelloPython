message = input(">")
words = message.split(' ')
emoji_mapping = {
    ":)" : "🙂",
    ":(" : "😔",
    ":P" : "😛",
    ":p" : "😛",
    "xd" : "😆",
    "XD" : "😆"
}
output = ""
for word in words:
    output += emoji_mapping.get(word, word) + " "
print(output)