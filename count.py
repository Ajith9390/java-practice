n =153
temp=n
count=0;
while(temp!=0):
    div = temp%10
    count=count+1
    temp = temp//10
print(count)

i=1
for i in range(9,11):
 print(i)

 i=1
 for i in range(1,20):
     if i%2==0:
         print(i)


sum=0;     
for i in range(0,10):
    sum = sum+i
print(sum)
n=5
for i in range(1,11):
    print(n,"x",i,"=", n*i)


n=153
rev=0
temp=n
while(temp!=0):
    div = temp%10
    rev = rev*10+div
    temp = temp//10
print(rev)


n=153
#temp=n
count=0
while(n!=0):
    div = n%10
    count =count+1
    n=n//10
print(count)

n=5
fact=1
for i in range(1,n+1):
    fact = fact*i
print(fact)

n=6
count=0
for i in range(1, n+1):
    if n%i==0:
        count = count+1
if count==2:
    print("Prime:")
else:
    print("Not Prime:")



n=5

first=0
second=1
for i in range(n):
    temp =first+second
    print(first)
    first=second
    second=temp


n=5
first=0
second=1
if(n==0):
    print(first)
elif (n==1):
   print(second)
else:
    
 for i in range(2,5):
    temp = first+second
    first=second
    second=temp
print(second)




n=153

temp = n
count=0
while(temp!=0):
    div = temp%10
    count = count+1
    temp = temp//10

temp1=n
sum=0
while(temp1!=0):
    
    div1 = temp1%10
    power=1
    for i in range (count):
        power = power*div1
    sum = sum+power
    temp1=temp1//10
if sum==n:
    print("It is a Arsmstrong number:")
else:
    print("It is  not a Armstrong number:")




s="python"
reverse=""

for i in s:
    reverse = i+reverse
print(reverse)


s="mam"
reverse=""

for ch in s:
    reverse = ch+reverse
    

if s==reverse:
    print("It is a palindore string:")
else:
    print("It is  not a palindrome string:")
    
    
    
    
    
    
s = "java"
result = ""

for ch in s:
    found = False

    for x in result:
        if ch == x:
            found = True
            break

    if found == False:
        result = result + ch

print("After Removing Duplicates:", result)

    


    
    




        
    
     
    
    
