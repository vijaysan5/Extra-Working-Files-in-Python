

from tkinter import messagebox
import tkinter as tk

user = "yazhrose"
pswd = "2123"
account= {
    "001_Acc2003" : {"name" : "vijay", "balance" : 200000}
}

def login():
    userid = username_entry.get()
    passid = password_entry.get()
    
    if (userid == user) and (passid == pswd):
        messagebox.showinfo("Login Info", "Login Successfully...")
        login_window.destroy()
        open_account_win()
    else:
        res = messagebox.askyesno("Error", "username is wrong. Create new login?")
        if res:
            create_login()
def create_login():
    global user, pswd
    user = username_entry.get()
    pswd = password_entry.get()
    messagebox.showinfo("Login Info", "New Login Id is Created")
    

def open_account_win():
    global acc_entry
    acc_window = tk.Tk()
    acc_window.title("Account window")
    acc_window.geometry("200x200")

    tk.Label(acc_window, text="Enter Account Number").pack()
    acc_entry = tk.Entry(acc_window)
    acc_entry.pack()

    tk.Button(acc_window, text="Submit", command=open_check_account).pack()
    acc_window.mainloop()
def open_check_account():
    acc_no = acc_entry.get()
    if acc_no in account:
        messagebox.showinfo("Account Check", "Account Number is found")
        open_bank_win(acc_no)
    else:
        res = messagebox.askyesno("Error","Account is not found. Create new Account?")
        if res:
            create_account()

def create_account():
    new_acc =tk.Tk()
    new_acc.title("Create Account")
    new_acc.geometry("300x200")

    tk.Label (new_acc, text="Name").place(x=0, y=5)
    name = tk.Entry (new_acc)
    name.place(x=150, y=5)

    tk.Label (new_acc, text="New Account Number").place(x=0, y=30)
    acc_no = tk.Entry (new_acc)
    acc_no.place(x=150, y=30)

    def save():
        account[acc_no.get()] = {
            "name" : name.get(),
            "balance" : 100,
        }
        messagebox.showinfo("New Account", "New Account is Created")
        new_acc.destroy()
        
    tk.Button(new_acc, text="Create", command=save).place(x=130, y=100)
    new_acc.mainloop()

def open_bank_win(acc_no):
    bank_win = tk.Tk()
    bank_win.title("Account Detailz...")
    bank_win.geometry("300x300")

    def check_balance():
        bal = account[acc_no]["balance"]
        messagebox.showinfo("Account Balance", f"Your Account Blance :{bal}") 
    def Deposit():
        amt = int(ammount_entry.get())
        account[acc_no]["balance"] += amt
        messagebox.showinfo("Show Deposit Info", "Amount is Deposited..!")
    def withdraw():
        amt = int(ammount_entry.get())
        if amt <= account[acc_no]["balance"]:
            account[acc_no]["balance"] -= amt
            messagebox.showinfo("Show Depit Info",  "Amount is Depited..!")
        else:
            messagebox.showwarning("Error", "Check your Account Balance..!")
    tk.Label (bank_win, text="Enter Amount").pack()
    ammount_entry = tk.Entry(bank_win)
    ammount_entry.pack()

    tk.Button(bank_win, text="Check Balance", command=check_balance).place(x=130, y=130)
    tk.Button(bank_win, text="Deposit", command=Deposit).place(x=130, y=200)
    tk.Button(bank_win, text="Withdraw", command=withdraw).place(x=130, y=270)

    bank_win.mainloop()


login_window = tk.Tk()
login_window.title("User Login Page...")
login_window.geometry("200x200")

tk.Label (login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label (login_window, text="Password").pack()
password_entry = tk.Entry(login_window)
password_entry.pack()

tk.Button(login_window, text="Submit", command=login).pack()

login_window.mainloop()