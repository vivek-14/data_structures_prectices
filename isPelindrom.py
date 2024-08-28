x = 1234

def is_palindrome(x):
    listed_nums = [ int(val) for val in str(x) ]
    
    print(type(listed_nums))
    if listed_nums == listed_nums[::-1]:
        return True
    return False


print(is_palindrome(x))
