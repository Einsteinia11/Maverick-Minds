'''This program will work as a virtual assistant of your pc and can perform all the general operations
It talks like human wih you and because of that it can become your good friend also. The impressing
thing about this is it shows you gifs while every talks with the user and thus it describes it's emotions
like this way. The one more intresting thing is that it is having both types of gifs for male and for female
that option can be set through manage account while creating your account.
'''
import os
import csv
import tkinter as tk
from tkinter import *
import PIL
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import count
import random

username = ""
Robo_name = ""

''' This is VRobot class which will automatically be called by e_check function inside another class named login_window
The VRobot class contains a constructor and 6 functions'''
class VRobot(tk.Frame): #Third Page
    count = 0
    s2 = ""
    give_R = False
    g = False
    textbox = False
    gif_type = "female"
    imer_var = True


    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        background_i = tk.PhotoImage(file=r"D:\zepeto\bg.png")
        background_l = tk.Label(root, image=background_i)
        background_l.place(relwidth=1, relheight=1)
        background_l.image = background_i
        root.frame = tk.Frame(root, bg='#80c1ff', bd=5)
        root.frame.place(relx=0.3333333333333333, rely=0.1, relwidth=0.63, relheight=0.1, anchor='n')
        root.entry = Entry(root.frame, font=40)
        root.entry.place(relwidth=0.63, relheight=1)
        root.entry.configure({"background": "Black", "foreground": "white"})
        root.button = tk.Button(root.frame, text="Send >>", font=40, command=root.word_split, fg="yellow",
                                bg="black")
        root.button.place(relx=0.7, relheight=1, relwidth=0.3)
        root.write_l = tk.Label(root, text="--Main BOX", bg="purple", fg="white", font=40)
        root.write_l.place(relx = 0.7, relwidth=0.1, relheight=0.1, rely=0)
        root.write_e = Entry(root, bg="Light Green", fg="blue", font=40)
        root.write_e.place(rely=0.1, relx=0.7, relheight=0.1, relwidth=0.2)
        root.send_button = Button(root, text="send >>", font=40, command=root.text_box, bg="gray", fg="pink")
        root.send_button.place(relx=0.9, rely=0.1, relheight=0.1, relwidth=0.1)
        root.clear_button = tk.Button(root, text="Clear_ALL", font=40, bg="pink", fg="red", command=root.clear_all)
        root.clear_button.place(relx=0.9, relheight=0.1, relwidth=0.1, rely=0)
        root.lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
        root.lower_frame.place(relx=0.3333333333333333, rely=0.25, relwidth=0.63, relheight=0.6, anchor='n')
        root.t = Listbox(root.lower_frame, background="blue", foreground="yellow", height=15, width=60,
                         font=("Helvetica", 12))
        root.h = Scrollbar(root.lower_frame, orient='horizontal')
        root.h.pack(side=BOTTOM, fill=X)
        root.v = Scrollbar(root.lower_frame, orient="vertical")
        root.v.pack(side=RIGHT, fill=Y)
        root.side_frame = tk.Frame(root, bg='pink', bd=10)
        root.side_frame.place(relx=0.91, rely=0.30, relwidth=0.40, relheight=0.5, anchor='n')
        root.t.pack(fill=BOTH)
        

    def clear_all(root):
        if root.g:
            root.K.destroy()
        if root.sent:
            root.t.delete(0, tk.END)

    def word_split(root):
        ignore_words = ["'", ",", "!", "?", "/", "{", "}", "(", ")", "*", "#", "&", "^", "@", "~", "`", "|", "<", ">"]
        s1 = ""
        if root.give_R:
            for i in root.s2:
                if i not in ignore_words:
                    s1 += i
            root.s2 = s1
            root.t.insert(END, root.s2)
            root.h.config(command=root.t.xview)
            root.v.config(command=root.t.yview)
            root.t.pack(side=LEFT, expand=True, fill=BOTH)
            root.h.config(command=root.t.xview)
            root.v.config(command=root.t.yview)
            root.t.pack(side=LEFT, expand=True, fill=BOTH)
            root.give_R = False
        else:
            root.sentence = root.entry.get()
            s = ''
            for j in root.sentence:
                if j not in ignore_words:
                    s += j
            root.sentence = s
            root.sent = True
            root.find_responses()
    
    def text_box(root):
        if root.textbox:
            if root.count == 6:
                text = root.write_e.get()
                root.t.insert(END, str(text))
                a = os.system('start {app}'.format(app=text))     
        root.textbox = False

    def give_responses(root):
        # Reading gender from the file
        dirName = "D:/VirtualAssistant"
        root.textbox = False
        root.give_R = True
        # Reading robo name from file
        tmp_file1 = "tmp_{username}.txt".format(username=username)
        print(tmp_file1)
        with open(os.path.join(dirName, tmp_file1), "r") as handler5:
            Robo_name = handler5.read()
        with open(os.path.join(dirName, tmp_file1), "r") as handler6:
            root.gif_type = handler6.read()
        if root.count == 1:
            root.r = [("Hello, My name is ", Robo_name, " and I am a virtual assistance of pc...!!!! would you please tell me"
                 " what I can do for you..???"), ("Hey there my name is ", Robo_name, " ..!!!\n How can I help you??")
                 , ("Oh Yea sure I am ", Robo_name, " a virtual assistance! How can you help you???")]
            root.s2 = (random.choice(root.r))
        elif root.count == 2:
            root.r = [("Hey ", username, ".....how are you??"), ("Hola hui ", username, " !, What's on your mind let's"
                 " explore...!!!"), "High five how's going..???", ("Hello ", username, "...!!!"), "Hey Hi so far to"
                 " see you How's going everything????"]
            root.s2 = (random.choice(root.r))
        elif root.count == 3:
            filename = "D:/VirtualAssistant/Tasks.csv"
            
            rowlist = [(a,b,c)]
            

            
        root.word_split()


    def find_responses(root):
        words = root.sentence.split()
        length = len(words)
        e = ""
        s1 = (">$You>>", root.sentence)
        root.t.insert(END, s1)
        root.sent = False
        root.main_word = ['name']
        for j in range(0, length):
            if words[j] in root.main_word:
                root.count = 1
                root.give_responses()
                root.sent = True
            if j == length and root.sent:
                words += [e]
        root.main_word = ['hi', "hello", "hey", "hola", "hui", "hoi"]
        for j in range(0, length):
            if words[j] in root.main_word:
                root.count = 2
                root.give_responses()
                root.sent = True
            if j == length and root.sent:
                words += [e]
        root.main_word = ["create", "Create"]
        for j in range(0, length):
            if words[j] in root.main_word:
                root.count = 3
                root.give_responses()
                root.sent = True
            if j == length and root.sent:
                words += [e]
        root.main_word = ["show", "Show"]
        for j in range(0, length):
            if words[j] in root.main_word:
                root.count = 4
                root.give_responses()
                root.sent = True
            if j == length and root.sent:
                words += [e]
        root.main_word = ["done", "finished", "completed"]
        for j in range(0, length):
            if words[j] in root.main_word:
                root.count = 5
                root.give_responses()
                root.sent = True
            if j == length and root.sent:
                words += [e]
        
        
