from tkinter import *

def CalculateAge():
    from datetime import datetime
    try:
        Year = int(year_entry.get())
        Month = int(month_entry.get())
        Day = int(date_entry.get())
        today = datetime.now()
        age = today.year - Year - ((today.month, today.day) < (Month, Day))
        result_label.config(text=f"Your age is: {age} years")
    except Exception as e:
        result_label.config(text="Pleas enter valid input")

def main():
    global year_entry, month_entry, date_entry,result_label
    wind= Tk()
    wind.title('Age Calculator')
    wind.geometry('400x400')
    f1= Frame(wind)
    f1.grid(row=0,column=0,columnspan=3)
    Label(f1,text="Enter date of birth ", font=('Arial',12,'bold')).grid(columnspan=4,pady=20)
    label_year = Label(wind,text='Enter Year  : ').grid(row=1,column=0,padx=10,pady=5)
    label_month = Label(wind,text='Enter Month : ').grid(row=2,column=0,padx=10,pady=5)
    label_date = Label(wind,text='Enter Date  : ').grid(row=3,column=0,padx=10,pady=5)

    year_entry = Entry(wind,textvariable=IntVar())
    year_entry.grid(row=1,column=1)
    month_entry = Entry(wind,textvariable=IntVar())
    month_entry.grid(row=2,column=1)
    date_entry = Entry(wind,textvariable=IntVar())
    date_entry.grid(row=3,column=1)

    result_label=Label(wind,text="hello")
    result_label.grid(row=4,column=1,pady=10)
    Button(wind,text='Calculate Age',command=CalculateAge).grid(row=4,column=0,columnspan=1,pady=10,padx=10)

    wind.mainloop()


if __name__ == '__main__':
    main()