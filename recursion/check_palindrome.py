def is_palindrome(string, start, end):
    if start == end:
        return True;
    
    if string[start] != string[end]:
        return False
    
    if start < end + 1:
        return is_palindrome(string, start + 1, end - 1)
    
    return True
        


if __name__ == "__main__":
    string = input()
    if is_palindrome(string, 0, len(input) - 1):
        print("true")
    else:
        print("false")
