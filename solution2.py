#you are given an array of integers, your task is to create pairs of them , such that every pair consists of equal numbers. Each array element may belong to one pair only. it is possible to use all of the integers? 
#Write a function :
#def solution(A)
#that , given an array A consisting of N integers , returns whether it is possible to split all integers into pairs. 

#Examples: 
#1.Given A=[1,2,2,1], your function should return True , as the pairs are (A[0],A[3]) both have value 1 and (A[1],A[2]) both have value 2.
#2. Given A=[7,7,7] , your function should return False, as you can make one pair of numbers 7 , but still have a single 7 left.
#3.Given A=[1,2,2,3,] , your function should return False , as there's nothing that A[0] can paired with .

#Assumptions:
#*N is an integer within the range [1..100,000]
#*each element of array A is an integer  within the range [-1,000,000..1,000,000]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    counts = {}
    
    # count the occurrences of the numbers
    for num in A:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    

    for count in counts.values():
        # check for odd, there cannot be an equal pair for that number
        if count % 2 != 0:
            return False
    
    # check for even, so we  can form pairs for each number
    return True
    pass

