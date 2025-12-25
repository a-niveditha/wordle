#this progra handles UI using TKINTER

from tkinter import *
import class02 #handle SQLDB
import class03 #handle Files

#create root window
root = Tk()

#root.title("hello workld - wordle")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.state("zoomed")

# GEOMETRY SIZE  - HORIZ * VERTICAL IN PIXEL
#root.geometry('800x600')
#function to show a frame
def show_frame(frame):
    frame.tkraise()

#Sign in page
frame1 = Frame(root  ,bg='black')
frame1.grid(row=0,column=0,sticky="nsew")
frame1.tkraise()

frame1_title=Label(frame1,text="Sign In Page" ,fg="#7fd3eb",bg='black',font='georgia 32 bold')
#frame1_title.pack(fill="x")
frame1_title.place(x=500,y=50)

#Existing user sign in line1,line2, line3, line4
frame1_line1 = Label(frame1, text="Existing user-Sign in",bg='black',fg='#7fd3eb' , font='georgia 20 bold')
frame1_line1.place(x=200,y=100)
frame1_line2 = Label(frame1,text="Enter user name : ",bg='black',fg='#cb63e6' ,font='georgia 16')
frame1_line2.place(x=100,y=150)
frame1_line2_username = Entry(frame1,width=30)
frame1_line2_username.place(x=300,y=160)
frame1_line3 = Label(frame1,text="Enter password :",bg='black',fg='#cb63e6',font='georgia 16 ')
frame1_line3.place(x=100,y=190)
frame1_line3_userpwd = Entry(frame1,width=30)
frame1_line3_userpwd.place(x=300,y=200)

#error login message
frame1_line4 = Label(frame1)
frame1_line4.place(x=200,y=250)
frame1_line4.configure(bg='black',fg='black')

frame1_btn1=Button(frame1,text="Login to play wordle",bg="#fcd9c0",fg="#de3507", font='georgia 16')
frame1_btn1.place(x=550,y=160)

#login method
def login(frame2):
    username = frame1_line2_username.get()
    userpwd = frame1_line3_userpwd.get()
    res = class02.sign_in(username,userpwd)
    if res:
        frame1_line4.configure(text="",bg='black',fg='black')
        frame2.tkraise()
    else:
        frame1_line4.configure(text="Invalid login credentials",bg='black',fg='#fa7e55' ,font='georgia 16 bold')

frame1_btn1.configure(command=lambda:login(frame2))


frame1_btn3=Button(frame1,text="Instructions to play wordle",bg="#D2A26C",fg="black", font='georgia 16')
frame1_btn3.place(x=500,y=530)


#New User line5,line6, line7, line8, line9
frame1_line5= Label(frame1, text="New User - Register ",bg='black',fg='#7fd3eb' , font='georgia 20 bold')
frame1_line5.place(x=200,y=300)
frame1_line6 = Label(frame1,text="Enter user name : ",bg="black",fg="#cb63e6", font='georgia 16')
frame1_line6.place(x=100,y=350)
frame1_line6_username = Entry(frame1,width=30)
frame1_line6_username.place(x=300,y=360)
frame1_line7 = Label(frame1,text="Enter password :",bg="black",fg="#cb63e6", font='georgia 16')
frame1_line7.place(x=100,y=390)
frame1_line7_userpwd = Entry(frame1,width=30)
frame1_line7_userpwd.place(x=300,y=390)
frame1_line8 = Label(frame1,text="Confirm password :",bg="black",fg="#cb63e6", font='georgia 16')
frame1_line8.place(x=100,y=430)
frame1_line8_userpwd_cnf = Entry(frame1,width=30)
frame1_line8_userpwd_cnf.place(x=300,y=440)

#error login message
frame1_line9 = Label(frame1)
frame1_line9.place(x=200,y=490)
frame1_line9.configure(bg='black',fg='black')

#login method
def new_user(frame2):
    username = frame1_line6_username.get()
    userpwd = frame1_line7_userpwd.get()
    userpwd_cnf = frame1_line8_userpwd_cnf.get()
    if userpwd == userpwd_cnf:
        pass
    else:
        frame1_line9.configure(text="Password and Confirm password are not matching",bg='black',fg='#fa7e55',font='georgia 16 bold')
        return
    res = class02.add_user(username,userpwd)
    if res:
        frame1_line8.configure(text="",bg='black' ,fg='black')
        frame2.tkraise()
    else:
        frame1_line8.        configure(text="Invalid login credentials",bg='grey',fg='red')

