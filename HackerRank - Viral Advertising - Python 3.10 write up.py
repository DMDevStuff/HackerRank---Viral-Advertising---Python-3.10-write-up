##    https://www.hackerrank.com/challenges/strange-advertising/problem
##
##    For the official problem description visit the above link.

##### ##### ##### #####

#   O(n)
#   n is the number of days
#   Algo:
#       1. Initialize variable for total likes, current day likes,
#           current day shares => O(1)
#       2. For each day in range, apply the formula provided in the
#           problem description => O(n)
#       3. Return total likes => O(1)

def viralAdvertising(days):
    
    cumulative_likes = 2
    liked_current = 2
    shared_current = 5
    
    for day in range(2, days+1):
        
        shared_current = liked_current * 3
        liked_current = shared_current // 2      
        cumulative_likes += liked_current
        
    return cumulative_likes
