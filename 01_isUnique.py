def uniChar(s):
    
    chars = "!@#$%^&*()_+-=/*\|;:,.<>}{[]"
    
    for i in s:
        if i in chars:
            return True
    else:
        return False
    
print(uniChar("sdfgh"))
print(uniChar("FTFY+hfh#e2345tyhjbh"))