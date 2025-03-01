from tkinter import *
import tkinter.messagebox

# cores
cor0 = "#444466"  # preto
cor1 = "#feffff"  # branco
cor2 = "#004338"


# criando a janela 

janela = Tk()
janela.geometry("500x200")
janela.configure(bg = cor1)

# configurando a janela

tela = Label(janela, bg = cor0, width = 40, height = 10, bd = 1) # estilo padrão = flat
tela.grid(row = 0, column = 0)

frame_direito = Frame(janela, bg = cor1) 
frame_direito.grid(row = 0, column = 1, padx = 10)

frame_baixo = Frame(janela, bg = cor1)
frame_baixo.grid(row = 1, column = 0, columnspan = 2, pady = 15) # expandir a coluna

# função scale 

def scale(value):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()
    rgb = f"{r}, {g}, {b}"
    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #alterando a cor do fundo da tela
    tela["bg"] = hexadecimal

    # alterando a entry
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)



# função click
def onClick():
    # mensagem
    tkinter.messagebox.showinfo("Color", "The Color has been Copied!")


    # criar o botão de copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()


# configurando o frame direito
# vermelho (red)
l_red = Label(frame_direito, text = "Red", width = 7, bg = cor1, fg = "red", anchor = "nw", font = ("Time New Roman", 12, "bold"))
l_red.grid(row = 0, column = 0)

s_red = Scale(frame_direito, command = scale, from_= 0, to = 255, length = 150, bg = cor1, fg = "red", orient = "horizontal")
s_red.grid(row = 0, column = 1)

# verde (green)
l_green = Label(frame_direito, text = "Green", width = 7, bg = cor1, fg = "green", anchor = "nw", font = ("Time New Roman", 12, "bold"))
l_green.grid(row = 1, column = 0)

s_green = Scale(frame_direito, command = scale, from_= 0, to = 255, length = 150, bg = cor1, fg = "green", orient = "horizontal")
s_green.grid(row = 1, column = 1)

# azul (blue)
l_blue = Label(frame_direito, text = "Blue", width = 7, bg = cor1, fg = "blue", anchor = "nw", font = ("Time New Roman", 12, "bold"))
l_blue.grid(row = 2, column = 0)

s_blue = Scale(frame_direito, command = scale, from_= 0, to = 255, length = 150, bg = cor1, fg = "blue", orient = "horizontal")
s_blue.grid(row = 2, column = 1)

# configurando o frame baixo
l_rgb = Label(frame_baixo, text = "RGB Code: ", bg = cor1, font = ("Ivy", 10, "bold"))
l_rgb.grid(row = 0, column = 0, padx = 5)

# entry 

e_cor = Entry(frame_baixo, width = 12, font = ("Ivy", 10, "bold"), justify = "center")
e_cor.grid(row = 0, column = 1, padx = 5)

# botão copiar
b_copiar = Button(frame_baixo, command = onClick, text = "Copy", bg = cor1, font = ("Ivy", 8, "bold"), relief = "raised", overrelief = "ridge")
b_copiar.grid(row = 0, column = 2, padx = 5)

# app name
l_app_name = Label(frame_baixo, text = "Color Selector", bg = cor1, font = ("Ivy", 15, "bold"))
l_app_name.grid(row = 0, column = 3, padx = 40)

janela.mainloop()