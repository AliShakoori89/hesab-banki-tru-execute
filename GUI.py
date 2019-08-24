import tkinter as tk
from tkinter import *
from json_file import JsonHandler
from functools import partial
from tkinter.messagebox import showinfo


class DepositForm(tk.Frame):
    
    def __init__(self, master, **kwargs):
        self.master = master
        tk.Frame.__init__(self, self.master, **kwargs)
        deposit_window = tk.Toplevel(self.master)
        deposit_window.title("deposit box")
        deposit_window.geometry("400x150")
        Label(deposit_window, text="ID number for deposit: ").grid(row=0, column=0)
        id_field = Entry(deposit_window, bg='light gray', width=30, bd=2, selectborderwidth=5)
        id_field.grid(row=0, column=3)
        Label(deposit_window, text="How many sheets: ").grid(row=1, column=0)
        sheet_field = Entry(deposit_window, bg='light gray', width=30, bd=2, selectborderwidth=5)
        sheet_field.grid(row=1, column=3)
        account_deposit_action_with_arg = partial(self.deposit, id_field, sheet_field)
        Button(deposit_window, text='Deposit', command=account_deposit_action_with_arg).place(x=10, y=60)
        
    def deposit(self, id_field, sheet_field):
        sheet=sheet_field.get()
        sheet=int(sheet)
        id_search=id_field.get()
        
        if JsonHandler.open_search(self, id_search):
            list_dic=JsonHandler.open_search(self, id_search)
            JsonHandler.add_sheets(self, list_dic,id_search,sheet)
            showinfo("notification box", "successfully operation")
        else:
            showinfo("notification box", "failed operation because customer not found ")

class DumpForm(tk.Frame):
    def __init__(self,master,**kwargs):
        self.master=master
        tk.Frame.__init__(self,self.master,**kwargs)
        dump_window = tk.Toplevel(self.master)
        dump_window.title("dump box")
        dump_window.geometry("400x150")
        Label(dump_window,text="ID number for dump: ").grid(row=0, column=0)
        id_field = Entry(dump_window, bg='light gray', width=30, bd=2, selectborderwidth=5)
        id_field.grid(row=0, column=3)
        Label(dump_window, text="How many sheets: ").grid(row=1, column=0)
        sheet_field = Entry(dump_window, bg='light gray', width=30, bd=2, selectborderwidth=5)
        sheet_field.grid(row=1, column=3)
        account_dump_action_with_arg =partial(self.dump,id_field,sheet_field)
        Button(dump_window,text="Dump",command=account_dump_action_with_arg).place(x=10,y=60)

        

    def dump(self,id_field,sheet_field):
        sheet=sheet_field.get()
        sheet=int(sheet)
        id_search=id_field.get()
        if JsonHandler.open_search(self, id_search):
            list_dic=JsonHandler.open_search(self, id_search)
            if JsonHandler.sub_sheets(self,list_dic,id_search,sheet):
                showinfo("notification box", "successfully operation")
            else:
                showinfo("notification box", "failed operation because not enough money ")
        else:
            showinfo("notification box", "failed operation because customer not found ")

class WithdrawForm(tk.Frame):
    def __init__(self,master,**kwargs):
        self.master=master
        tk.Frame.__init__(self,self.master,**kwargs)
        withdraw_window = tk.Toplevel(self.master)
        withdraw_window.title("dump box")
        withdraw_window.geometry("400x150")
        Label(withdraw_window,text="ID number for withdraw: ").grid(row=0, column=0)
        id_field = Entry(withdraw_window, bg='light gray', width=30, bd=2, selectborderwidth=5)
        id_field.grid(row=0, column=3)
        account_withdraw_action_with_arg =partial(self.withdraw,id_field)
        Button(withdraw_window,text="withdraw",command=account_withdraw_action_with_arg).place(x=10,y=60)

    def withdraw(self,id_field):
        id_search=id_field.get()
        if JsonHandler.open_search(self,id_search):
            list_dic=JsonHandler.open_search(self, id_search)
            JsonHandler.withdraw(self, list_dic,id_search)
            showinfo("notification box", "successfully operation")
        else:
            showinfo("notification box", "failed operation because customer not found ")