frame1_btn2=Button(frame1,text="Register to play wordle",bg="#fcd9c0",fg="#de3507",font='georgia 16 ')
frame1_btn2.place(x=550,y=390)
frame1_btn2.configure(command=lambda:new_user(frame2))

frame1_btn4=Button(frame1,text="Exit",bg="#D2A26C",fg="black",font='georgia 16 ')
frame1_btn4.place(x=350,y=530)


frame2=Frame(root, bg='black')
frame2.grid(row=0,column=0,sticky="nsew")
frame2_title=Label(frame2,text=" WORDLE",bg="black" ,fg='#4ad0e8', font='georgia 36 bold')
frame2_title.place(x=460,y=10)

attempt=0
GREEN  = "#007d21"
YELLOW = "#e2e600"
BLACK  = "#000000"
WHITE  = "#f5e4df"
GREY  = "#505050"
LGREY = "#808080"

r1=0
# title
#label_1=Label(root,text="Welcome to WORDLE")
#label_1.place(x=300,y=5)

r1 += 1
# take input
choice1 = Label(frame2,text = "Guess the word [5 letters] : ",bg='black',fg='#4ad0e8',font='georgia 14')
choice1.place(x=5,y=75)
input1 = Entry(frame2, width=20)
input1.place(x=250,y=85)
btn1 = Button(frame2,text="Submit",bg='#fcd9c0',fg='#de3507',font='georgia 14')
btn1.place(x=425,y=75)
btn2=Button(frame2,text="Return to main page",bg='#fcd9c0',fg='#de3507',font='georgia 14')
btn2.configure(command=lambda:show_frame(frame1))
btn2.place(x=525,y=75)

r1 += 1
# display output
selected = class03.get_words().upper()

#msg1 = Label(frame2,text = selected)
#msg1.place(x=5,y=480)
msg2 = Label(frame2)
msg2.place(x=300,y=460)
msg2.configure(bg='black',fg='black')

#set x,y to display each attempt
x1 = 50
y1 = 100

#set x,y for displaying keyboiard
x2 = 200
y2 = 500
dict_keys={}

def dispKB():
    global x2, y2, dict_keys

    #line 1 Q W E R T Y U I O P
    for ch in "QWERTYUIOP":
        label_1 = Label(frame2, text = ch)
        label_1.configure(bg=WHITE, fg = BLACK)
        label_1.place(height=50, width=50,x=x2,y=y2)
        dict_keys[ch] = (label_1,"WHITE")
        x2 += 52
    # 2nd line
    x2 = 225
    y2 = 552
    for ch in "ASDFGHJKL":
        label_1 = Label(frame2, text=ch)
        label_1.configure(bg=WHITE, fg=BLACK)
        label_1.place(height=50, width=50, x=x2, y=y2)
        dict_keys[ch] = (label_1, "WHITE")
        x2 += 52
    #3rd line
    x2 = 275
    y2 = 604
    for ch in "ZXCVBNM":
        label_1 = Label(frame2,text=ch)
        label_1.configure(bg=WHITE, fg =BLACK)
        label_1.place(x=x2,y=y2,height=50,width=50)
        dict_keys[ch] = (label_1, "WHITE")
        x2 += 52

    return





