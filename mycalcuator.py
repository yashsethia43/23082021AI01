import tkinter as tkr
app = tkr.Tk(__name__)
app.title('Calculator')
app.geometry('400x400')
tkr.Label(app,text='My Calculator').place(x=75,y=1)
tkr.Label(app,text='Enter First value',font=('Arial',10)).place(x=30,y=70)
tkr.Label(app,text='Enter Second value',font=('Arial',10)).place(x=150,y=70)

fv = tkr.Variable(app)
sv = tkr.Variable(app)

tkr.Entry(app, textvariable=fv, width=15).place(x=30,y=90)
tkr.Entry(app, textvariable=sv, width=15).place(x=150,y=90)

def  operate():
    res.set(int(fv.get())+int(sv.get()))
    #print(int(fv.get())+int(v2.get()))
def operatep():
     res.set(int(fv.get())*int(sv.get()))
     #print(int(fv.get())*int(v2.get()))
def  operated():
    res.set(int(fv.get())/int(sv.get()))
    #print(int(fv.get())/int(v2.get()))
def  operatem():
    res.set(int(fv.get())-int(sv.get()))
    #print(int(fv.get())-int(v2.get()))
        
    
    

tkr.Button(app,text='+',command= operate).place(x=30,y=150)
tkr.Button(app,text='-',command=operatem).place(x=90,y=150)
tkr.Button(app,text='x',command= operatep).place(x=150,y=150)
tkr.Button(app,text='/',command= operated).place(x=210,y=150)


tkr.Label(app,text='Result').place(x=90,y=240)

res=tkr.Variable(app)
res.set('0')
tkr.Label(app,textvariable=res,font=('Arial',15)).place(x=130,y=235)


app.mainloop()
