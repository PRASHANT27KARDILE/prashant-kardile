

import os
import pymysql

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('1240x600+0+0')  # 1240x720 is WH and 0+0 is position axis
root.title('Electric Shop Management')
root.config(bg='#fff')
# Variables
font = ('san-serif', 16, 'bold')
bg = 'gray'
fg = 'black'

# Create form variable
sid = tk.StringVar()
fname = tk.StringVar()
lname = tk.StringVar()
Class_ = tk.StringVar()
stream = tk.StringVar()
email = tk.StringVar()
mob = tk.StringVar()
python = tk.IntVar()
sql = tk.IntVar()
ml = tk.IntVar()
total = tk.IntVar()
per = tk.IntVar()
grade = tk.StringVar()


# Functions
def close_window():
    ask = messagebox.askyesno('Warning', 'Do you want to close')
    if ask:
        root.destroy()


def reset():
    sid.set(' ')
    fname.set(' ')
    lname.set(' ')
    Class_.set(' ')
    stream.set(' ')
    email.set(' ')
    mob.set(' ')
    python.set(0)
    ml.set(0)
    sql.set(0)
    total.set(0)
    per.set(0)
    grade.set(' ')


def calculate():
    t = python.get() + ml.get() + sql.get()
    total.set(t)
    p = t / 3
    per.set(p)
    if p >= 75:
        grade.set('A')
    elif 60 <= p <= 75:
        grade.set('B')
    elif 40 <= p <= 60:
        grade.set('C')
    else:
        grade.set('Fail')


# To save a file
def connect_db():
    conn = pymysql.connect(host = 'localhost',
                           user = 'root',
                           password = 'PRASHANT123',
                           database = 'gui')
    cursor = conn.cursor()
    return conn, cursor
    
      
def is_exits():
    conn, cursor = connect_db()
    query = f''' select * from result where sid = {sid.get()} '''
    cursor.execute(query)
    record = cursor.fetchone()
    if record:
        ask = tk.messagebox.askyesno('warning ' ,
                                     'Record already exits, do you want to update it ')
        
        if ask:
            query = f''' select * from result where sid = {sid.get()} '''
            cursor.execute(query)
            conn.commit()
            conn.close()
            saves()
            tk.messagebox.showinfo('SUCCESS , Record update successfully')
              
    else:
        saves()
        tk.messagebox.showinfo('SUCCESS', 
                               'Record saved successfully')



# search 


def search():
    con, cursor = connect_db()
    query = f''' select *from result where sid = {sid.get()}'''
    cursor.execute(query)
    record = cursor.fetchone()
    if record:
        fname.set(record[1])
        lname.set(record[2])
        Class_.set(record[3])
        stream.set(record[4])
        email.set(record[5])
        mob.set(record[6])
        python.set(record[7])
        ml.set(record[8])
        sql.set(record[9])
        total.set(record[10])
        per.set(record[11])
        grade.set(record[12])
        con.commit()
        cursor.close()
        con.close()
    
    else:
        tk.messagebox.showinfo('error','file does not exisit')

def delete():
    con, cursor = connect_db()
    query = f''' select *from result where sid = {sid.get()}'''
    cursor.execute(query)
    record = cursor.fetchone()
    if record:
        ask = messagebox.askyesno('Warning ' , 'Do you wanna delete')
        
        if ask:
            query = f'''delete from result where sid= {sid.get()}'''
            cursor.execute(query)
            con.commit()
            cursor.close() 
            con.close()
            messagebox.showinfo('Success ' , 'Deleted')
         
    
   
   




                       


def saves():
    calculate()
    conn, cursor = connect_db()
    query = f''' insert into result values
    ('{sid.get()}','{fname.get()}','{lname.get()}','{Class_.get()}','{stream.get()}','{email.get()}','{mob.get()}',{python.get()},{ml.get()},{sql.get()},{total.get()},{per.get()},'{grade.get()}')'''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
   
    



# Creating a frames
top_frame = tk.Frame(root, bg='gray')
top_frame.place(x=5, y=5, width=1240, height=100)

lft_frame = tk.Frame(root, bg='gray')
lft_frame.place(x=5, y=110, width=620, height=380)

rgt_frame = tk.Frame(root, bg='gray')
rgt_frame.place(x=630, y=110, width=620, height=380)

btm_frame = tk.Frame(root, bg='gray')
btm_frame.place(x=5, y=496, width=1240, height=100)

title = tk.Label(top_frame, text='Result', font=('san-serif', 30, 'bold'), bg='gray', fg='black')
title.pack(pady=20)

lft_title = tk.Label(lft_frame, text='Student Info', font=('san-serif', 30, 'bold'), bg='gray', fg='black')
lft_title.pack(pady=20)

lft_title.grid(row=0, column=0, padx=5, pady=5)

rgt_title = tk.Label(rgt_frame, text='Marks', font=('san-serif', 30, 'bold'), bg='gray', fg='black')
rgt_title.pack(pady=20)

rgt_title.grid(row=0, column=0, padx=5, pady=5)

sid_lbl = tk.Label(lft_frame, text='SID', font=font, bg=bg, fg=fg)
sid_lbl.grid(row=1, column=0, padx=5, pady=5)

sid_entry = tk.Entry(lft_frame, textvariable=sid, font=font, bg=bg, fg=fg)
sid_entry.grid(row=1, column=1, padx=5, pady=5)