def getGuess():
    global attempt, x1, y1, dict_keys
    
    inputword = input1.get().upper()
    print("get guess ", inputword)
    if len(inputword) != 5:
        msg2.configure(text="Please enter word of 5 characters",fg='#4ad0e8',font='georgia 16 bold')
        return

    if class03.check_words(inputword):
        pass
    else:
        msg2.configure(text="Invalid word, please enter a valid word",fg='#4ad0e8',font='georgia 16 bold' )
        return

    attempt += 1
    print("attempt ", attempt)
    y1 += 52
    msg2.configure(text='',fg=BLACK,bg=BLACK)
    x1=50

    for i, letter in enumerate(inputword):
        x1 += 52
        label = Label(frame2,text=letter)
        label.place(height=50,width=50,x=x1,y=y1)
        if letter == selected[i]:   #if inputword[i] == selected[i]
            label.config(bg=GREEN, fg=YELLOW, font='georgia 10')
            (l1, c1) = dict_keys.get(letter)
            l1.configure(bg=GREEN,fg=YELLOW,font='georgia 10')
            dict_keys[letter] = (l1, "GREEN")

        if letter in selected and not letter == selected[i]:
            label.config(bg=YELLOW, fg = BLACK,font='georgia 10')
            (l1, c1) = dict_keys.get(letter)
            if c1 == "GREEN":
                pass
            else:
                l1.configure(bg=YELLOW,fg=BLACK)
                dict_keys[letter]=(l1,"YELLOW")

        if letter not in selected:
            label.config(bg=GREY,fg=WHITE,font='georgia 10')
            (l1,c1) = dict_keys.get(letter)
            l1.configure(bg=GREY,fg=WHITE)
            dict_keys[letter] = (l1, "BLACK")
                
            
    if inputword == selected:
            msg2.configure(text="Congrats, you have guessed it correct!!!",fg='#4ad0e8',font='georgia 16 bold')
            return

    if attempt >=5:
        msg2.configure(text=f"Maximum attempts used, selected word is {selected}",fg='red',font='georgia 16')
        btn1.configure(state=DISABLED)
        return
    
    
    
btn1.configure(command=getGuess)

#Frame3 instructions page
frame3=Frame(root, bg='black')
frame3.grid(row=0,column=0,sticky="nsew")
frame3_title=Label(frame3,text=" INSTRUCTIONS TO PLAY WORDLE",bg="black" ,fg='#4ad0e8', font='georgia 36 bold')
frame3_title.place(x=150,y=10)
frame1_btn3.configure(command=lambda:new_user(frame3))

#Instruction Lines
frame3_line1= Label(frame3, text="1. You have five tries to guess the word correctly ",bg='black',fg='#7fd3eb' , font='georgia 16')
frame3_line1.place(x=100,y=100)
frame3_line2= Label(frame3, text="2. If you guess the exact position of a letter in the word it will turn GREEN",bg='black',fg='#7fd3eb' , font='georgia 16')
frame3_line2.place(x=100,y=150)
frame3_line3= Label(frame3, text="3. If you guess a letter that exists in the word of the day, but it is in the wrong position it turns YELLOW",bg='black',fg='#7fd3eb' , font='georgia 16')
frame3_line3.place(x=100,y=200)
frame3_line4= Label(frame3, text="4. If the letter does not exist, it turns GREY. ",bg='black',fg='#7fd3eb' , font='georgia 16')
frame3_line4.place(x=100,y=250)
frame3_line5= Label(frame3, text="5. Good luck!! ",bg='black',fg='#7fd3eb' , font='georgia 16 ')
frame3_line5.place(x=100,y=300)

frame3_btn1=Button(frame3,text="Return to main page",bg='#fcd9c0',fg='#de3507',font='georgia 18')
frame3_btn1.configure(command=lambda:show_frame(frame1))
frame3_btn1.place(x=500,y=450)

#Frame4 Credits Page
frame4=Frame(root, bg='black')
frame4.grid(row=0,column=0,sticky="nsew")
frame4_title=Label(frame4,text=" CREDITS",bg="black" ,fg='#4ad0e8', font='georgia 36 bold')
frame4_title.place(x=150,y=10)

#Credits 
frame4_line1= Label(frame4, text="1. Niveditha A",bg='black',fg='#7fd3eb' , font='georgia 16')
frame4_line1.place(x=100,y=100)
frame4_line2= Label(frame4, text="2. J Shaffin Navroz",bg='black',fg='#7fd3eb' , font='georgia 16')
frame4_line2.place(x=100,y=150)
frame4_line3= Label(frame4, text="3. M Charulatha",bg='black',fg='#7fd3eb' , font='georgia 16')
frame4_line3.place(x=100,y=200)

frame1_btn4.configure(command=lambda:new_user(frame4))

frame1.tkraise()
dispKB()

#execute tkinter
root.mainloop()
