for n in range(10):
    if n==6:
        break
    print(n,end=',')

for n in range(10):
    if n%2 ==0:
        print("Even",n)
        continue
    print("Odd",n)
