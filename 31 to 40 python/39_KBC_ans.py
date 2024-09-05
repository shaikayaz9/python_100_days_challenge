Questions = [ ["which langauge was used to craete facebook ?", "python", "PHP", "java", "english", 2],
             ["facebook CEO name ?", "elon", "mark", "jack", "ambani", 2],
             ["which langauge was used to craete facebook ?", "python", "PHP", "java", "english", 2],
             ["which langauge was used to craete facebook ?", "python", "PHP", "java", "english", 2],
             ["which langauge was used to craete facebook ?", "python", "PHP", "java", "english", 2]]

level = [1000,2000,3000,5000, 10000 , 20000 ,40000 , 80000 , 160000, 320000 , 640000 , 1280000 ,]
money = 0
for i in range(0, len(Questions)):
     Question = Questions[i]
     print(f"Question for RS. {level[i]}")
     print(f" a.{Question[1]}            b.{Question[2]}")
     print(f" c.{Question[3]}            d.{Question[4]}")
     reply = int(input("Enter your Answer (1-4): "))
     if(reply == Question[-1]):
        print(f"Currect answer,you have won RS. {level[i]}")
        if(i == 4):
            money = 10000
        elif(i ==9):
            money = 320000
     else:
        print(f"Wrong answer")
        break


print(f"your take monay is {money}")