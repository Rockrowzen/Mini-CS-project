import json
from difflib import get_close_matches
data = json.load(open('dictionary_compact.json'))

word = str(input("Enter :")).lower()

possible = get_close_matches(word, data.keys(), n=5)

print(type(data))

#display words that begin with a certain string
def startletter(word):
    for i in data.keys():
        if i.startswith(word):
            print(i)

#display words of meaning
def wordsofmeaning(word):
    count=1
    for key,value in data.items():
        if word in value:
            if count<21:
                print(count,"-",key,end=" ")
            count+=1
    return("thank you")
        

#    return ("Word {} - Meaning {}".format(data,value))
#    else:
#        newword2 = input(f"Try these : {possible} :").lower()
#        return (wordsofmeaning(newword2))

#find meaning
def meaning(x):
    if x in data:
        return data[x]
    elif len(possible)>0:
        newword1 = input(f"Try these : {possible} :").lower()
        return (data[newword1])
    else:
        return "Word doesn't exist"

choice = int(input())
if choice==1:
    print(meaning(word))
elif choice==2:
    startletter(word)
elif choice==3:
    wordsofmeaning(word)
else:
    print("ïnvalid choice")

#loadscreen
#display words beginning with a certain letter
#find meaning of specific word
#display words of a certain meaning