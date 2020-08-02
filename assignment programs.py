

# Prg to check whether the given string is palindrome or not:

s=input("enter a string:")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Prg to sort words in alphabetic order

x=["sandeep","arjun","vijay","infiag"]
print(list.sort(x))
print(x)

# Prg to find largest of 3 numbers:

n1=12
n2=4
n3=33
if n1>n2 and n1>n3:
    l=n1
elif n2>n1 and n2>n3:
    l=n2
else:
    l=n3
print("the largest number is:",l)

# prg to find largest number inside the list:

x=[23,44,12,23,11,48,25]
x.sort()
print("largest number inside the list is:",x[-1])

# program to find 2nd and 4th as well as 3rd and 5th largest number in the given list:

x=[23,44,12,24,11,48,25]
x.sort()
print("the 2nd and 4th largest numbers are",x[1],x[3])
print("the 3rd and 5th largest numbers are",x[2],x[4])

# check whether the given number is prime or not:

n=7  #given number
i=2
f=0
while i <= n/2:
    if n % i==0:
        f=1
        break
    else:
        i=i+1
if f==1:
    print("its not a prime number")
else:
    print("its a prime number")

#  print prime numbers between given two numbers:

m=int(input("enter the first number:"))
n=int(input("enter the second number"))
for num in range(m,n + 1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
               print(num)

# prime numbers between given two numbers are:

m=10
n=50
print("prime numbers between",m,"and",n,"are:")
for num in range(m,n + 1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
               print(num)

# Prg to print pyramid of numbers:

n=int(input("enter the number of rows:"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()


# Prg to print triangle pattern using 0's and 1's:

n=6
for i in range(1,n):
    for j in range(1,i):
        r=j%2
        print(r,end=" ")
    print("\n")
