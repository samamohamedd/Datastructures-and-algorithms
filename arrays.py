import array

a = "apple"
b = "apple"
if a is b:
    print("true")

a1 = [1, 2]
b1 = [1, 2]
if a is b:
    print("true")
# we know that a and b both refer to a string, but we don’t know whether they refer
# to the same string. There are two possible states:
# In one case, a and b refer to two different objects that have the same value. In the
# second case, they refer to the same object.

"""
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        biglist: list[list[int]] = []
        biglist.append([])  # adding empty set
        for item in nums:
            smalllist = []
            for subset in biglist:
                newsebset = subset + [item]
                smalllist.append(newsebset)
                biglist.extend(smalllist)
        print(biglist)

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        biglist: list[list[int]] = []
        biglist.append([])  # adding empty set
        for item in nums:
            smalllist = []
            for subset in biglist:
                newsubset = subset + [item]
                smalllist.append(newsubset)
            biglist.extend(smalllist)
        return biglist

s = Solution()
result = s.subsets([1, 2, 3])
print(result)
"""
s = 'real'

for char in s:
    print (5)

