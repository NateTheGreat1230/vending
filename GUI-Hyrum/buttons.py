import tkinter as tk
import random

from api import API

itemString = ''
numberTurple = ('1','2','3','4','5','6','7','8','9','0')


def makeItem(put):
    global itemString
    global numberTurple

    if put in numberTurple and itemString in numberTurple or put not in numberTurple and itemString not in numberTurple:
        # happens either if both are numbers or letters
        itemString = put

    elif put in numberTurple and itemString not in numberTurple or put not in numberTurple and itemString in numberTurple:
        # happens if both are different
        if put in numberTurple:
            itemString += put
        elif put not in numberTurple:
            itemString = put + itemString

    if len(itemString) == 2:
        print(itemString + ' fell')
        itemString = ''

def summonButtons():

    btA = tk.Button(root, text = "A", bd = 2, command = lambda: makeItem('A'))
    btB = tk.Button(root, text = "B", bd = 2, command = lambda: makeItem('B'))
    btC = tk.Button(root, text = "C", bd = 2, command = lambda: makeItem('C'))
    btD = tk.Button(root, text = "D", bd = 2, command = lambda: makeItem('D'))
    btE = tk.Button(root, text = "E", bd = 2, command = lambda: makeItem('E'))
    btF = tk.Button(root, text = "F", bd = 2, command = lambda: makeItem('F'))
    bt1 = tk.Button(root, text = "1", bd = 2, command = lambda: makeItem('1'))
    bt2 = tk.Button(root, text = "2", bd = 2, command = lambda: makeItem('2'))
    bt3 = tk.Button(root, text = "3", bd = 2, command = lambda: makeItem('3'))
    bt4 = tk.Button(root, text = "4", bd = 2, command = lambda: makeItem('4'))
    bt5 = tk.Button(root, text = "5", bd = 2, command = lambda: makeItem('5'))
    bt6 = tk.Button(root, text = "6", bd = 2, command = lambda: makeItem('6'))
    bt7 = tk.Button(root, text = "7", bd = 2, command = lambda: makeItem('7'))
    bt8 = tk.Button(root, text = "8", bd = 2, command = lambda: makeItem('8'))
    bt9 = tk.Button(root, text = "9", bd = 2, command = lambda: makeItem('9'))
    bt0 = tk.Button(root, text = "0", bd = 2, command = lambda: makeItem('0'))


    btA.pack()
    btB.pack()
    btC.pack()
    btD.pack()
    btE.pack()
    btF.pack()
    bt1.pack()
    bt2.pack()
    bt3.pack()
    bt4.pack()
    bt5.pack()
    bt6.pack()
    bt7.pack()
    bt8.pack()
    bt9.pack()
    bt0.pack()


    btA.place(x=50, y=50)
    btB.place(x=100, y=50)
    btC.place(x=150, y=50)
    btD.place(x=200, y=50)
    btE.place(x=50, y=100)
    btF.place(x=100, y=100)
    bt1.place(x=150, y=100)
    bt2.place(x=200, y=100)
    bt3.place(x=50, y=150)
    bt4.place(x=100, y=150)
    bt5.place(x=150, y=150)
    bt6.place(x=200, y=150)
    bt7.place(x=50, y=200)
    bt8.place(x=100, y=200)
    bt9.place(x=150, y=200)
    bt0.place(x=200, y=200)



def scanSuccess():
    api.scan()
    customer = api.getCustomer()
    print( customer)

    print('scan successful. Hello {0}, you have ${1} to spend'.format( customer['name'], customer['balance'] ) )

    for product in api.getProducts():
        print( product )

    scanbtn.pack_forget()
    summonButtons()

api = API()

root = tk.Tk()
root.geometry('300x300')
frame = tk.Frame(root)
frame.pack()

instruction_label = tk.Label(root, bg='white', text="Select what you want!")
instruction_label.pack()

scanbtn = tk.Button(root, text = "Scan Face.", bd = 4, command = scanSuccess)
scanbtn.pack(side = 'top')




root.mainloop()
