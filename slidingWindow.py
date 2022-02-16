'''
* Used when we want to operate on a specific window size of a linked list/array
* Windows slides from the start to the end of the array
* Traverse one element at a time

How to identify this type of problem:
- Usually has to do with: linked lists, arrays, string
- Find a substring of a certain quality
- Analyze a portion of a linear data structure of a certain size.

Example of a problem: 
- Max sum subarry of size "K"
- Longest substring with "K" distinct characters
- String anagrams
'''

# Given the problem from leetcode:1343
# Number of Sub-arrays of size K and average greater than or equal to threshold

# Problem 1:
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater
# than or equal to threshold

'''
Problem pseudocode:

1. find the sum of first k ints
2. add to counter if the average is >= threshold
3. for the rest of the array
    - slide the window up by one element
    - calcuate the average of these k elements
    - update counter
4. return counter
'''


class Solution(object):

    def numOfSubarrays(arr, k, threshold):

        count = 0
        sum_t = sum(arr[0:k])

        if sum_t >= k * threshold:
            count += 1

        n = len(arr)
        for i in range(n - k):
            j = i + k

            sum_t = sum_t - arr[i] + arr[j]
            if sum_t >= k*threshold:
                count += 1
        return count
