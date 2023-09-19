#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  
If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''
import math
def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle

    '''
    length = len(input)
    length /= 2
    #length = int(round(length, 0))
    length = int(length)
    length = math.floor(length)
    charlist = [x for x in input]
    x = charlist[length-1]
    if charlist[int(length-1)] == " ":
        charlist.insert(length, "\n")
    else:
        if charlist[length-2] == " " and charlist[length] == " ":
            charlist.insert(length, "\n")
        else:
            charlist.insert(length, "-\n")
    charlist = "".join(charlist)
    print(charlist)
    return str(charlist)

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"