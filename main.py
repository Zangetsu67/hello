word="hello"
n=len(word)
for i in range(1,n+1):
    print(word[:i])
for i in range(n-1,0,-1):
    print(word[:i])