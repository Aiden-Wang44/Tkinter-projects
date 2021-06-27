from tkinter import*
import pygame
import time
master=Tk()
master.title("hello")
i2=pygame.image.load('C:/Users/ubons/Downloads/question.png')
i5=pygame.transform.scale(i2,(30,30))
pygame.image.save(i5,'C:/Users/ubons/Downloads/question.png')
i1=PhotoImage(file='C:/Users/ubons/Downloads/question.png')
colors=["red","yellow","green","blue","orange","cyan2","azure","maroon1"]
c=0
r=0
z=0
clicked=[]
score=0
d=StringVar()
d.set(str(score))
class tile:
    def __init__(self):
        self.row=r
        self.column=c
        self.img=i1
        self.color=colors[z]
        self.isclicked=0


    def showimg(self):
        global clicked
        global score
        l2=Label(master,text='    ',bg=self.color)
        l2.grid(row=self.row,column=self.column)
        clicked.append(self.color)
        master.update()
        if len(clicked)==1:
            time.sleep(2)
            l2.destroy()
        elif len(clicked)==2:
            if clicked[0]==clicked[1]:
                score=score+1
                d.set(str(score))
                master.update()
                clicked=[]
                
            else:
                time.sleep(1)
                l2.destroy()
                clicked=[]
        
        
    def draw(self):
        
        
        b1=Button(master,image=i1,command=tile1.showimg)
        b1.grid(row=self.row,column=self.column)
        
for loop in range(1,5,1):
    for loop in range(1,5,1):
        tile1=tile()
        tile1.draw()
        c=c+1
        z=z+1
        if z==7:
            z=0
    c=0
    r=r+1
l3=Label(master,textvariable=d)
l3.grid(row=5,column=1)
master.mainloop()
