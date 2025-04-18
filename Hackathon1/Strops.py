#getspan(s, ss), reverseWords(s), removePunctuation(s), countWords(s), charecterMap(s)
#makeTitle(s), normalizeSpaces(s), transform(s), getPermutations(s)

# program to find the span
def getAllSpans(s, value):
    spans = []
    start = 0
    while start < len(s):
        start = s.find(value, start)
        if start == -1:
            break
        spans.append((start, start + len(value)))
        start += 1
   
    print(len(spans),spans)
#-------------------------------------------------------

#Program to find the reverse of word  
def reverseWords(n):
    out = n[::-1]
    print(f'{n} is reversed as {out}')
#-------------------------------------------------------

#Program to find the removal of Punctuation from code
def removePunctuation(Word):
    remove_Punc=''
    s = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in Word:
        if i not in s:
            remove_Punc=remove_Punc+i
    #return remove_Punc
    print(f'The User Enterted:',Word)
    print(f'After removal of Punctuations:',remove_Punc)
#-------------------------------------------------------

#Program to find word count
def countWords(s):
    wo= s.split()
    l= len(wo)
    print(f" {s} having {l} length")
#-------------------------------------------------------

#Program to find charecterMap
def charecterMap(s):
    d= {}
    for x in s.lower():
        if x in d.keys():
            d[x] = d[x]+1
        else:
            d[x] = 1
    return d 
#-------------------------------------------------------

#Program to find makeTitle
def makeTitle(s):
    if (s.istitle()):
        print("The given string is already a title")
    em=[]
    g = s.split()
    em = [x.capitalize() for x in g]
    cap= ' '.join(em)
    #return cap
    print("The title is:",cap)
#-------------------------------------------------------

#Program to find normalizeSpaces
def normalizeSpaces(s):
    sen=[]
    f = False
    for x in s:
        if x != ' ':
            sen.append(x)
            f= False
        elif not f:
            sen.append(' ')
            f = True
    sentence = ''.join(sen)     
    print("Normalized sentence:",sentence)
#-------------------------------------------------------

#Program to find transform
def transform(string):
    f = string[::-1]
    g = f.swapcase()
    print("Transformed sentence is-> ")
    return g
#-------------------------------------------------------

#Program to find permutation
def get_permutations(s, step=0):
    if step == len(s):
        print("".join(s)) 
        return
 
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step], s_list[i] = s_list[i], s_list[step] 
        get_permutations(s_list, step + 1)


if __name__ == "__main__":

    s = 'mississippi'
    value = 'ss'
    print(getAllSpans(s, value))
#---------------------------------------------
    output = reverseWords('miss')
    print(output)
#---------------------------------------------
    s = removePunctuation("Hello!!#Hello$%@")
    print(s)
#---------------------------------------------
    r = countWords("Hello hello hello")
    print(r)
#---------------------------------------------
    y = charecterMap("Hello")
    print(y)
#---------------------------------------------
    z = normalizeSpaces("hello   hello   hi   ")
    print(z)
#---------------------------------------------
    f = makeTitle("jungle book")
    print(f)
#---------------------------------------------
    r = transform("Hello")
    print(r)
#---------------------------------------------   
    g = get_permutations("ijk")
    print(g)
