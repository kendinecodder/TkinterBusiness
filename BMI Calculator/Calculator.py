import tkinter

def clear():
    slavelist = window.pack_slaves()
    for a in slavelist[6:len(slavelist)]:
        a.destroy()


def bmicalculator():
    global result_label
    global clear_button
    wt = weight_entry.get()
    ht = height_entry.get()
    text = ""
    try:
        wtsq = (int(ht)/100) * (int(ht)/100)
        userBMI = round(int(wt) / wtsq, 2)
        if userBMI < 18.5:
            text = "you are underweight"
        if 18.5 <= userBMI <25:
            text = "your weight is healthy weight"
        if 25<= userBMI < 30:
            text = "you are in overweight"
        if 30 <= userBMI:
            text = "you are obese"
        result_label = tkinter.Label(text=f"your BMI is {userBMI}, {text}")
        result_label.pack()
    except:
        if wt == "" or ht == "":
            exceptresult = tkinter.Label(text="Bir değer giriniz.")
            exceptresult.pack()
        else:
            exceptresult = tkinter.Label(text="Değerleri santimetre giriniz.")
            exceptresult.pack()


window = tkinter.Tk()
weight_label = tkinter.Label(text="Enter your weight value: (kg)")
weight_entry = tkinter.Entry()
height_label = tkinter.Label(text="Enter your height value: (cm)")
height_entry = tkinter.Entry()
clear_button = tkinter.Button(text="Clear", command=clear)
calculate_button = tkinter.Button(text="Calculate", command=bmicalculator)

window.minsize(280, 230)
window.title("BMI Calculator")
window.config(pady=30)


weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
clear_button.pack()
calculate_button.pack(pady=20)

userWeight = weight_entry.get()
userHeight = height_entry.get()


tkinter.mainloop()