class ShowForm(tk.Frame):
    def __init__(self,master,**kwargs):
        self.master=master
        tk.Frame.__init__(self,self.master,**kwargs)
        show_window = tk.Toplevel(self.master)
        show_window.title("show box")
        list_name=JsonHandler.show(self)
        print(list_name)
        Label(show_window,text=list_name).grid()

def create_deposit_window(args, master=None):
    main_gui = DepositForm(master)

def create_dump_window(args,master=None):
    main_gui = DumpForm(master)

def create_withdraw_window(args, master=None):
    main_gui = WithdrawForm(master)

def create_show_list(args,master=None):
    main_gui = ShowForm(master)

class MainGUI:
    master = tk.Tk()
    master.geometry("400x200")
    master.title("Operation Box")
    name_field = Entry(master, bg='light gray', width=30, bd=2, selectborderwidth=5)
    name_field.grid(row=0, column=3)

    last_name_field = Entry(master, bg='light gray', width=30, bd=2, selectborderwidth=5)
    last_name_field.grid(row=1, column=3)

    id_field = Entry(master, bg='light gray', width=30, bd=2, selectborderwidth=5)
    id_field.grid(row=2, column=3)

    account_number_field = Entry(master, bg='light gray', width=30, bd=2, selectborderwidth=5)
    account_number_field.grid(row=3, column=3)

    supply_field = Entry(master, bg='light gray', width=30, bd=2, selectborderwidth=5)
    supply_field.grid(row=4, column=3)

    name_label = Label(master, text="Name: ")
    name_label.grid(row=0, column=0, sticky=W)

    last_name_label = Label(master, text="LastName: ")
    last_name_label.grid(row=1, column=0, sticky=W)

    id_label = Label(master, text="ID Num: ")
    id_label.grid(row=2, column=0, sticky=W)

    account_number_label = Label(master, text="Bank Account Number: ")
    account_number_label.grid(row=3, column=0, sticky=W)

    supply_label = Label(master, text="supply: ")
    supply_label.grid(row=4, column=0, sticky=W)

    def add_button(self, name_field, last_name_field, id_field, bank_account_field, supply_field):
 
        try:
            id_field=int(id_field.get())
        except ValueError:
            showinfo("notification box", "please input true data type and enter ID number again")
        try:
            name_field=str(name_field.get())
        except ValueError:
            showinfo("notification box", "please input true data type and enter name again")
        try:
            last_name_field=str(last_name_field.get())
        except ValueError:
            showinfo("notification box", "please input true data type and enter lastname again")
        try:
            bank_account_field=int(bank_account_field.get())
        except ValueError:
            showinfo("notification box", "please input true data type and enter bank account number again ")
        try:
            supply_field=int(supply_field.get())
        except ValueError:
            showinfo("notification box", "please input true data type and enter supply again")

        data_dict = {id_field:{'name': name_field, 'lastname': last_name_field, 'id': id_field,
                'bank_account': bank_account_field, 'supply': int(supply_field)}}

        JsonHandler.add(self, data_dict)


    create_add_window_action_with_arg = partial(add_button, master, name_field, last_name_field, id_field,
                                                account_number_field,
                                                supply_field)
    Button(master, text='Add', command=create_add_window_action_with_arg).place(x=10, y=145)

    create_deposit_window_action_with_arg = partial(create_deposit_window, master)
    Button(master, text='Deposit', command=create_deposit_window_action_with_arg).place(x=45, y=145)
    
    create_dump_window_action_with_arg = partial(create_dump_window,master)
    Button(master, text='Dump', command=create_dump_window_action_with_arg).place(x=98, y=145)

    create_withdraw_window_action_with_arg = partial(create_withdraw_window,master)
    Button(master, text="Withdraw", command=create_withdraw_window_action_with_arg).place(x=143,y=145)

    create_show_window_action_with_arg = partial(create_show_list,master)
    Button(master,text="Show",command=create_show_window_action_with_arg).place(x=207,y=145)
    
    master.mainloop()

main = MainGUI
