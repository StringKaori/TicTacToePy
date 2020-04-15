from tkinter import *
from tkinter import messagebox as ms

root=Tk()
root.title("Jogo da velha")
root.geometry("135x122+450+120")

i=0
texto=[None]*9
velha=0
xVitorias=0
oVitorias=0

def reset():
    global botoes,velha,i
    velha=0
    i=-1
    for ii in range(9):
        botoes[ii]["text"]=''
        botoes[ii].configure(state='normal')
        texto[ii]=''
       
        
def click(botao,index):
    global i,texto,velha,botoes,xVitorias,oVitorias
    
    if i%2==0:
        texto[index]="X"
        botao["text"]=texto[index]
        botao.configure(state=DISABLED,disabledforeground="black")
    else:
        texto[index]="O"
        botao["text"]=texto[index]
        botao.configure(state=DISABLED,disabledforeground="black")
        
    if texto[0]==texto[1]==texto[2]=="X" or texto[3]==texto[4]==texto[5]=="X" or texto[6]==texto[7]==texto[8]=="X" or texto[0]==texto[4]==texto[8]=="X" or texto[2]==texto[4]==texto[6]=="X" or texto[0]==texto[3]==texto[6]=="X" or texto[1]==texto[4]==texto[7]=="X" or texto[2]==texto[5]==texto[8]=="X":
        xVitorias+=1
        ms.showinfo("",'X Ganhou')
        reset()
        
    elif texto[0]==texto[1]==texto[2]=="O" or texto[3]==texto[4]==texto[5]=="O" or texto[6]==texto[7]==texto[8]=="O" or texto[0]==texto[4]==texto[8]=="O" or texto[2]==texto[4]==texto[6]=="O" or texto[0]==texto[3]==texto[6]=="O" or texto[1]==texto[4]==texto[7]=="O" or texto[2]==texto[5]==texto[8]=="O":
        oVitorias+=1
        ms.showinfo("",'O Ganhou')
        reset()
        
    else:
        velha+=1

    if velha==9:
        ms.showinfo('','Velha')
        reset()
        
    i+=1
    

textoX="X ganhou:"+str(xVitorias)
xGanhou=Label(root,text=textoX)
################Botões################
botao00=Button(text='',width=5,height=2,command=lambda:click(botao00,0))
botao00.grid(row=0,column=0)
botao01=Button(text='',width=5,height=2,command=lambda:click(botao01,1))
botao01.grid(row=0,column=1)
botao02=Button(text='',width=5,height=2,command=lambda:click(botao02,2))
botao02.grid(row=0,column=2)
botao10=Button(text='',width=5,height=2,command=lambda:click(botao10,3))
botao10.grid(row=1,column=0)
botao11=Button(text='',width=5,height=2,command=lambda:click(botao11,4))
botao11.grid(row=1,column=1)
botao12=Button(text='',width=5,height=2,command=lambda:click(botao12,5))
botao12.grid(row=1,column=2)
botao20=Button(text='',width=5,height=2,command=lambda:click(botao20,6))
botao20.grid(row=2,column=0)
botao21=Button(text='',width=5,height=2,command=lambda:click(botao21,7))
botao21.grid(row=2,column=1)
botao22=Button(text='',width=5,height=2,command=lambda:click(botao22,8))
botao22.grid(row=2,column=2)
botoes=[botao00,botao01,botao02,botao10,botao11,botao12,botao20,botao21,botao22]
######################################

root.mainloop()