def Unique(s):
    
    ans = "No"

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans = "No"
        elif s[i] != s[i+1]:
            ans = "Yes"

    return ans  

s = "abcdefgg"
print(Unique(s))
