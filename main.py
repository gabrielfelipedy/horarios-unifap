# Passo a Passo
# Receber entradas do usuário para os horários
# Organizar em uma tabela
# Mostrar com interface gráfica
from disciplina import Disciplina
from table import Table

import tkinter as tk
from tkinter import ttk
import pandas as pd

t = Table()

def handle_na(value):
    return "'" if pd.isna(value) else value

def example():
    dis = Disciplina(code_var.get(), name_var.get())

    if(dis.join_table(t) == -1):
        warning["text"] = "Código Inválido. Tente novamente"
        return
    else:
        warning["text"] = ""

    ret = t.get_table()
    columns = list(ret.columns) 
    
    for i, row in ret.iterrows():
        values = [str(i)] + [handle_na(row[col]) for col in columns]

        index = int(str(i)[0])
        if str(i)[1].lower() == 'n':
            index += 5

        result.insert("", index-1,  values=values)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Horários UNIFAP")
    window.geometry("920x580")

    code_var = tk.StringVar()
    name_var = tk.StringVar()

    code_label = tk.Label(window, text="Digite o código do horário")
    code_label.grid(column=0, row=0, padx=10, pady=10)

    code = tk.Entry(window, textvariable=code_var)
    code.grid(column=0, row=1, padx=10, pady=10)

    name_label = tk.Label(window, text="Digite o nome da disciplina")
    name_label.grid(column=0, row=2, padx=10, pady=10)

    name = tk.Entry(window, textvariable=name_var)
    name.grid(column=0, row=3, padx=10, pady=10)

    button = tk.Button(window, text="Verificar", command=example)
    button.grid(column=0, row=4, padx=10, pady=10)

    #creates the column
    result = ttk.Treeview(window)
    columns = ["Horarios"] + list(t.get_table().columns) 
    result["columns"] = columns

    for col in columns:
        result.heading(col, text=col)
        result.column(col, anchor="center", width=100)
 
    result.grid(column=0, row=5, padx=10, pady=10)

    warning = tk.Label(window, text="", foreground='red')
    warning.grid(column=0, row=6)

    window.mainloop()
