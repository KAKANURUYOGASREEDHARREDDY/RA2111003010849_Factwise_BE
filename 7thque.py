def maxScore(cardPoints,k):
    total_points=sum(cardPoints)
    window_size=len(cardPoints)-k
    current_sum=sum(cardPoints[:window_size])
    min_sum=current_sum
    for i in range(window_size,len(cardPoints)):
        current_sum+=cardPoints[i]-cardPoints[i-window_size]
        min_sum=min(min_sum,current_sum)
    return total_points-min_sum
#example 1 
cardPoints1=[1,2,3,4,5,6,1]
k1=3
print("Example 1 output:",maxScore(cardPoints1,k1))

#example 2 
cardPoints2=[2,2,2]
k2=2
print("Example 2 output:",maxScore(cardPoints2,k2))

#example 3 
cardPoints3=[9,7,7,9,7,7,9]
k3=7
print("Example 3 output:",maxScore(cardPoints3,k3))

#output
#Example 1 output: 12
#Example 2 output: 4
#Example 3 output: 55

#=== Code Execution Successful ===
