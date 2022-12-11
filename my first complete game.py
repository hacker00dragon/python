name = input("enter ur name: ")
sis = input("enter your brother or sister name: ")
print("hello " +name+ " welcome to my game," +"\n the idea of the game is that you have 2 choices and you will choose 1 of them" + "\n the story will continue depends on your choices")
print("if you want to play type yes if you dont want to play type no")
choose = input("yes or no: ")
yes = "yes"
no = "no"

if choose == yes:
    print("here we go.")
    print("One day you was bored, you said let me sit in my room for a while when you entered you found " + sis +" sitting and looking" " \n provocative I said let me hit him a little bit but you said should i hit him with what with the pillow or the shoe")
    choose2 = input("pillow or shoe: ")
    yes2 = "pillow"
    no2 = "shoe"

    if choose2 == yes2:
                       print("you grapped the pillow and throw it on him, Suddenly you start hearing some noise" +"\n a man called mr.fomton enter ur room and ask you to go with him to a Secret mission. ")

    if choose2 == no2:
                      print("you grapped the shoe and throw it on him, Suddenly you start hearing some noise" +"\n a man called mr.fomton enter ur room and ask you to go with him to a Secret mission. ")
    choose3 = input("do you want to go with him?: ")
    yes3 = yes
    no3 = no

    if choose3 == yes3:
                       print("you: okay but "+ sis +" will come with me." + "\nMr.fomton: okay no problem lets go to my car." + "\nyou: Mr.fomton where is your car. " + "Mr.fomton i was joking i dont have one" + "\n Suddenly a man Notice mr.fomton real identity")


    else:
        print("Mr.fomton: why you say no" + "\nyou: are you stupid mr.fomton no means no" +"\n Mr.fomton: okay goodbye")
       
    choose4 = input("act as died or Distract him or hide :")
    yes4 = "act as died"
    no4 =  "Distract him"
    lol = "hide"
    
    if choose4 == yes4:
        print ("the man notice you are acting. you lose")
    elif choose4 == no4:
        print("Mr.fomton  someone to distrat him, at the same time a thief with a gun as you to give him all your money")
        choose5=input("reply at him, run, give hime money:")
        yes5= "reply at him"
        no5= "run"
        lol2= "give hime money"
        if choose5 == yes5:
            print("you make fun of the thief and refused to give him money so he kill you with his gun" + "\n you lose!")

        elif choose5 == no5:
            print("you ask the thief do discuss an idea with mr. fomton and " +sis+ " do say you will run but the thieve hear you and he killed you with his gun" + "\n you lose!")

        else:
            print("you was going to give him money but you notice you dont have the theif pity on you and give u some money and he let you go " + " Mr. fomton take you to his boss but the problem was the boss was your mother and she ask you to but a bread from the supermarket " + "\n congradulations you won! but dont forget to respect your parents")

    else:
        print("you and "+ " sis "+ " Mr.fomton hide in a supermarket but the owner ask you to buy or he will call the police")
        choose6= input("buy or no: ")
        yes6="buy"
        no6 ="no"
        if choose6 == yes6:
            print("you say somthing not funny and you got kicked from the supermark" + "\n but the man finally got tired from searching and you finally went with Mr.fomton to his boss " + "the boss said to you to bring him a tv remote so you start pucnhing him" +"\n but the problem was that the boss was your father and yow will get kicked from his family " + " but you apologize alot and he forgive you " + "\n congradulatins you win! but dont forget to respect your parents" )
        else:
            print("the police put you in the jail, you lose!")


else:
    print("goodbye stupid!")




