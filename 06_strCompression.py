def strCompression(word):
    
    word = sorted(word)
    compress = ""
    count = 0
    for i in range(len(word)):
        count = count + 1

        if ((i+1)>=len(word)) or (word[i] != word[i+1]):
            compress = compress + (""+word[i]+str(count))
            count = 0

    return compress
print(strCompression("aaabbabccbcaac"))