fname_lbl = tk.Label(lft_frame, text='FName', font=font, bg=bg, fg=fg)
fname_lbl.grid(row=2, column=0, padx=5, pady=5)

fname_entry = tk.Entry(lft_frame, textvariable=fname, font=font, bg=bg, fg=fg)
fname_entry.grid(row=2, column=1, padx=5, pady=5)

lname_lbl = tk.Label(lft_frame, text='LName', font=font, bg=bg, fg=fg)
lname_lbl.grid(row=3, column=0, padx=5, pady=5)

lname_entry = tk.Entry(lft_frame, textvariable=lname, font=font, bg=bg, fg=fg)
lname_entry.grid(row=3, column=1, padx=5, pady=5)

class_lbl = tk.Label(lft_frame, text='Class', font=font, bg=bg, fg=fg)
class_lbl.grid(row=4, column=0, padx=5, pady=5)

class_entry = tk.Entry(lft_frame, textvariable=Class_, font=font, bg=bg, fg=fg)
class_entry.grid(row=4, column=1, padx=5, pady=5)

stream_lbl = tk.Label(lft_frame, text='Stream', font=font, bg=bg, fg=fg)
stream_lbl.grid(row=5, column=0, padx=5, pady=5)

stream_entry = tk.Entry(lft_frame, textvariable=stream, font=font, bg=bg, fg=fg)
stream_entry.grid(row=5, column=1, padx=5, pady=5)

email_lbl = tk.Label(lft_frame, text='Email', font=font, bg=bg, fg=fg)
email_lbl.grid(row=6, column=0, padx=5, pady=5)

email_entry = tk.Entry(lft_frame, textvariable=email, font=font, bg=bg, fg=fg)
email_entry.grid(row=6, column=1, padx=5, pady=5)

mob_lbl = tk.Label(lft_frame, text='Mobile No', font=font, bg=bg, fg=fg)
mob_lbl.grid(row=7, column=0, padx=5, pady=5)

mob_entry = tk.Entry(lft_frame, textvariable=mob, font=font, bg=bg, fg=fg)
mob_entry.grid(row=7, column=1, padx=5, pady=5)

python_lbl = tk.Label(rgt_frame, text='Python', font=font, bg=bg, fg=fg)
python_lbl.grid(row=1, column=0, padx=5, pady=5)

python_entry = tk.Entry(rgt_frame, textvariable=python, font=font, bg=bg, fg=fg)
python_entry.grid(row=1, column=1, padx=5, pady=5)

ml_lbl = tk.Label(rgt_frame, text='Machine Learning', font=font, bg=bg, fg=fg)
ml_lbl.grid(row=2, column=0, padx=5, pady=5)

ml_entry = tk.Entry(rgt_frame, textvariable=ml, font=font, bg=bg, fg=fg)
ml_entry.grid(row=2, column=1, padx=5, pady=5)

sql_lbl = tk.Label(rgt_frame, text='SQL', font=font, bg=bg, fg=fg)
sql_lbl.grid(row=3, column=0, padx=5, pady=5)

sql_entry = tk.Entry(rgt_frame, textvariable=sql, font=font, bg=bg, fg=fg)
sql_entry.grid(row=3, column=1, padx=5, pady=5)

total_lbl = tk.Label(rgt_frame, text='Total', font=font, bg=bg, fg=fg)
total_lbl.grid(row=4, column=0, padx=5, pady=5)

total_entry = tk.Entry(rgt_frame, textvariable=total, font=font, bg=bg, fg=fg)
total_entry.grid(row=4, column=1, padx=5, pady=5)

per_lbl = tk.Label(rgt_frame, text='Percentage', font=font, bg=bg, fg=fg)
per_lbl.grid(row=5, column=0, padx=5, pady=5)

per_entry = tk.Entry(rgt_frame, textvariable=per, font=font, bg=bg, fg=fg)
per_entry.grid(row=5, column=1, padx=5, pady=5)

grd_lbl = tk.Label(rgt_frame, text='Grade', font=font, bg=bg, fg=fg)
grd_lbl.grid(row=6, column=0, padx=5, pady=5)

grd_entry = tk.Entry(rgt_frame, textvariable=grade, font=font, bg=bg, fg=fg)
grd_entry.grid(row=6, column=1, padx=5, pady=5)

quit_btn = tk.Button(btm_frame, text='Quit', font=font, bg=fg, fg=bg, command=close_window)
quit_btn.pack(padx=20, pady=20, side=tk.RIGHT)

reset_btn = tk.Button(btm_frame, text='Reset', font=font, bg=fg, fg=bg, command=reset)
reset_btn.pack(pady=20, padx=20, side=tk.RIGHT)

save_btn = tk.Button(btm_frame, text='Save', font=font, bg=fg, fg=bg, command= is_exits)
save_btn.pack(pady=20, padx=20, side=tk.RIGHT)


searc_btn = tk.Button(btm_frame, text='Search', font=font, bg=fg, fg=bg, command= search)
searc_btn.pack(pady=5, padx=5, side=tk.RIGHT)


det_btn = tk.Button(btm_frame, text='Delete', font=font, bg=fg, fg=bg, command= delete)
det_btn.pack(pady=5, padx=5, side=tk.RIGHT)



root.mainloop()