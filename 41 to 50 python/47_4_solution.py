#solution of exercise 4

st = input("Enter your code : ")

# word = "ayaz is learning python"
words = st.split(" ")

coding = input("Coding = 1 , decoding = 0 :")
coding = True if(coding == "1") else False
if(coding):
    nword = []
    for word in words:
     if(len(word)>=3):
        r1 = "dsk"
        r2 = "jrk"
        stnew = r1 + word[1:] + word[0] +r2
        print(stnew)
        nword.append(stnew)
        print(nword)
    else:
       nword.append(word[::-1])

else:
   nword = []
   for word in words:
    if(len(word)>=3):
        stnew =  word[3:-3]
        stnew = stnew[-1] + stnew[:-1]
        print(stnew)
        nword.append(stnew)
        print(nword)