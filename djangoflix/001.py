def substring(str):
    print(str[:len(str)//2])
    return str[:len(str)//2]

print(substring("qwertykeyboards"))

def reverse(data):
    start = 0
    end = len(data)-1
    while end> start:
        data[start],data[end] = data[end],data[start]
        start = start + 1
        end = end - 1

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
