#largest and smallest number
arr=[10,20,30,40,50,]
name=["aditya"]
largest=arr[0]
smallest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
       largest=arr[i]
    
    if arr[i]< smallest:
      smallest = arr[i]
      
      
print ("largest element in array:", largest)
print ("smallest element in array:", smallest)
print("hi",name)
        