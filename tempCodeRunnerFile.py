flag = input("Enter Flag:")
esc = input("Enter Escape character:")
data = input("Enter Data:")

# Stuffing
flagCount = data.count(flag)
# adding escape characters before flags
stuffed = flag+(data.replace(flag, esc+flag, flagCount))+flag
# adding flag in begining and end
print("Stuffed Data: "+stuffed)

# De-stuffing
flagEscCount = stuffed.count(esc+flag)
# removing internal escape sequence
destuffed = stuffed.replace(esc+flag, flag, flagEscCount)
destuffed = destuffed[len(flag):(len(destuffed)-len(flag))]
print("Destuffed Data: "+destuffed)
