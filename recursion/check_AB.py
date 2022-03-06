def checkAB(string):
    if not string:
        return True
	
    if string[0] == 'a':
        if len(string[1:]) > 1 and string[1:3] == "bb":
            return checkAB(string[3:])
        else:
            return checkAB(string[1:])
    
    return False


if __name__ == "__main__":
    string = input()
    result = checkAB(string)
    print("true" if result else "false")
