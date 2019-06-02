"""Given a string, find the length of the longest substring without repeating characters."""

string1 = "pwwkew"


def longest_substring(string1):
    """Return the length of longest substring.

    >>> longest_substring("abcabcbb")
    3
    >>> longest_substring("pwwkew")
    3
    """
    used_chars = dict() # Initializing the used_chars dictionary
    start = length = 0 # start tracks the start of the substring and the length tracks the length
    for i in range(len(string1)):
        if string1[i] in used_chars and start <= used_chars[string1[i]]: 
        # if the char is in used chars and start is index less than used_chars index
                start = used_chars[string1[i]] + 1
        else:
            length = max(length, i-start+1) 
        used_chars[string1[i]] = i  # add the char to used_char or update the index
    #print used_chars
    #print "Length of the Longest substring is: "
    return length

if __name__=='__main__':
    print longest_substring(string1)
    import doctest
    doctest.testmod()