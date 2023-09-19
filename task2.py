#!python3
'''
##### Task 2
Take a string and make sure that it is a proper sentence, with only the first letter capitalized and the rest of the sentence in lower case. We will assume that the sentence never includes names that require capitalization.
(2 points)
'''

def properCaps(input):
    '''
    parameters:
    str input - string to fix capitalization for
    
    return
    str - proper capitalized string
    '''
    return


if __name__ == "__main__":
    sentence = "Carry On My Wayward Son!"
    assert properCaps(sentence) == "Carry on my wayward son!"

    sentence = "I'm JuSt A LiTtle Black RainCLOUD!"
    assert properCaps(sentence) == "I'm just a little black raincloud!"