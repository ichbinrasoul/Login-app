from tkinter import *
from tkinter import messagebox
import os

def login():
    user = username.get()
    code = password.get()

    if user == 'ichbinrussellhj' and code == 'r11061368r':
        root = Toplevel(screen)
        root.title('صورتحساب')
        root.geometry('1005x500')
        root.configure(bg='lightblue')
        root.resizable(False, False)

    #start
        def Reset():
            entry_sandwich.delete(0, END)
            entry_cookie.delete(0, END)
            entry_tea.delete(0, END)
            entry_coffee.delete(0, END)
            entry_juice.delete(0, END)
            entry_pancake.delete(0, END)
            entry_pastrey.delete(0, END)

        def Total():
            try:
                a1 = int(sandwich.get())
            except:
                a1 = 0

            try:
                a2 = int(cookie.get())
            except:
                a2 = 0

            try:
                a3 = int(tea.get())
            except:
                a3 = 0

            try:
                a4 = int(coffee.get())
            except:
                a4 = 0

            try:
                a5 = int(juice.get())
            except:
                a5 = 0

            try:
                a6 = int(pancake.get())
            except:
                a6 = 0

            try:
                a7 = int(pastrey.get())
            except:
                a7 = 0

            # define cost of each itme per quantity
            cost1 = 20000*a1
            cost2 = 10000*a2
            cost3 = 7000*a3
            cost4 = 10000*a4
            cost5 = 12000*a5
            cost6 = 15000*a6
            cost7 = 30000*a7

            entry_total = Entry(f2, font=('Cascadia Code', 17, 'bold'),
                                textvariable=Total_bill, bd=6, width=14, bg='lightgreen')
            entry_total.place(x=60, y=100)

            total_cost = cost1+cost2+cost3+cost4+cost5+cost6+cost7
            string_bill = 'تومان', str('%.2f' % total_cost)
            Total_bill.set(string_bill)


        Label(text='مدیریت صورتحساب', bg='black', fg='white', font=(
            'Cascadia code', 33), width='300', height='2').pack()

        # manu card
        f = Frame(root, bg='lightgreen', highlightbackground='black',
                highlightthickness=1, width=300, height=370)
        f.place(x=10, y=122)

        Label(f, text='منو', font=('Cascadia Code', 40, 'bold'),
            fg='black', bg='lightgreen').place(x=100, y=0)

        Label(f, font=('Cascadia Mono', 16, 'bold'), text='ساندویچ..........20.000',
            fg='black', bg='lightgreen').place(x=10, y=80)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='کلوچه..........10.000',
            fg='black', bg='lightgreen').place(x=10, y=110)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='چای...........7.000',
            fg='black', bg='lightgreen').place(x=10, y=140)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='قهوه..........10.000',
            fg='black', bg='lightgreen').place(x=10, y=170)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='آبمیوه..........12.000',
            fg='black', bg='lightgreen').place(x=10, y=200)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='پنکیک..........15.000',
            fg='black', bg='lightgreen').place(x=10, y=230)
        Label(f, font=('Cascadia Mono', 16, 'bold'), text='پاستا..........30.000',
            fg='black', bg='lightgreen').place(x=10, y=260)

        # Entry Work
        f1 = Frame(root, bd=3, height=400, width=450, relief=RAISED)
        f1.pack()

        sandwich = StringVar()
        cookie = StringVar()
        tea = StringVar()
        coffee = StringVar()
        juice = StringVar()
        pancake = StringVar()
        pastrey = StringVar()
        Total_bill = StringVar()


        # Bill
        f2 = Frame(root, bg='lightyellow', highlightbackground='black',
                highlightthickness=1, width=300, height=370)
        f2.place(x=690, y=118)

        Bill = Label(f2, text=":قیمت نهایی", font=('Cascadia Code', 17), bg='lightyellow')
        Bill.place(x=100, y=10)


        # Label
        lbl_sandwich = Label(f1, font=('Cascadia Code', 15, 'bold'),
                            text='ساندویچ', width=14, fg='blue')
        lbl_cookie = Label(f1, font=('Cascadia Code', 15, 'bold'),
                        text='کلوچه', width=14, fg='blue')
        lbl_tea = Label(f1, font=('Cascadia Code', 15, 'bold'),
                        text='چای', width=14, fg='blue')
        lbl_coffee = Label(f1, font=('Cascadia Code', 15, 'bold'),
                        text='قهوه', width=14, fg='blue')
        lbl_juice = Label(f1, font=('Cascadia Code', 15, 'bold'),
                        text='آبمیوه', width=14, fg='blue')
        lbl_pancake = Label(f1, font=('Cascadia Code', 15, 'bold'),
                            text='پنکیک', width=14, fg='blue')
        lbl_pastrey = Label(f1, font=('Cascadia Code', 15, 'bold'),
                            text='پاستا', width=14, fg='blue')

        lbl_sandwich.grid(row=2, column=0)
        lbl_cookie.grid(row=3, column=0)
        lbl_tea.grid(row=4, column=0)
        lbl_coffee.grid(row=5, column=0)
        lbl_juice.grid(row=6, column=0)
        lbl_pancake.grid(row=7, column=0)
        lbl_pastrey.grid(row=8, column=0)

        # Entry
        entry_sandwich = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=sandwich, bd=6, width=8, bg='lightpink')
        entry_cookie = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=cookie, bd=6, width=8, bg='lightpink')
        entry_tea = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                        textvariable=tea, bd=6, width=8, bg='lightpink')
        entry_coffee = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=coffee, bd=6, width=8, bg='lightpink')
        entry_juice = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=juice, bd=6, width=8, bg='lightpink')
        entry_pancake = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=pancake, bd=6, width=8, bg='lightpink')
        entry_pastrey = Entry(f1, font=('Cascadia Code', 18, 'bold'),
                            textvariable=pastrey, bd=6, width=8, bg='lightpink')

        entry_sandwich.grid(row=2, column=1)
        entry_cookie.grid(row=3, column=1)
        entry_tea.grid(row=4, column=1)
        entry_coffee.grid(row=5, column=1)
        entry_juice.grid(row=6, column=1)
        entry_pancake.grid(row=7, column=1)
        entry_pastrey.grid(row=8, column=1)

        # Button
        btn_reset = Button(f1, bd=5, fg='black', bg='lightblue', font=(
            'Cascadia mono', 16, 'bold'), width=10, text='بازنشانی', command=Reset)
        btn_reset.grid(row=9, column=0)

        btn_total = Button(f1, bd=5, fg='black', bg='lightblue', font=(
            'Cascadia mono', 16, 'bold'), width=10, text='جمع', command=Total)
        btn_total.grid(row=9, column=1)

        #End


    # alerts, when someone tries to enter wrong user and password

    elif user == '' and code == '':
        messagebox.showerror('لطفا نام کاربری و رمز را صحیح وارد کنید')

    elif user == '':
        messagebox.showerror('لطفا نام کاربری را صحیح وارد کنید')

    elif code == '':
        messagebox.showerror('لطفا رمز صحیح را وارد کنید')

    elif user != 'ichbinrussellhj' and code != 'r11061368r':
        messagebox.showerror('لطفا نام کاربری و رمز را صحیح وارد کنید')

    elif user != 'ichbinrussellhj':
        messagebox.showerror('لطفا نام کاربری را صحیح وارد کنید')

    elif code!= 'r11061368r':
        messagebox.showerror('لطفا رمز صحیح را وارد کنید')    


