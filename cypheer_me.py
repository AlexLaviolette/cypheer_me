###CIPHEER_ME###

import graphics
from graphics import *
import function
from function import *

###VARIABLES###

loop_1 = 1
loop_2 = 1
loop_3 = 1
flag = 0
flagged = 0
store_user1 = ""
store_password1 = ""
store_messfrom1 = ""
store_messtext1 = ""
loginsuccess = 0

###MAIN###

win = GraphWin("Cipher Code based on Lorenz Machine", 800, 600)

win.setBackground('Navajo White')

home = rectangle(280,443,520,510,'Peru',win)
homet = text(400,477,"START",30,'Cornsilk', win)

title = text(400,200,"CYPHEER_ME",36,'Firebrick', win)
title2 = text(400,270,"SEND, RECEIVE, and ENCRYPT MESSAGES.",20,'Saddle Brown', win)

while loop_1 == 1: #Program Loop
    move = win.getMouse()
    moveX = move.getX()
    moveY = move.getY()

    if moveX >= 280 and moveX <= 520 and moveY >= 443 and moveY <= 510: 
        title.undraw()
        title2.undraw()
        homet.undraw()
        home.undraw()

        while loop_2 == 1: #Log In/Sign up loop
            flagged = 0
            if flag == 11:
                flag = 0
                flagged = 1
                createaccount.undraw()
                user.undraw()
                entryuser.undraw()
                password.undraw()
                entrypassword.undraw()
                signrect.undraw()
                create.undraw()

            
            if flag == 0:
                flag = 1
                login = text(400,140,"LOGIN",30,'Firebrick', win)

                user = text(290,195,"Username:",18,'Saddle Brown', win)
                entryuser = entrys(450,195,20,win)

                password = text(290,255,"Password:",18,'Saddle Brown', win)
                entrypassword = entrys(450,255,20,win)

                signrect = rectangle(350,285,461,320,'Peru',win)
                signin = text(406,303,"SIGN IN",18,'Cornsilk', win)

                createrect = rectangle(300,398,500,530,'Peru',win)
                create = text(400,466,"CREATE AN\n ACCOUNT",25,'Cornsilk', win)


            move = win.getMouse()
            moveX = move.getX()
            moveY = move.getY()

            if flag == 10:
                unsuccess.undraw()
                flag = 1

            if flagged == 1:
                warn.undraw()
            
            ###LOG IN###
            if moveX >= 350 and moveX <= 461 and moveY >=275 and moveY <= 320:
                store_user = []
                store_pass = []
                textFileps = open(r"tuttepseu.txt","r")
                rlineps = textFileps.readlines()
                rline_len = len(rlineps)
                textFilepa = open(r"tuttepass.txt","r")
                rlinepa = textFilepa.readlines()
                userguess= entryuser.getText()
                passwordguess = entrypassword.getText()
                for i in range(rline_len):
                    rlineps_process = rlineps[i].split("\n")
                    rlinepa_process = rlinepa[i].split("\n")
                    store_user.append(rlineps_process[0])
                    store_pass.append(rlinepa_process[0])
                for i in range(rline_len):
                    if userguess == store_user[i] and passwordguess == store_pass[i]:
                        
                        userusing= store_user[i]
                        num = i

                        textFileps.close()
                        textFilepa.close()

                        login.undraw()
                        user.undraw()
                        entryuser.undraw()
                        password.undraw()
                        entrypassword.undraw()
                        signrect.undraw()
                        signin.undraw()
                        createrect.undraw()
                        create.undraw()

                        i = rline_len

                        sett = text(80,25,"Welcome, " + userusing,15, "Saddle Brown",win)

                        quitrect = rectangle(690,10,790,50,'Peru',win)
                        quitt = text(740,30,"QUIT",25,'Cornsilk', win)

                        mainrect = rectangle(690,60,790,100,'Peru',win)
                        main = text(740,80,"MAIN",25,'Cornsilk', win)



                        while loop_3 == 1: #Logged in Loop
                            loginsuccess = 1

                            if flag == 1:
                                flag = 2
                                
                                inboxrect = rectangle(231,156,571,227,'Peru',win)
                                inbox = text(401,192,"INBOX",25,'Cornsilk', win)

                                messagerect = rectangle(231,237,571,308,'Peru',win)
                                message = text(401,273,"SEND",25,'Cornsilk', win)

                                encryptrect = rectangle(231,318,571,389,'Peru',win)
                                encrypt = text(401,354,"ENCRYPT/DECRYPT",25,'Cornsilk', win)

                            

                            move = win.getMouse()
                            moveX = move.getX()
                            moveY = move.getY()

                            ###INBOX###
                            if moveX>= 231 and moveX <= 571 and moveY >= 156 and moveY <= 227:
                                if flag == 2:
                                    flag = 3
                                    
                                    inboxrect.undraw()
                                    inbox.undraw()
                                    messagerect.undraw()
                                    message.undraw()
                                    encryptrect.undraw()
                                    encrypt.undraw()
                                    inmess = text(250, 80,"Your Messages",25,"Firebrick",win)
                                    
                                    inloop = 0
                                while inloop == 0:
                                    textFillus = open(r"tuttemessfrom.txt","r")
                                    store_mess_user = textFillus.readlines()
                                    textFillme = open(r"tuttemesstext.txt","r")
                                    store_mess_mess = textFillme.readlines()
                                    textFillus.close()
                                    textFillme.close()
                                    
                                    if flag == 4:
                                        sentuser.undraw()
                                        sentmess.undraw()
                                        cross.undraw()
                                        flag = 3         
                                    
                                    store_mess_user_ = store_mess_user[num].split("\n")
                                    store_mess_user_ = store_mess_user_[0]
                                   
                                    store_mess_mess_ = store_mess_mess[num].split("\n")
                                    store_mess_mess_ = store_mess_mess_[0]
                                    
                                    store_mess_mess1 = store_mess_mess_.split(",")
                                    store_mess_user1 = store_mess_user_.split(",")
                                    store_messlen = len(store_mess_mess1)
                                    sendstringmess = ""
                                    sendstringuser = ""
                                    numcross = ""

                                    ###SHOW MESSAGE###
                                    
                                    if store_mess_user1[0] == "" and store_messlen == 1:
                                        print("")
                                    else:
                                        
                                        numcross = "X\n"
                                        for m in range(store_messlen):
                                            sendstringuser += store_mess_user1[m].upper() + "\n"
                                            sendstringmess += store_mess_mess1[m] + "\n"
                                    
                                    if flag == 3:
                                        flag = 4
                                        sentuser = text(125, 350,sendstringuser,18,"Indian Red",win)
                                        sentmess = text(425, 350,sendstringmess,18,"Saddle Brown",win)
                                        cross = text(700, 550,numcross,36,"Red",win)

                                    move = win.getMouse()
                                    moveX = move.getX()
                                    moveY = move.getY()
                                    ###DELETE MESSAGE###
                                    
                                    if moveX>= 690 and moveX <= 715 and moveY>=500 and moveY<=536:
                                        
                                        tempmess = ""
                                        tempuser = ""
                                        if store_messlen != 1:
                                            for b in range(store_messlen-2):
                                                tempmess += store_mess_mess1[b]+ ','
                                                tempuser += store_mess_user1[b]+ ','
                                            tempuser += store_mess_user1[store_messlen-2]
                                            tempmess += store_mess_mess1[store_messlen-2]
                                                                                       
                                        store_mess_mess[num] = tempmess + '\n'
                                        store_mess_user[num] = tempuser + '\n'
                                        a = 0

                                        tempuser = ""
                                        tempmess = ""
                                        
                                        for a in range(len(store_mess_mess)):
                                            
                                            tempuser += store_mess_user[a]
                                            tempmess += store_mess_mess[a]
                                        
                                        textFillus = open(r"tuttemessfrom.txt","w")
                                        textFillus.write(tempuser)
                                        textFillme = open(r"tuttemesstext.txt","w")
                                        
                                        textFillme.write(tempmess)
                                        textFillus.close()
                                        textFillme.close()
                                    ###MAIN###                                               
                                    if moveX>= 690 and moveX <= 790 and moveY >= 60 and moveY <= 100:
                                        
                                        sentuser.undraw()
                                        sentmess.undraw()
                                        inmess.undraw()
                                        cross.undraw()
                                        inloop = 1
                                        flag = 1
                                    ###QUIT###
                                    if moveX>= 690 and moveX <= 790 and moveY >= 10 and moveY <= 50:
                                        flag = 2
                                        sentuser.undraw()
                                        sentmess.undraw()
                                        inmess.undraw()
                                        cross.undraw()
                                        inloop = 1

                            ###SEND###
                            if moveX>= 231 and moveX <= 571 and moveY >= 237 and moveY <= 308:
                                if flag == 2:
                                    
                                    flag = 3
                                    
                                    inboxrect.undraw()
                                    inbox.undraw()
                                    messagerect.undraw()
                                    message.undraw()
                                    encryptrect.undraw()
                                    encrypt.undraw()

                                sendloop = 1
                                while sendloop == 1:
                                    
                                    textFillus = open(r"tuttemessfrom.txt","r")
                                    store_mess_user = textFillus.readlines()
                                    textFillme = open(r"tuttemesstext.txt","r")
                                    store_mess_mess = textFillme.readlines()
                                    textFillus.close()
                                    textFillme.close()

                                    textFillpseu = open(r"tuttepseu.txt","r")
                                    store_pseu = textFillpseu.readlines()
                                    textFillpseu.close()
                                    
                                    store_messlen = len(store_mess_mess)

                                    if flag == 3:
                                        flag = 4
                                        
                                        sentuser = text(150, 180,"To:",18,"Saddle Brown",win)
                                        sentmess = text(184, 230,"Message:",18,"Saddle Brown",win)
                                        entrysentuser = entrys(265,180,20,win)
                                        entrysentmess = entrys(335,230,20,win)
                                        sendingrect = rectangle(300,270,500,330,'Peru',win)
                                        sending = text(400,300,"SEND",25,'Cornsilk', win)
                                                                            
                                    move = win.getMouse()
                                    moveX = move.getX()
                                    moveY = move.getY()

                                    ###SENDING###
                                    if moveX>= 300 and moveX <= 500 and moveY >= 270 and moveY <= 330:

                                        for l in range(store_messlen):
                                            if store_pseu[l] == entrysentuser.getText() + "\n":
                                                
                                                store_mess_user_ = store_mess_user[l].split("\n")
                                                store_mess_mess_ = store_mess_mess[l].split("\n")
                                                
                                                if store_mess_mess_[0] != "":
                                                    store_mess_user[l] = store_mess_user_[0] +',' + userusing + "\n"
                                                    store_mess_mess[l] = store_mess_mess_[0] +',' + entrysentmess.getText() + "\n"
                                                else:
                                                    store_mess_user[l] = userusing + "\n"
                                                    store_mess_mess[l] = entrysentmess.getText() + "\n"
                                                tempuser = ""
                                                tempmess = ""
                                                for i in range(store_messlen):
                                                    tempuser += store_mess_user[i]
                                                    tempmess += store_mess_mess[i]

                                                textFille = open(r"tuttemessfrom.txt","w")
                                                textFille.write(tempuser)
                                                textFille.close()
                                                textFille = open(r"tuttemesstext.txt","w")
                                                textFille.write(tempmess)
                                                textFille.close()
                                                entrysentuser.undraw()
                                                entrysentmess.undraw()
                                                entrysentuser = entrys(265,180,20,win)
                                                entrysentmess = entrys(335,230,20,win)
                                                
                                    ###MAIN###                                               
                                    if moveX>= 690 and moveX <= 790 and moveY >= 60 and moveY <= 100:
                                        
                                        sentuser.undraw()
                                        sentmess.undraw()
                                        entrysentuser.undraw()
                                        entrysentmess.undraw()
                                        sendingrect.undraw()
                                        sending.undraw()
                                        sendloop = 0
                                        flag = 1
                                    ###QUIT###
                                    if moveX>= 690 and moveX <= 790 and moveY >= 10 and moveY <= 50:
                                        flag = 2
                                        sentuser.undraw()
                                        sentmess.undraw()
                                        entrysentuser.undraw()
                                        entrysentmess.undraw()
                                        sendingrect.undraw()
                                        sending.undraw()
                                        sendloop = 0
                                    
                            ###ENCRYPT###
                            if moveX>= 231 and moveX <= 571 and moveY >= 318 and moveY <= 389:
                                if flag == 2:
                                    flag = 3
                                    
                                    #sett.undraw()
                                    inboxrect.undraw()
                                    inbox.undraw()
                                    messagerect.undraw()
                                    message.undraw()
                                    encryptrect.undraw()
                                    encrypt.undraw()
                                    
                                encryptloop = 1
                                while encryptloop == 1:
                                    if flag == 3:
                                        flag = 4
                                        
                                        textencrypt = text(184, 230,"Text:",18,"Saddle Brown",win)
                                        
                                        entrytext = entrys(335,230,20,win)
                                        encryptingrect = rectangle(300,270,500,330,'Peru',win)
                                        encrypting = text(400,300,"ENCRYPT",25,'Cornsilk', win)        
    
                                    move = win.getMouse()
                                    moveX = move.getX()
                                    moveY = move.getY()

                                    if flagged == 2:
                                        flagged = 0
                                        encryptedtext.undraw()

                                    ###ENCRYPT###
                                    if moveX>= 300 and moveX <= 500 and moveY >= 270 and moveY <= 330:
                                        querry = entrytext.getText()
                                        final = "" 
                                        querry = querry.lower()
                                        lenQuerry = len(querry)

                                        cipher = ""
                                        letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                                        "q","r","s","t","u","v","w","z","y","z"]
                                        teleprinter1 = {"a":"XX...","b":"X..XX","c":".XXX.","d":
                                        "X..X.","e":"X....","f":"X.XX.","g":".X.XX","h":"..X.X","i":".XX..","j":"XX.X.",
                                        "k":"XXXX.","l":".X..X","m":"..XXX","n":"..XX.","o":"...XX","p":".XX.X","q":
                                        "XXX.X","r":".X.X.","s":"X.X..","t":"....X","u":"XXX..","v":".XXXX"
                                        ,"w":"XX..X","x":"X.XXX","y":"X.X.X","z":"X...X", " ":"XX.XX", ".":
                                        "..X..", ",":".X...","'":".....","*":"XXXXX",":":"...X."}
                                        teleprinter = {"XX...":"a","X..XX":"b",".XXX.":"c","X..X.":"d","X....":"e",
                                        "X.XX.":"f",".X.XX":"g","..X.X":"h",".XX..":"i","XX.X.":"j","XXXX."
                                        :"k",".X..X":"l","..XXX":"m","..XX.":"n","...XX":"o",".XX.X":"p"
                                        ,"XXX.X":"q",".X.X.":"r","X.X..":"s","....X":"t","XXX..":"u",
                                        ".XXXX":"v","XX..X":"w","X.XXX":"x","X.X.X":"y","X...X":"z",
                                        "XX.XX": " ","..X..":".",".X...":",",".....":"'","XXXXX":"*","...X.":":"}

                                        rand = 0
                                        #Alphabetical key   
                                        for i in range(lenQuerry):
                                            rand_l = letter[rand]  
                                            rand += 1
                                            key = teleprinter1[rand_l]
                                            alph = querry[i]
                                            code = teleprinter1[alph]
                                            cipher = ""

                                            for i in range(5):
                                                if code[i] == key[i]:
                                                    cipher = cipher + "."                        
                                                else:
                                                    cipher = cipher + "X"
                                                    
                                            letter_cipher = teleprinter[cipher]
                                            final = final + teleprinter[cipher]

                                        encryptedtext = text(400,350,final,13,'Green', win)
                                        
                                        flagged = 2
                                        entrytext.undraw()
                                        entrytext = entrys(335,230,20,win)
                                    
                                    ###MAIN###                                               
                                    if moveX>= 690 and moveX <= 790 and moveY >= 60 and moveY <= 100:
                                        textencrypt.undraw()
                                        entrytext.undraw()
                                        encryptingrect.undraw()
                                        encrypting.undraw()
                                        
                                        encryptloop = 0
                                        flag = 1
                                    ###QUIT###
                                    if moveX>= 690 and moveX <= 790 and moveY >= 10 and moveY <= 50:
                                        flag = 2
                                        textencrypt.undraw()
                                        entrytext.undraw()
                                        encryptingrect.undraw()
                                        encrypting.undraw()
                                        encryptloop = 0
                            ###QUIT###
                            if moveX>= 690 and moveX <= 790 and moveY >= 10 and moveY <= 50:
                                if flag == 2:
                                    flag == 3
                                    
                                    sett.undraw()
                                    inboxrect.undraw()
                                    inbox.undraw()
                                    messagerect.undraw()
                                    message.undraw()
                                    encryptrect.undraw()
                                    encrypt.undraw()
                                    quitrect.undraw()
                                    quitt.undraw()
                                    mainrect.undraw()
                                    main.undraw()
                                    loop_3 = 0
                                    loop_2 = 0
                                    loop_1 = 0
                                    win.close()
                            ###MAIN###
                            #if moveX>= 690 and moveX <= 790 and moveY >= 60 and moveY <= 100:
                                
                ###UNSUCCESFULL###
                if loginsuccess == 0: 
                    unsuccess = text(400,350,"Wrong Password or Username",13,'Red', win)
                    flag = 10

            ###SIGN UP###
            if moveX>= 300 and moveX <= 500 and moveY >= 398 and moveY <= 530:
                
                if flag == 1:
                    flag = 11
                    login.undraw()
                    signin.undraw()
                    createrect.undraw()
                    create.undraw()

                    createaccount = text(400,140,"Sign Up",30,'Firebrick', win)
                    create = text(406,303,"Create",18,'Cornsilk', win)
                signloop = 1
                while signloop == 1:    

                    move = win.getMouse()
                    moveX = move.getX()
                    moveY = move.getY()

                    if flagged == 1:
                        warn.undraw()
            
                    
                    if moveX >= 350 and moveX <= 461 and moveY >=275 and moveY <= 320:
                        user_ = entryuser.getText()
                        password_ = entrypassword.getText()
                        textFile1 = open(r"tuttepseu.txt","r")
                        store_user = textFile1.readlines()
                        textFile1.close()
                        textFile2 = open(r"tuttepass.txt","r")
                        store_password = textFile2.readlines()
                        textFile2.close()
                        textFile3 = open(r"tuttemessfrom.txt","r")
                        store_messfrom= textFile3.readlines()
                        textFile3.close()
                        textFile4 = open(r"tuttemesstext.txt","r")
                        store_messtext= textFile4.readlines()
                        textFile4.close()
                        store_user_len = len(store_user)

                        if user_ + "\n" in store_user:
                            warn = text(400,350,"This username already exist,\n please try again.",13,'Red', win)
                            flagged = 1
                        else:
                            warn = text(400,350,"Your account was succesfully created!",13,'Green', win)
                            
                            store_user.append(user_ + "\n")
                            store_password.append(password_+ "\n")
                            store_messfrom.append("\n")
                            store_messtext.append("\n")
                            for i in range (store_user_len + 1):
                                store_user1 = store_user1 + store_user[i]
                                store_password1 = store_password1 + store_password[i]
                                store_messfrom1 = store_messfrom1 + store_messfrom[i]
                                store_messtext1 =store_messtext1 + store_messtext[i]
                            textFile1 = open(r"tuttepseu.txt","w")
                            textFile1.write(store_user1)
                            textFile1.close()
                            textFile2 = open(r"tuttepass.txt","w")
                            textFile2.write(store_password1)
                            textFile2.close()
                            textFile3 = open(r"tuttemessfrom.txt","w")
                            textFile3.write(store_messfrom1)
                            textFile3.close()
                            textFile4 = open(r"tuttemesstext.txt","w")
                            textFile4.write(store_messtext1)
                            textFile4.close()
                            signloop = 0
                            flag = 11

                    
