import time 

rules='''\n\n\n........π π π π π  welcome to the python quiz  π π π π π.................\n

#Rulesβ¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ   β¬οΈ\n
1.πΆ   you have to give answer in small letters.
2.πΆ   don't use space at the end of the answer.
3.πΆ   use space between each word.
4.πΆ   if option are given in any question so you have to write correct option as it is as given.
5.πΆ   if you want to quit the game , simply write "QUIT" in capital letters.\n\n
 ----------πππππ Do you want to play this game?????πππππ--------------
                            yes..or..no
'''
for char in rules:
    print(char,end="")
    time.sleep(0.03)

playing = input("\n ANS = ")
score=0
minus=0

if playing!="yes":
    var1 = ' π π π...ok !!!  try next time... π π π'
    for char in var1:
        print(char,end="")
        time.sleep(0.03)
    quit()
else :
    var2='''\n\nπ€  π€  π€ ok!!!...let's play it ...π€  π€  π€ \n
         π₯π₯π₯ C O M E   F A S T π₯π₯π₯\n\n'''
    for char in var2:
        print(char,end="")
        time.sleep(0.04)

message='''
                        --------------------------------------
                            ------------------------------ 
                                -----------------------  
                                   G A M E   O V E R 
                                -----------------------   
                            -----------------------------  
                        ---------------------------------------    
  '''    

var3=''' Q.1οΈβ£    who invented python language??\n ANS = '''
for char in var3:
        print(char,end="")
        time.sleep(0.04)
answer= input()
if answer=="QUIT":
    print("you give correct answer of ",score, "questions....π₯³π₯³π₯³π₯³π₯³\n")
    print("you give wrong  answer of " ,minus,  "questions...πππππ\n\n")
    for char in message:
        print(char,end="")
        time.sleep(0.0000001)
    quit()

elif answer=="guido van rossum":
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1

var4=''' Q.2οΈβ£    in which year python was officially released??\n ANS = '''
for char in var4:
        print(char,end="")
        time.sleep(0.04)
answer= input()
if answer=="QUIT":
        percent=(score/1)*100

        m= f'''   you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
    you give wrong  answer of {minus} questions...πππππ\n
π₯π₯π₯π₯π₯your perfomance is {percent} % right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} % wrongπππππ\n\n'''

        for char in m:
                 print(char,end="")
                 time.sleep(0.04)

        for char in message:
          print(char,end="")
          time.sleep(0.0000001)
        quit()

elif answer==str(1991):
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1

var5=''' Q.3οΈβ£    what is full form of REPL ??\n ANS = '''
for char in var5:
        print(char,end="")
        time.sleep(0.04)
answer= input()

if answer=="QUIT":
        percent=(score/2)*100

        m= f'''   you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
    you give wrong  answer of {minus} questions...πππππ\n
π₯π₯π₯π₯π₯your perfomance is {percent} % right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} % wrongπππππ\n\n'''

        for char in m:
                 print(char,end="")
                 time.sleep(0.04)

        for char in message:
            print(char,end="")
            time.sleep(0.0000001)
        quit()

elif answer=="read evaluate print loop":
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1

var6=''' Q.4οΈβ£    is python case sensitive ??\n ANS = '''
for char in var6:
        print(char,end="")
        time.sleep(0.04)
answer= input()

if answer=="QUIT":
        percent=(score/3)*100

        m= f'''   you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
    you give wrong  answer of {minus} questions...πππππ\n
π₯π₯π₯π₯π₯your perfomance is {percent} % right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} % wrongπππππ\n\n'''

        for char in m:
                 print(char,end="")
                 time.sleep(0.04)


        for char in message:
          print(char,end="")
          time.sleep(0.0000001)

        quit()

elif answer=="yes":
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1

var7=''' Q.5οΈβ£      Which operator has higher precedence in the following list..

       % (Modulus)
       & (BitWise AND)
       **(Exponent)
       >(Comparison)\n ANS = '''
for char in var7:
        print(char,end="")
        time.sleep(0.04)
answer= input()

if answer=="QUIT":
        percent=(score/4)*100

        m= f'''   you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
    you give wrong  answer of {minus} questions...πππππ\n
π₯π₯π₯π₯π₯your perfomance is {percent} % right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} % wrongπππππ\n\n'''

        for char in m:
                 print(char,end="")
                 time.sleep(0.04)
        for char in message:
             print(char,end="")
             time.sleep(0.0000001)
        quit()

elif answer=="**(Exponent)":
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1

var8='''  Q.6οΈβ£      What is the output of the following code?
                #TIP=**PLEASE DON'T FOLLOW THE RULE NO. 1** 

        var = "ANil" * 2  * 3
        print(var) \n ANS = '''
for char in var8:
        print(char,end="")
        time.sleep(0.04)
answer= input()

if answer=="QUIT":
        percent=(score/5)*100

        m= f'''   you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
    you give wrong  answer of {minus} questions...πππππ\n
π₯π₯π₯π₯π₯your perfomance is {percent} % right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} % wrongπππππ\n\n'''

        for char in m:
                 print(char,end="")
                 time.sleep(0.04)
    

    
        for char in message:
               print(char,end="")
               time.sleep(0.0000001)
        quit()

elif answer=="ANilANilANilANilANilANil":
    print("\n correct!!!!π π π\n")
    score=score+1
else:
    print("\n incorrect!!...π­ π­ π­\n")
    minus=minus+1


percent=(score/6)*100

m=f'''you give correct answer of {score} questions....π₯³π₯³π₯³π₯³π₯³\n
you give wrong  answer of {minus} questions...πππππ\n"
π₯π₯π₯π₯π₯your perfomance is {percent} %  right...π₯π₯π₯π₯π₯\n
πππππyour perfomance is {100-percent} %  wrongπππππ\n\n'''

for char in m:
        print(char,end="")
        time.sleep(0.04)

for char in message:
        print(char,end="")
        time.sleep(0.0000001)