def main_screen():

    global screen
    global username
    global password

    screen = Tk()
    screen.config(bg='yellow')

    #icon
    # image_icon = PhotoImage("login_pic.png")
    # screen.iconphoto(False,image_icon)
    screen.title('ورود کابر')

    lbl_title = Label(text='صفحه ورود کاربر', font=('Cascadia Mono', 50, 'bold'), foreground='black')
    lbl_title.pack(pady=50)

    border_color = Frame(screen, bg='darkblue', width=800, height=400)
    border_color.pack()

    main_frame = Frame(border_color, bg='lightblue', width= 800, height=400)
    main_frame.pack(padx=20, pady=20)

    Label(main_frame, text='نام کابری', font=('Cascadia Code', 30, 'bold'), bg='pink').place(x=100, y=50)
    Label(main_frame, text='رمز عبور', font=('Cascadia Code', 30, 'bold'), bg='pink').place(x=100, y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(main_frame, textvariable=username, width=12, bd=2, font=('arial', 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(main_frame, textvariable=password, width=12, bd=2, font=('arial', 30), show='*')
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(main_frame, text='ورود', height='2', width=23, bg='red', fg='light blue', bd=0, command=login).place(x=100, y=250)
    Button(main_frame, text='بازنشانی', height='2', width=23, bg='green', fg='light blue', bd=0, command=reset).place(x=300, y=250)
    Button(main_frame, text='خروج', height='2', width=23, bg='dark blue', fg='light blue', bd=0, command=screen.destroy).place(x=500, y=250)

    screen.mainloop()
    
main_screen()