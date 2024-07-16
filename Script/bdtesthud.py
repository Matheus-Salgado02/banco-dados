import customtkinter as ctk
import banquinho as bq
from tkinter import *

def func_alterar(texto,tabela,janela):
    alterar = ctk.CTkToplevel(janela)
    alterar.title("Alterar")
    alterar.geometry("800x500")
    alterar.resizable(False,False)

    titulo = ctk.CTkLabel(alterar, text=texto, font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20, anchor="w", padx=20) 

    
    row, nomesrow = bq.select(tabela)

    # pesquisa
    # lista = list(nomesrow)

    # combobox1 = ctk.CTkComboBox(alterar, values=lista, 
    #                     fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    # combobox1.place(relx=0.3, rely=0.08, anchor="center")

    # entidade=combobox1.get()

    # combobox2 = ctk.CTkComboBox(alterar, values=["=", "<=", ">=", "<", ">"], 
    #                        fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    # combobox2.place(relx=0.48, rely=0.08, anchor="center")

    # logica=combobox1.get()

    # # print(combobox.get())  - pega resultado da combobox

    # textbox = ctk.CTkTextbox(alterar, scrollbar_button_color="#0093E9", corner_radius=4,
    #                  border_color="#0093E9", border_width=2, width=300, height=25)
    # textbox.place(relx=0.77, rely=0.08, anchor="center")

    # condicao=textbox.get()

    # tabela

    scroll = ctk.CTkScrollableFrame(alterar, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    tabela_frame = ctk.CTkFrame(scroll)
    tabela_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tabela_frame.grid_rowconfigure(0, weight=1)
    for i in range(len(row) + 1):
        tabela_frame.grid_rowconfigure(i + 1, weight=1)

    for col_num, col_name in enumerate(nomesrow):
        header_label = ctk.CTkLabel(tabela_frame, text=col_name, font=ctk.CTkFont(size=12, weight="bold"), corner_radius=0)
        header_label.grid(row=0, column=col_num, padx=1, pady=1, sticky="nsew")

        linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
        linha_canvas.grid(row=1, column=col_num, padx=1, pady=0, sticky="nsew")

    for row_num, row1 in enumerate(row):
        for col_num, value in enumerate(row1):
            cell_label = ctk.CTkLabel(tabela_frame, text=value, font=ctk.CTkFont(size=12), corner_radius=0)
            cell_label.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
        
            if row_num < len(row) - 1:
                linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
                linha_canvas.grid(row=row_num + 2, column=col_num, padx=1, pady=0, sticky="nsew")
        delete_button = ctk.CTkButton(tabela_frame, text="Excluir",command=lambda r=row1: delete_row(r, tabela,janela,alterar))
        delete_button.grid(row=row_num + 1, column=len(nomesrow), padx=5, pady=1, sticky="nsew")
    for col_num in range(len(nomesrow)):
        tabela_frame.grid_columnconfigure(col_num, weight=1)



    def delete_row(row,tabela,janela,alterar):
        id_entidade = row[0]
        bq.delete_entidade(tabela,"id","=",id_entidade)
        alterar.destroy()
        func_alterar(texto,tabela,janela)



def tabela(janela,nomesrow,row):
    scroll = ctk.CTkScrollableFrame(janela, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    tabela_frame = ctk.CTkFrame(scroll)
    tabela_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tabela_frame.grid_rowconfigure(0, weight=1)
    for i in range(len(row) + 1):
        tabela_frame.grid_rowconfigure(i + 1, weight=1)

    for col_num, col_name in enumerate(nomesrow):
        header_label = ctk.CTkLabel(tabela_frame, text=col_name, font=ctk.CTkFont(size=12, weight="bold"), corner_radius=0)
        header_label.grid(row=0, column=col_num, padx=1, pady=1, sticky="nsew")

        linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
        linha_canvas.grid(row=1, column=col_num, padx=1, pady=0, sticky="nsew")

    for row_num, row1 in enumerate(row):
        for col_num, value in enumerate(row1):
            cell_label = ctk.CTkLabel(tabela_frame, text=value, font=ctk.CTkFont(size=12), corner_radius=0)
            cell_label.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
        
            if row_num < len(row) - 1:
                linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
                linha_canvas.grid(row=row_num + 2, column=col_num, padx=1, pady=0, sticky="nsew")
    for col_num in range(len(nomesrow)):
        tabela_frame.grid_columnconfigure(col_num, weight=1)


        