class startup(tk.Tk):
    check = False
    
    def __init__(root, *args, **kwargs):  
        # __init__ function for class Tk 
        tk.Tk.__init__(root, *args, **kwargs) 
          
        # creating a container 
        root.title("ChatBot")
        root.geometry("1000x600+10+20")
        root.resizable(False, False)
        container = tk.Frame(root)
        container.pack(side = "top", fill = "both", expand = True)  
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1)
        root.frames = {}   
        for F in (login_window, Manage_account, VRobot):
            frame = F(container, root) 
            root.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew")
        root.show_frame(login_window)
          
    def show_frame(root, cont):
        frame = root.frames[cont] 
        frame.tkraise()


class login_window(tk.Frame): # First Page
    
    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        background_i = tk.PhotoImage(file=r'D:\zepeto\bg2.png')
        background_l = tk.Label(root, image=background_i)
        background_l.place(relwidth=1, relheight=1)
        background_l.image = background_i
        lbl5=Label(root,text="Login",relief="solid",font=("Times New Roman",18),width=10)
        lbl5.grid(row = 2, column = 1, padx = 10, pady = 10)
        lbl6=Label(root,text="Enter Username: ",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=25)
        lbl6.place(x=295,y=100)
        root.txt3=Entry(root,relief="solid",font=("Times New Roman",18),width=30, show="@")
        root.txt3.place(x=275,y=170)
        lbl7=Label(root,text="Enter Password: ",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=25)
        lbl7.place(x=295,y=220)
        root.txt4=Entry(root,relief="solid",font=("Times New Roman",18),width=30, show="$")
        root.txt4.place(x=275,y=290)
        btn2=Button(root,text="Create Account",relief="solid",fg="#B80F0A",font=("Times New Roman",18),width=15,command=lambda : controller.show_frame(Manage_account))
        btn2.place(x=350,y=370)
        btn3=Button(root,text="Verify!",relief="solid",fg="#B80F0A",font=("Times New Roman",18),width=15,command=root.e_check)
        btn3.place(x=350,y=500)       

    def e_check(root):
        global username
        u = root.txt3.get()
        username = u
        p = root.txt4.get()
        # Reading from csv file
        filename = "D:/VirtualAssistant/data.csv"
        handler = open(filename, "r", newline="")
        obj = csv.reader(handler)
        list1 = []
        for row in obj:
            length = len(row)
            for i in range(0, length):
                list1.append(row[i])
        length = len(list1)
        list1.remove("Username")
        list1.remove("Password")
        list1.remove("Gender")
        root.login = False
        root.login2 = False
        if length > 2:
            for i in range(1, length + 1, 3):
                try:
                    if int(p) == int(list1[i]):
                        root.login = True
                        break
                except:
                    if i == length +1:
                        break
        length = len(list1)
        for j in range(0, length, 3):
            if str(u) == str(list1[j]):
                root.login2 = True
                break
            if j == length:
                length += 1
            else:
                if i == length:
                    break
        if root.login and root.login2:
            messagebox.showinfo('Welcome', "Name and Password --VERIFIED")
            Manage_account.destroy(root)
            startup.destroy(root)
            root.destroy()
            a = ""
            try:
                username = u
                k = VRobot(startup, a)
            except:
                pass
        else:
            messagebox.showinfo('Error', "Wrong Password")
            root.destroy()
            exit()


