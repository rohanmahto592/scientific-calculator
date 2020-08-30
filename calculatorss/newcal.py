from tkinter import *
from tkinter.messagebox import *
from audio import  playaudio
import threading
import math as m

font=('Times',"18","bold italic")
ob=playaudio()


def allclr():
    textfiled.delete(0,END)
def clr():
    ex=textfiled.get()
    ex=ex[0:len(ex)-1]
    textfiled.delete(0,END)
    textfiled.insert(0,ex)
    
def clickbtn(event):
    b=event.widget
    text=b['text']
    t= threading.Thread(target=ob.speak,args=(text,))
    t.start()
    if text=='x':
        textfiled.insert(END,"*")
        return
    if text=='=':
        try:
            ex=textfiled.get()
            answer=eval(ex)
            textfiled.delete(0,END)
            textfiled.insert(0,answer)
        except Exception as e:
            #print("Error..", e)
            showerror("Error", e)
        return
            
    textfiled.insert(END,text)
    
window=Tk()
window.title("My Calculator")
window.geometry("480x620")
pic=PhotoImage(file='calculator.png')
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=5)
heading2=Label(window,text="Calculator",font=font)
heading2.pack(side=TOP)
##textfiled
textfiled=Entry(window,font=font,justify=CENTER)
textfiled.pack(side=TOP,pady=5,fill=X)
##creating button frame
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP)
##adding button
t=1
for i in range(3):
    for j in range(3):
        btn1=Button(buttonFrame,text=str(t),font=font,width=5,relief='ridge',activebackground='red',activeforeground="orange")
        btn1.grid(row=i,column=j,padx=5,pady=5)
        t+=1
        btn1.bind('<Button-1>',clickbtn)
zerobtn=Button(buttonFrame,text='0',font=font,width=5,relief='ridge',activeforeground="orange")
zerobtn.grid(row=3,column=0,padx=5,pady=5)
dotbtn=Button(buttonFrame,text='.',font=font,width=5,relief='ridge',activeforeground="orange")
dotbtn.grid(row=3,column=1,padx=5,pady=5)
equalbtn=Button(buttonFrame,text='=',font=font,width=5,relief='ridge',activeforeground="orange")
equalbtn.grid(row=3,column=2,padx=5,pady=5)
plusbtn=Button(buttonFrame,text='+',font=font,width=5,relief='ridge',activeforeground="orange")
plusbtn.grid(row=0,column=3,padx=5,pady=5)
minusbtn=Button(buttonFrame,text='-',font=font,width=5,relief='ridge',activeforeground="orange")
minusbtn.grid(row=1,column=3,padx=5,pady=5)
mulbtn=Button(buttonFrame,text='x',font=font,width=5,relief='ridge',activeforeground="orange")
mulbtn.grid(row=2,column=3,padx=5,pady=5)
dividebtn=Button(buttonFrame,text='/',font=font,width=5,relief='ridge',activeforeground="orange")
dividebtn.grid(row=3,column=3,padx=5,pady=5)
oneclrbtn=Button(buttonFrame,text='<--',font=font,width=5,relief='ridge',activeforeground="orange",command=clr)
oneclrbtn.grid(row=4,column=0,padx=5,pady=5)
allclrbtn=Button(buttonFrame,text='AC',font=font,width=5,relief='ridge',activeforeground="orange",command=allclr)
allclrbtn.grid(row=4,column=1,padx=5,pady=5)

## binding rest button
plusbtn.bind("<Button-1>",clickbtn)
dotbtn.bind("<Button-1>",clickbtn)
minusbtn.bind("<Button-1>",clickbtn)
dividebtn.bind("<Button-1>",clickbtn)
mulbtn.bind("<Button-1>",clickbtn)
zerobtn.bind("<Button-1>",clickbtn)
equalbtn.bind("<Button-1>",clickbtn)

## creating frame
sc_frame=Frame(window)
powbttn=Button(sc_frame,text="^",font=font,width=5,relief='ridge',activeforeground="orange")
powbttn.grid(row=0,column=0,padx=5,pady=5)
sqrbtn=Button(sc_frame,text='√x',font=font,width=5,relief='ridge',activeforeground="orange")
sqrbtn.grid(row=0,column=1,padx=5,pady=5)
factorialbtn=Button(sc_frame,text='x!',font=font,width=5,relief='ridge',activeforeground="orange")
factorialbtn.grid(row=0,column=2,padx=5,pady=5)
radbtn=Button(sc_frame,text='toRad',font=font,width=5,relief='ridge',activeforeground="orange")
radbtn.grid(row=0,column=3,padx=5,pady=5)
todegreebtn=Button(sc_frame,text='toDeg',font=font,width=5,relief='ridge',activeforeground="orange")
todegreebtn.grid(row=1,column=0,padx=5,pady=5)
sinbtn=Button(sc_frame,text='sinθ',font=font,width=5,relief='ridge',activeforeground="orange")
sinbtn.grid(row=1,column=1,padx=5,pady=5)
cosbtn=Button(sc_frame,text='cosθ',font=font,width=5,relief='ridge',activeforeground="orange")
cosbtn.grid(row=1,column=2,padx=5,pady=5)
tanbtn=Button(sc_frame,text='tanθ',font=font,width=5,relief='ridge',activeforeground="orange")
tanbtn.grid(row=1,column=3,padx=5,pady=5)




## creating scientific functions
normalcal=True

def calc(event):
    btn=event.widget
    text=btn['text']
    print(text)
    ans=" "
    ex=textfiled.get()
    if text=="toDeg":
       ans=str(m.degrees(float(ex)))
    elif text=="toRad":
        ans=str(m.radians(float(ex)))
    elif text=="x!":
        ans=str(m.factorial(int(ex)))
    elif text=="sinθ":
        ans=str(m.sin(m.radians(int(ex))))
    elif text=="cosθ":
        ans=str(m.cos(m.radians(int(ex))))
    elif text=="tanθ":
        ans=str(m.tan(m.radians(int(ex))))
    elif text=="√x":
        ans=str(m.sqrt(int(ex)))
    elif text=="^":
        base,power=ex.split(',')
        ans=str(m.pow(float(base),int(power)))
    
    textfiled.delete(0,END)
    textfiled.insert(0,ans)

def sci_fic():
    global normalcal
    if normalcal:
        window.geometry("480x680")
        buttonFrame.pack_forget()
        sc_frame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        normalcal=False

    else:
        sc_frame.pack_forget()
        window.geometry("480x620")
        normalcal=True

##adding scientic part
sqrbtn.bind('<Button-1>',calc)
sinbtn.bind('<Button-1>',calc)
cosbtn.bind('<Button-1>',calc)
tanbtn.bind('<Button-1>',calc)
powbttn.bind('<Button-1>',calc)
todegreebtn.bind('<Button-1>',calc)
radbtn.bind('<Button-1>',calc)
factorialbtn.bind('<Button-1>',calc)

menubar=Menu(window)
mode=Menu(menubar,font=font,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sci_fic)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)

window.mainloop()