1. Write a python program to accept list of integers
    and print the total sum of odd elements within 
    the list 
 
solution:
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 2 == 1:
        result = result + ele 
print(result)
 
2. Write a python program to accept a list of 
    integers and print the total count of numbers 
    which are divisible by 5 
 
solution:    
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 5 == 0:
        result = result + 1 
print(result)
 
 
3. Write a python program to accept a list of
    integers and print total count of negative
    numbers in the list 
 
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele < 0:
        result = result + 1 
print(result)
 
 
4. Write a python program to accept a list of 
    integers and print the average of these 
    numbers 
 
nums = list(map(int, input().split()))
#temp = sum(nums)
sumOfElements = 0 
for ele in nums:
    sumOfElements = sumOfElements + ele 
print(sumOfElements // len(nums))
 
 
 
5. Write a python program to accept a list of
    integers and print sum of 2nd greatest 
     element and 2nd smallest element from list
 
 
nums = list(map(int, input().split()))
result = 0 
nums = sorted(nums)
result = nums[1] + nums[n - 2]
print(result)
 
 


