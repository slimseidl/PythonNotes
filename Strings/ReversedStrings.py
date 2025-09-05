text = input("Enter a word to reverse:\n")

while text.lower() not in ("done","d"):
    print(text[::-1])
    text = input("Enter another word to reverse or Done to quit:\n")