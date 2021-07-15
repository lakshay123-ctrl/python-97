intro = input("enter your introduction")
cc = 0
wordcount = 1
for i in intro:
    cc = cc+1
    print(cc)
    if (i == " " ):
        wordcount = wordcount+1
print("number of words")
print(wordcount)
print("number of characters")
print(cc) 