import random
import string

def get_random_letters(n=3):
    return "".join(random.choices(string.ascii_letters,k=n))

def encode (word):
    if len(word)>3:
        first=word[0]
        core = word[1:]+first
        prefix = get_random_letters()
        suffix = get_random_letters()
        return prefix + core + suffix
    else:
        return word[::-1] # used to reverse the word
    
def decode(code):
    if len(code)<3:
        return code[::-1]
    else:
        core = code[3:-3]#ignoreing first 3 AND Last 3 letters
        last = core [-1]
        rest = core [:-1]# exepect -1 take the remaning letters
        return last + rest 
    
original = "Vinay"
enco  = encode(original)
deco = decode(enco)
print("original",original)
print("encode",enco)
print("decoded",deco)


