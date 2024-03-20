from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Database

#---config windows 
windows = Tk()
windows.title("Auditoria System")
windows.geometry("800x600")
windows.configure(background="white")
windows.resizable(width=False, height=False)
windows.iconbitmap(default="imagens/LogoIcon.ico")
#----------#
#-----Image
logo = PhotoImage(file="imagens/logo.png")
#--widgets
LeftFrame = Frame(windows, width=350, height=600, bg="midnightblue",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(windows, width=450, height=600, bg="lightgrey",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="midnightblue")
LogoLabel.place(x=80,y=100)

#VarietysGlobals
EmailLabel = Label(RightFrame, text="E-mail", font=("Arial", 20), bg="lightgrey",fg="black")
EmailEntry = ttk.Entry(RightFrame, width= 30)
UserEntry = ttk.Entry(RightFrame, width= 30)
UserLabel = Label(RightFrame, text="Username", font=("Arial", 20), bg="lightgrey",fg="black")
PasswordLabel = Label(RightFrame, text="Password", font=("Arial", 20), bg="lightgrey",fg="black")
PasswordEntry = ttk.Entry(RightFrame, width= 30, show ="*")
NameLabel= Label(RightFrame, text="Name", font=("Arial", 20), bg="lightgrey",fg="black")
NameEntry = ttk.Entry(RightFrame, width= 30)

#--functions

def Register():
    global LoginButton,UserLabel,UserEntry, PasswordLabel,PasswordEntry, NameEntry, NameLabel

    LoginButton.place(x=8000)
    NameLabel.place(x=80,y=10)
    NameEntry.place(x=80,y=50)
    UserLabel.place(x=80,y=80)
    UserEntry.place(x=80,y=120)
    PasswordLabel.place(x=80,y=145)
    PasswordEntry.place(x=80,y=185)
    EmailLabel.place(x=80,y=210)
    EmailEntry.place(x=80,y=250)
    print("Registrado")
    RegisterButton = ttk.Button(RightFrame, text="Register",width=30, command=RegisterToDataBase)
    RegisterButton.place(x=80,y=300)
    BackButton = ttk.Button(RightFrame, text="Back",width=30, command=Back)
    BackButton.place(x=80,y=350)

def Back():
    NameEntry.place(x=8000,y=2000)
    NameLabel.place(x=8000,y=2000)
    UserLabel.place(x=80,y=100)
    UserEntry.place(x=80,y=150)
    EmailLabel.place(x=8000,y=2000)
    PasswordLabel.place(x=80,y=200)
    PasswordEntry.place(x=80,y=250)
    
    UserEntry
    PasswordEntry.clipboard_clear()
    #-----Button
    LoginButton = ttk.Button(RightFrame, text="Login",width=30 )
    LoginButton.place(x=80,y=300)

    RegisterButton = ttk.Button(RightFrame, text="Register",width=30, command=Register)
    RegisterButton.place(x=80,y=350)

def RegisterToDataBase():
    Name = NameEntry.get()
    Username = UserEntry.get()
    Password = PasswordEntry.get()
    Email = EmailEntry.get()
    
    if Name == '':
        messagebox.showerror(title='Register Error',message='Please fill in the name field.')
    elif Email == '':
        messagebox.showerror(title='Register Error',message='Please fill in the email field.')
    elif Username == '':
        messagebox.showerror(title='Register Error',message='Please fill in the username field.')
    elif Password == '':
        messagebox.showerror(title='Register Error',message='Please fill in the password field.')
    else:
        Database.cursor.execute("""
        INSERT INTO Users(NAME, EMAIL, USER, PASSWORD)VALUES (?, ?, ?, ?)
        ;
        """, (Name, Email, Username, Password))
        Database.conn.commit()
        messagebox.showinfo(title="Register info", message="Register sucessfull!")

def Login():
    Username = UserEntry.get()
    Password = PasswordEntry.get()
    Database.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (Username, Password))
    VerifyLogin = Database.cursor.fetchone()
    try: 
        if Username in VerifyLogin and Password in VerifyLogin:
            messagebox.showinfo(title="Login Info", message="Welcome! Access acept")
    except:
        messagebox.showinfo(title="Login info", message="Access denied")

def ForgotPassword():
    pass

UserLabel.place(x=80,y=100)
UserEntry.place(x=80,y=150)

PasswordLabel.place(x=80,y=200)
PasswordEntry.place(x=80,y=250)

#-----Button
LoginButton = ttk.Button(RightFrame, text="Login",width=30, command=Login )
LoginButton.place(x=80,y=300)

RegisterButton = ttk.Button(RightFrame, text="Register",width=30, command=Register)
RegisterButton.place(x=80,y=350)

ForgotPasswordButton = ttk.Button(RightFrame, text="Forgot Password",width=30, command=ForgotPassword)
ForgotPasswordButton.place(x=80,y=400)

windows.mainloop()



