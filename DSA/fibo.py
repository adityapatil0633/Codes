#fibo number
n=10

a = []
a.append(0)
a.append(1)
  
for i in range(2,n):
    num =a[2-1]+ a[i-1]
    a.append(num)
    
print("fibonacci number is:",a)    