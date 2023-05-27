def urled(s):
    
    # t = s.replace(" ", "%20")
    # return t
 
    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "%20"
            
    return s

print(urled("th sdfgh fcgvhbjn 23r3d"))