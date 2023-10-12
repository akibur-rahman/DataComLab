flag = input("Enter Flag:")
data = input("Enter Data:")

fiveOneCount=data.count('11111')

stuffed=data.replace('11111','111110',fiveOneCount)
stuffed=flag+stuffed+flag
print(stuffed)

destuffed=stuffed[len(flag):len(stuffed)-len(flag)]
destuffed=destuffed.replace('111110','11111')
print(destuffed)