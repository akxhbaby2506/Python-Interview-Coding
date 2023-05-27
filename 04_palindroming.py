def palindrom(word):
    
    word = word.lower()
    beg = 0
    end = len(word)-1
    
    charss = "!@#$%^&*()_+-=`~}{[],./?\|/*;: "
    
    while(beg<end):
        
        # if (word[beg] == " "):
        #    beg = beg + 1
                                         # print(palindrom("taco cat")) --> only if there is a space it skips, not for spcl chracters
        # if (word[end] == " "):
        #    end = end - 1
        
        if (word[beg] in charss):
            beg += 1
        if (word[end] in charss):
            end -= 1
        
        if (word[beg] != word[end]):
            return False
        beg = beg + 1
        end = end - 1
    return True
        
print(palindrom("MalAyalam"))
print(palindrom("jnvuiew"))
print(palindrom("tAco Cat"))
print(palindrom("t aco, cat"))  #False if top 2 if condittions are commented out (why??)
print(palindrom("A man, a plan, a canal: Panama")) #False (why??)