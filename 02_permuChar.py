def permutation_char(s,t):
    
    if (len(s) != len(t)):
        return False
    
    if (sorted(s)!=sorted(t)):
        return False
    else:
        return True

print(permutation_char("rat","tra"))
print(permutation_char("car","tar"))