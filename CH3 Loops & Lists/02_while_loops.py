playing = True

while playing:
    res = input("Say 'yes': ")
    if res == "yes":
        print("That is yes!")
        playing = False # or break
    else:
        print("That is not yes! You inputted " + res)
        
print("Congrats!")
