def substring(str):
    print(str[:len(str)//2])
    return str[:len(str)//2]

# print(substring("qwertykeyboards"))

def reverse(data):
    data = list(data)
    start = 0
    end = len(data)-1
    while end> start:
        data[start],data[end] = data[end],data[start]
        start = start + 1
        end = end - 1
    return ''.join(data)

def palindrome(string):
    if string == string[::-1]:
        return True

    return  False

def is_palindome(string):
    original = string
    reversed_string = reverse(original)
    if reversed_string == original:
        return True
    return False

def reverse_num(num):
    reverse_number = 0
    remainder = 0

    while num > 0:
        # print(num)
        remainder = num%10
        num = num//10
        reverse_number = reverse_number*10 + remainder
        print(reverse_number)
    return reverse_number

def is_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False
def duplicates(nums):
    for num in nums:
        if nums[abs(num)] >=0:
            nums[abs(num)] = - nums[abs(num)]
        else:
            print(f"repetition found:{str(abs(num))}")


if __name__ == "__main__":
    # print(is_palindome('racecar'))
    # print(reverse_num(1234))
    print(is_anagram('restful', 'fluster'))
    # print(duplicates([1,2,3,2,1]))