s = "he,llo,2,dog"

i = 2 
print(s[0:i])
s = s[i+1:len(s)] # s now becomes llo,2,dog

i = 3
print(s[0:i])
s = s[i+1:len(s)] # s now becomes 2,dog

i = 1
print(s[0:i])
s = s[i+1:len(s)] # s now becomes dog

i = 3
print(s[0:i])
s = s[i+1:len(s)]  # s now becomes <EMPTY>

# print(s)