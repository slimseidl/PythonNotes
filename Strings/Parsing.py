words = input("Enter input string:\n")
while words != "q":    
    if "," not in words:
        print("Error: No comma in string.\n")
    else:
        wordList = words.split(",")
        print(f'First word: {wordList[0].strip()}\nSecond word: {wordList[1].strip()}\n')
    words = input("Enter input string:\n")

