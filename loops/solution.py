# sol 1
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
y=0
for x in numbers:
    if x < 0:
        y+=1
print("The number of negative numbers in the list is:", y)

# sol 2
sum=0
n=5
for x in range(1,n+1):
        if(x%2==0):
            sum+=x
           
print("The sum of the even numbers from 1 to",n,"is:",sum)

# sol 3
n=2
for x in range(1,11):
        if(x!=5):
            print(n*x)
       

# sol 4
str="teena sajwan"
rev_str=""
for x in str:
     rev_str=x+rev_str
print("The reverse of the string is:", rev_str)

# sol 5
str="hallahlujiah"
for x in str:
     if(str.count(x)==1):
          print("the first non repeating character is:",x)
          break

# sol 6
n=5
fact=1 
for x in range(1,n+1):
     fact*=x
print("The factorial of",n,"is:",fact)
# sol 7
n=int(input("Enter a number: "))
while True:
    if 1<= n<=10:
        print("thanks the number is between 1 and 10")
        break
    else:     
        print("the number is not between 1 and 10, please enter the number again")
        n=int(input("Enter a number: "))
     
    #  sol 8
n=int(input("Enter a number: "))
for x in range(2,n):
     if(n%x==0):
          print("not a prime number")
          break

# sol 9
items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()
for x in items:
     if x in unique_items:
           print("Duplicate item found:", x)
           break
     else:           unique_items.add(x)

    # sol 10
    # Problem: Implement an exponential backoff strategy
    #  that doubles the wait time between retries,
    #  starting from 1 second, but stops after 5 retries.
import time
max_tries=5
Wait_time=1
tries=0
while(tries<max_tries):
   print("Attempt", tries+1,"- Waiting for", Wait_time, "seconds before retrying...")
   time.sleep(Wait_time)
   Wait_time*=2
   tries+=1