class Manage_account(tk.Frame):# Second Page
      
    def __init__(root, parent, controller):
        tk.Frame.__init__(root, parent)
        background_i = tk.PhotoImage(file=r'D:\zepeto\bg.png')
        background_l = tk.Label(root, image=background_i)
        background_l.place(relwidth=1, relheight=1)
        background_l.image = background_i
        lbl=Label(root,text="Manage Account :)",relief="solid",font=("Times New Roman",18),width=10)
        lbl.place(relx=0, rely=0, relheight=0.1, relwidth=0.3)
        lbl2=Label(root,text="USERNAME: ",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=20)
        lbl2.place(x=295,y=150)
        root.txt5=Entry(root,relief="solid",font=("Times New Roman",18),width=30)
        root.txt5.place(x=275,y=220)
        lbl3=Label(root,text="Password: ",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=20)
        lbl3.place(x=295,y=300)
        root.txt2=Entry(root,relief="solid",font=("Times New Roman",18),width=30, show="*")
        root.txt2.place(x=275,y=370)
        btn=Button(root,text="ADD",relief="solid",fg="#B80F0A",font=("Times New Roman",18),width=15,command=root.create_file)
        btn.place(x=400,y=470)
        g_label=Label(root,text="Gender:",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=20)
        g_label.place(relx=0.8, rely=0.3, relheight=0.1, relwidth=0.2)
        root.g_entry=Entry(root,relief="solid",font=("Times New Roman",18),width=10)
        root.g_entry.place(relx=0.8, rely=0.4, relheight=0.1, relwidth=0.2)
        v_label=Label(root,text="Give your robo a name:",fg="#1134A6",font=("Times New Roman",18),relief="solid",width=20)
        v_label.place(relx=0.7, rely=0.6, relheight=0.1, relwidth=0.3)
        root.v_entry=Entry(root,relief="solid",font=("Times New Roman",18),width=10)
        root.v_entry.place(relx=0.8, rely=0.7, relheight=0.1, relwidth=0.2)
        back=Button(root,text="Back",relief="solid",font=("Times New Roman",18),width=10,command=lambda : controller.show_frame(login_window))
        back.place(x=850,y=15)

    def create_file(root):
        u = root.txt5.get()
        p = root.txt2.get()
        g = root.g_entry.get()
        n = root.v_entry.get()
        # Creating directory VirtualAssistant containing data.csv
        c = 0
        dirName = 'D:/VirtualAssistant'
        rowlist = [(u, p, g)]
        try:
            os.mkdir(dirName)
            filename = "D:/VirtualAssistant/data.csv"
            handler = open(filename, "a", newline="")
            l = [{"Username": u, "Password": p, "Gender": g}]
            fields = list(l[0].keys())
            obj = csv.DictWriter(handler, fieldnames=fields)
            obj.writeheader()
            obj.writerows(l)
        except FileExistsError:
            filename = "D:/VirtualAssistant/data.csv"
            handler = open(filename, "a", newline="")
            writer = csv.writer(handler)
            writer.writerows(rowlist)
        # Creating two different files at VirtualAssistant path containing robo name and user's gender
        try:
            name_file = 'tmp_{filename}.txt'.format(filename=u)
            with open(os.path.join(dirName, name_file), "a") as handler2:
                handler2.write(n)
                c+=1
            tmp_file = 'g_{filename}.txt'.format(filename=u)
            with open(os.path.join(dirName, tmp_file), "a") as handler3:
                handler3.write(g)
        except FileExistsError:
            tmp_file = 'g_{filename}{c}.txt'.format(filename=u, c=c)
            with open(os.path.join(dirName, tmp_file), "a") as handler3:
                handler3.write(g)
            name_file = 'tmp_{filename}{c}.txt'.format(filename=u, c=c)
            with open(os.path.join(dirName, name_file), "a") as handler2:
                handler2.write(n)
            c+=1
        messagebox.showinfo("Congratulations","Account created...!!!")

k = startup()
k.mainloop()
