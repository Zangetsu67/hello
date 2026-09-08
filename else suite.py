l=[1,2,3,4,5,6]
n=int(input("enter element to search"))
for i in l:
    if n==i:
        print("element found")
        break
else:
    print("element not found")