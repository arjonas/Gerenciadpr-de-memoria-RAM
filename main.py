from psutil import virtual_memory
import tkinter

#Variaveis#


#Ambiemte grafico#


janela = tkinter.Tk()
janela.title("Memoria Ram")
janela.config(height=250,width=250)


canvas= tkinter.Canvas(height=100,width=100)
img = tkinter.PhotoImage(file='pc.png')
canvas.create_image(100,100,image=img)
canvas.grid(column=0,row=0)

def atualizar():

    obj_mem = virtual_memory()

    total_mem = obj_mem[0]
    usada_mem = obj_mem[3]
    livre_mem = obj_mem[1]

    free = tkinter.Label(text=f'Memória livre :{round(livre_mem/1000000000,3)} MB', font=('Abys', 10,'bold'))
    free.grid(column=0, row=1)

    total = tkinter.Label(text=f'Memória total do sistema :{round(total_mem / 1000000000,3)} MB',
                          font=('Abys', 10, 'bold'))
    total.grid(column=0, row=3)

    usando = tkinter.Label(text=f'Memória Utilizada pelo sistema :{round(usada_mem / 1000000000,3)} MB ',
                          font=('Abys', 10, 'bold'))
    usando.grid(column=0, row=5)


    janela.after(3000,atualizar)



atualizar()

janela.mainloop()