# We deal with words, numbers, any sequence of units OR phrases

def isPalindrome(string):
    # The string has to be len(string) % 2 != 0
    
    string = string.replace(" ", "") #remove any space in the string
    
    if len(string) % 2 == 0:
        return False
    
    # We now go over the string by comparing both ends of the string one at a time
    low_char = 0
    upper_char = len(string) - 1
    for i in range(int(len(string)/2)): # we only need to loop over half minus one elements of the string
        if string[low_char] != string[upper_char]: # If at one point any character doesn't match, break the loop
            return False
        
        low_char += 1
        upper_char -= 1
    
    return True