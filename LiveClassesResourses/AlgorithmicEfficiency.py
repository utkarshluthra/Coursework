# Time - no. of times the program runs to give a certain output
# Space - memory

# if x==1:
#     x+=1
#     print(x)

#     time is directly proportional to the value x --> constant --> x 


# Internal:
# 1. Time
# 2. Space

# External:
# 1. Size of input
# 2. RAM, and Storage
# 3. Quality of Compiler/inperpretter

# Effective Algo - The degree to which the algorithm carries out its intended function correctly

# Efficient Algo - The degreee to which the algorithm is correct with the best possible performance

# Complexity: It is the study of the factors to determine how much resource is sufficient and necessary for the algorithm.

# 1. Time Complexity: Time taken to run the algorithm in ideal conditions.
#                     No. of times the algorithm runs to give final output

#                     For a given set of input, it is the no. of elementary instructions that the program executes wrt the size n of the input data.

# 2. Space Complexity: (Network Traffic (for web)) The amount of data needed to run a specific program in ideal conditions



#             Best Case - Worst Case - Average Case 
# Notation =  Omega(k)        O()        Theta()

# log --> log_2(x)

# Common O-Notation:
# 1. Constant O(k)        --> Adding an element to the front of list      --> Simples
# 2. Logarithm O(log)     --> Search in sorted array                      --> Binary Search
# 3. Linear O(n)          --> Searching in unsorted array                 --> Loops
# 4. nlogn                --> Sorting
# 5. Quadratic O(n^2)     --> Bubble Sort and Insertion Sort              --> Nested Loops
# 6. Cubic O(n^3)         --> Equating Equation
# 7. Exponetial O(2^n)    --> Tower of Hanoi Problem

# Step 1: Choose the elementary instruction
# Step 2: Analyze the code - Identify the parts

# -Statements
# -Loop _/
# -Nested Loop _/
# -Conditionals 
# -Consecutive statements _/
# -Function = 'A function is as good as the composition' _/

# Step 3: Estimate the size of input 

# Step 4: Select your prefered notation - omega() theta() O() -(Big oh notation)

# Best Case - 
# Ease of understanding low
# Efficiency high

# Worst Case:
# Ease of understanding high
# Efficiency low


# Rules:
# 1. Simple statement are of O(1).
#     1.1 When one is assigning an array in which case it will be O(n) where n is the size of array

# 2. A function call has o(1) in case of no arguments
#     2.1 If there are arguments, the O-notation is given as O(n) where n is the number of arguments

# *3. Addition Rule: You can combine a squence of statements by using the addition rule which states that the running time of a sequence of statements is just the maximum of the running time ofg each individual statement.

# *4. Multiplication Rule: You need to determine the running time of the loop body and the number of times the loop iterates. Frequently, you can just multiply th run time of the body byt the number of iterations

# for i in range(3000):
#     print("Hello WOrld")
#     print("Bye World")
 
#     Total time = 3000 x O(2) = O(6000) 

# for i in range(n):
#     for j in range(n):
#         print(1)

# Total Time =  O(1*n*n) = O(1 x n^2) --> O(n^2)

# In CS, whenever we talk about log, we are stating binary log. log_2()

# a=int(input("Enter a number"))
# while i<=a:
#     a+=1
#     print(a)
#     i=2/i

# n --> n/2 --> n/4 --> n/8 ---> n/16 -->...--> n/(2^k)

# n/(2^k) <= 1
# n <= 2^k

# log_2(n) <= log_2(2^k)
# logn <= k

# O(logn)

# n=int(input("Enter a number: "))
# count=0
# for i<=n:
#     for j<=n:
#         count+=1
#         j+=i
#     i+=1
# print(count)

# i=1
#     j=1,2,3,4...,n
# Time: n

# i=2
#     j=1,3,5,7,..,(2n-1)
# TIme: n/2

# i=3
#     j=1,4,7,10,...
# Time: n/3
# .
# .
# .
# .
# i=n
#     j=1
# TIme: 1

# Time taken = 1+...+n/3+n/2+n
#             =   n(1/n+...+1/3+1/2+1)
#             =   nlogn

#             O(nlogn)
            


# O(n) _=>_ O(1)

# O(nlogn) __<=__ O(n^2)

# O(2^n)  __>>>__  O(n^2)

# O(n^3) __=__ O(n^3)