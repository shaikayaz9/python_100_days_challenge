#wap to translate a message into secrat code langauge, use the rules below to translate normal message into secret code language.

#codeing
# 1 if the word containers atleast 3 Charecter , remove the frist letter & append it at the end
# now append three charecter at the string and the end 
# else simple reverse the string
import random
word = input("Enter your Code : ")
a = random.randint(0,len(word)) 
b = ["*" , "%" , "#","_","^", "@"]
print(a)
r = b[a]

if(len(word) > 4):
    c = word[-1]
    word = word +c
    word = word + "$"
    print(r +word +b[4])
else:
   word = word.index[0]
   print(word)




# word = input("Enter your secrat code.. : ")
# if(len(word) >3 and len(word) <5):
#     a = word.lower()
#     b = a.replace("a","*")
#     print(b+"h")
# elif(len(word)>6):
#     word = word.upper()
#     words = word[0] = "_"
#     print(word.upper())
# else:
#     word = word.lower()


# # print(s)
# # print(b)