def sum_of_two(nums,target):
    prevMap ={}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return None

def maxProfit(prices):
    l = 0
    r = 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
            
        else:
            l = r
        r = r+1
    
    return maxP

def containsDuplicate( nums) :
    hashmap = set()
    for i in nums:
        if i not in hashmap:
            hashmap.add(i)
        else:
            return True
    return False

def productExceptSelf(nums):
    res = [1] *len(nums)
    prefix = 1
    for i in range(len(nums)):
        print(i)
        res[i] = prefix
        prefix = prefix * nums[i]
    postfix =1
    for i in range(len(nums)-1,-1,-1):
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]
    return res

def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0
    for i in nums:  
        if curSum < 0:
            curSum=0
        curSum +=i
        maxSub = max(curSum,maxSub)
    return maxSub

def maxProduct( nums):
    res = max(nums) #[2,3,-2,4]
    curMin,curMax = 1,1
    for n in nums:
        if n==0:
            curMin=1
            curMax=1
            continue
        tmp = n*curMax #2,6,-12,-24
        curMax = max(tmp,n*curMin,n) #2,6,
        curMin = min (tmp,n*curMin,n) #2,-4,-12,-24
        res = max(res,curMax,curMin)
    return res

def findMin( nums):
    res = nums[0]
    l=0
    r = len(nums) -1
    while l <=r:
        if nums[l] < nums[r]:
            res =  min(res,nums[l])
            break
        m = (l+r) // 2
        res = min(res,nums[m])
        if nums[m] >= nums[l]:
            l = m +1
        else:
            r = m -1
    return res
                 
def search(nums, target): # nums = [4,5,6,7,0,1,2], target = 0
    l,r = 0 ,len(nums)-1
    while l <=r:
        mid = (l+r) // 2
        if target == nums[mid]:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid +1
            else:
                r = mid -1
        else:
            if target < nums[mid] or target >nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

def threeSum(nums):
    res = []
    nums.sort()
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l,r = i+1, len(nums) -1
        while l <r:
            threeSum = a + nums[l] + nums[r]
            if threeSum >0:
                r -=1
            elif threeSum <0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while  nums[l]  == nums[l-1] and  l <r:
                    l+=1
    return res
            
def maxArea(height) :
    res = 0
    l,r = 0,len(height) -1
    while l < r:
        area = (r - l) * min(height[l],height[r])
        res = max(res,area)
        
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return res

def getSum(a, b):
    Sum = sum([a,b])
    return Sum

def hammingWeight(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res

def countBits(n):
    dp = [0] * (n+1)
    print(dp)
    offset=1
    for i in range(1,n+1):
        print(i)
        if offset * 2 == i:
            print("here",offset * 2)
            offset = i
            print(offset)
        
        dp[i] = 1 + dp[i - offset]
        print('dp[i]',dp[i])
    return dp

def missingNumber(nums):
    hashset = set()
    n = max(nums)
    print(n)
    data = list(range(1,n+1))
    print(data)
    for i in data:
        hashset.add(i)
    for n in nums:
        if n in hashset:
            hashset.discard(n)
    return hashset.pop()    

def missingNumber(nums):
    n = len(nums) +1 
    for i in range(n):
        if i not in nums:
            return i

def findDuplicate(nums):
    hashset = set()
    for i in nums:
        if i  in hashset:
            return i
        hashset.add(i)

def findErrorNums(nums):
    hashset = set()
    duplicate = None
    for i in nums:
        if i  in hashset:
            duplicate = i
        else:
            hashset.add(i)
    for i in range(1,len(nums)+1):
        if i not in nums:
            return [duplicate,i]

def firstMissingPositive( nums):
    my_nums = set(nums)
    for i in range(1,len(my_nums)+1):
        if i not in my_nums:
            return i

def intToRoman( num):
    dicti = {1000: 'M',
            900: 'CM', 
            500: 'D', 
            400: 'CD', 
            100: 'C', 
            90: 'XC', 
            50: 'L', 
            40: 'XL', 
            10: 'X', 
            9: 'IX', 
            5: 'V', 
            4: 'IV', 
            1: 'I'} 
    
    res = ""
    
    for i in dicti:
        res += (num//i) * dicti[i]
        num %= i
    return res

def romanToInt(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    summ= 0
    for i in range(len(s)-1,-1,-1):
        num = roman[s[i]]
        if 3*num < summ: 
            summ = summ-num
        else: 
            summ = summ+num
    return summ
                    
                   

if __name__ == "__main__":
    # res = productExceptSelf([1,2,3,4])
    # res  = countBits(4)
    # res = missingNumber([0,1])
    print('res',"res")
    # print(sum_of_two([2,4,5,6], 6))