import customtkinter as ctk
import banquinho as bq
from tkinter import *
# from hud import icone
import subprocess

def func_alterar(texto,tabela,janela,row, nomesrow):
    alterar = ctk.CTkToplevel(janela)
    alterar.title("Alterar")
    alterar.geometry("1500x700")
    alterar.resizable(False,False)
    # icone(alterar)

    titulo = ctk.CTkLabel(alterar, text=texto, font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20, anchor="w", padx=20) 

    # pesquisa
    lista = list(nomesrow)

    combobox1 = ctk.CTkComboBox(alterar, values=lista,state="readonly",
                        fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox1.place(relx=0.22, rely=0.08, anchor="center")

    combobox2 = ctk.CTkComboBox(alterar, values=["=", "<=", ">=", "<", ">"],state="readonly",
                           fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox2.place(relx=0.40, rely=0.08, anchor="center")

    textbox = ctk.CTkTextbox(alterar, scrollbar_button_color="#0093E9", corner_radius=4,
                     border_color="#0093E9", border_width=2, width=300, height=25)
    textbox.place(relx=0.69, rely=0.08, anchor="center")

    # botao pesquisar
    pesquisar_button = ctk.CTkButton(alterar,text="⌕",width=30,height=30, command = lambda: pressbutton(tabela,janela))
    pesquisar_button.place(relx=0.90, rely=0.08, anchor="center")

    # tabela
    scroll = ctk.CTkScrollableFrame(alterar, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    scroll.update_idletasks()

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

    def pressbutton(tabela,janela):
        condicao = textbox.get('0.0','end')
        entidade=combobox1.get()
        logica=combobox2.get()
        
        row, nomesrow = bq.select_cond(tabela,"*",entidade,logica,condicao)
        alterar.destroy()
        func_alterar(texto,tabela,janela,row, nomesrow)

    def delete_row(row,tabela,janela,alterar):
        id_entidade = row[0]
        bq.delete_entidade(tabela,"id","=",id_entidade)
        alterar.destroy()
        row, nomesrow = bq.select(tabela)
        func_alterar(texto,tabela,janela,row, nomesrow)
    
def func_read(texto,tabela,janela,row, nomesrow):
    alterar = ctk.CTkToplevel(janela)
    alterar.title("Ler")
    alterar.geometry("1500x700")
    alterar.resizable(False,False)
    # icone(alterar)

    titulo = ctk.CTkLabel(alterar, text=texto, font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20, anchor="w", padx=20) 



    # pesquisa
    lista = list(nomesrow)

    combobox1 = ctk.CTkComboBox(alterar, values=lista, 
                        fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox1.place(relx=0.22, rely=0.08, anchor="center")

    combobox2 = ctk.CTkComboBox(alterar, values=["=", "<=", ">=", "<", ">"], 
                           fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox2.place(relx=0.40, rely=0.08, anchor="center")

    textbox = ctk.CTkTextbox(alterar, scrollbar_button_color="#0093E9", corner_radius=4,
                     border_color="#0093E9", border_width=2, width=300, height=25)
    textbox.place(relx=0.69, rely=0.08, anchor="center")

    # botao pesquisar
    pesquisar_button = ctk.CTkButton(alterar,text="⌕",width=30,height=30, command = lambda: pressbutton(tabela,janela))
    pesquisar_button.place(relx=0.90, rely=0.08, anchor="center")

    # tabela
    scroll = ctk.CTkScrollableFrame(alterar, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    scroll.update_idletasks()

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


    # tabela end

    def pressbutton(tabela,janela):
        condicao = textbox.get('0.0','end')
        entidade=combobox1.get()
        logica=combobox2.get()
        
        row, nomesrow = bq.select_cond(tabela,"*",entidade,logica,condicao)
        alterar.destroy()
        func_read(texto,tabela,janela,row, nomesrow)


def tabela(janela,nomesrow,row):
    scroll = ctk.CTkScrollableFrame(janela, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    tabela_frame = ctk.CTkFrame(scroll)
    tabela_frame.pack(pady=10, padx=10, fill="both", expand=True,anchor="e")

    # texto_protocolo = ctk.CTkLabel(janela, text="teste", font=ctk.CTkFont(size=15, weight="bold"))
    # texto_protocolo.pack(anchor = "nw",rely=1, relx=0)

    scroll.update_idletasks()
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

def tabela_superior(nomesrow,row,janela):

    lista_func = []
    row4,nomesrow4 = bq.select_cond("funcionario","id","0","=","0")
    lista_func = [str(r[0])for r in row4]
    
    scroll = ctk.CTkScrollableFrame(janela, width=1100, height=200)
    scroll.pack(pady=10, padx=10, expand=True,anchor="e",side="right")

    tabela_frame = ctk.CTkFrame(scroll)
    tabela_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

    scroll.grid_rowconfigure(0, weight=1)
    scroll.grid_columnconfigure(0, weight=1)
    
    scroll.update_idletasks()

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
            if nomesrow[col_num] == "deferido":
                cell_entry = ctk.CTkComboBox(tabela_frame, values=["0","1"],state="readonly")
                cell_entry.set(value)  # Insere o valor na caixa de texto
                cell_entry.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
            elif nomesrow[col_num] == "data_plantar":
                cell_entry2 = ctk.CTkEntry(tabela_frame, width=100)
                cell_entry2.insert(0, value)  # Insere o valor na caixa de texto
                cell_entry2.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
            elif nomesrow[col_num] == "id_funcionario":
                cell_entry3 = ctk.CTkComboBox(tabela_frame, values=lista_func,state="readonly")
                cell_entry3.set(value)  # Insere o valor na caixa de texto
                cell_entry3.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
            else:
                cell_label = ctk.CTkLabel(tabela_frame, text=value, font=ctk.CTkFont(size=12), corner_radius=0)
                cell_label.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
        
            if row_num < len(row) - 1:
                linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
                linha_canvas.grid(row=row_num + 2, column=col_num, padx=1, pady=0, sticky="nsew")
        pesquisar_button = ctk.CTkButton(tabela_frame,text="Salvar", command=lambda rn=row_num: salvar_alteracoes(rn, nomesrow, tabela_frame,janela))
        pesquisar_button.grid(row=row_num + 1, column=len(nomesrow), padx=5, pady=1, sticky="nsew")
    for col_num in range(len(nomesrow)):
        tabela_frame.grid_columnconfigure(col_num, weight=1)

def protocolo(janela,tab):
    row,nomesrow = bq.select_cond(tab,"*","deferido","=","0")
    
    
    resultados = row
    substituto_null = "0"  # Defina o valor que deseja usar no lugar de NULL
    linha = [
    [substituir_null(valor, substituto_null) for valor in row]
    for row in resultados]
    
    tabela_superior(nomesrow,linha,janela)
    
   
    
def substituir_null(valor, substituto):
        return substituto if valor is None else valor


def salvar_alteracoes(row_num, nomesrow, tabela_frame,janela):
    valores = {}
    
    for col_num, col_name in enumerate(nomesrow):
        widget = tabela_frame.grid_slaves(row=row_num + 1, column=col_num)[0]
        
        if isinstance(widget, ctk.CTkEntry):
            valores[col_name] = widget.get()
        elif isinstance(widget, ctk.CTkComboBox):
            valores[col_name] = widget.get()
        elif isinstance(widget, ctk.CTkLabel):
            valores[col_name] = widget.cget("text")
    
    set_clause = ', '.join([f"{nome} = '{valor}'" for nome, valor in valores.items()])
    condicao =f"{valores.get('id')}"
    bq.update("protocolo", set_clause, "id", "=", condicao)
    janela.destroy()
    subprocess.run(["python", "hud.py"])
    

def atualizar(texto,tabela,janela,row, nomesrow):


    alterar = ctk.CTkToplevel(janela)
    alterar.title("Alterar")
    alterar.geometry("1500x700")
    alterar.resizable(False,False)
    # icone(alterar)

    titulo = ctk.CTkLabel(alterar, text=texto, font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20, anchor="w", padx=20) 

    # pesquisa
    lista = list(nomesrow)

    combobox1 = ctk.CTkComboBox(alterar, values=lista,state="readonly",
                        fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox1.place(relx=0.22, rely=0.08, anchor="center")

    combobox2 = ctk.CTkComboBox(alterar, values=["=", "<=", ">=", "<", ">"],state="readonly",
                           fg_color="#0093E9", border_color="#FBAB7E", dropdown_fg_color="#0093E9")
    combobox2.place(relx=0.40, rely=0.08, anchor="center")

    textbox = ctk.CTkTextbox(alterar, scrollbar_button_color="#0093E9", corner_radius=4,
                     border_color="#0093E9", border_width=2, width=300, height=25)
    textbox.place(relx=0.69, rely=0.08, anchor="center")

    # botao pesquisar
    pesquisar_button = ctk.CTkButton(alterar,text="⌕",width=30,height=30, command = lambda: pressbutton(tabela,janela))
    pesquisar_button.place(relx=0.90, rely=0.08, anchor="center")

    # tabela
    scroll = ctk.CTkScrollableFrame(alterar, width=1100, height=500)
    scroll.pack(pady=10, padx=10, fill="both", expand=True)

    scroll.update_idletasks()

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
            cell_entry2 = ctk.CTkEntry(tabela_frame, width=100)
            cell_entry2.insert(0, value)  # Insere o valor na caixa de texto
            cell_entry2.grid(row=row_num + 1, column=col_num, padx=1, pady=1, sticky="nsew")
        
            if row_num < len(row) - 1:
                linha_canvas = ctk.CTkCanvas(tabela_frame, height=1, bg="gray")
                linha_canvas.grid(row=row_num + 2, column=col_num, padx=1, pady=0, sticky="nsew")
        pesquisar_button = ctk.CTkButton(tabela_frame,text="Salvar", command=lambda rn=row_num: update_alteracoes(rn, nomesrow, tabela_frame,tabela,janela))
        pesquisar_button.grid(row=row_num + 1, column=len(nomesrow), padx=5, pady=1, sticky="nsew")
    for col_num in range(len(nomesrow)):
        tabela_frame.grid_columnconfigure(col_num, weight=1)

    def pressbutton(tabela,janela):
        condicao = textbox.get('0.0','end')
        entidade=combobox1.get()
        logica=combobox2.get()
        
        row, nomesrow = bq.select_cond(tabela,"*",entidade,logica,condicao)
        alterar.destroy()
        atualizar(texto,tabela,janela,row, nomesrow)


    def update_alteracoes(row_num, nomesrow, tabela_frame,tab,janela):
        valores = {}
        
        for col_num, col_name in enumerate(nomesrow):
            widget = tabela_frame.grid_slaves(row=row_num + 1, column=col_num)[0]

            if isinstance(widget, ctk.CTkEntry):
                valores[col_name] = widget.get() 
        set_clause = ', '.join([f"{nome} = '{valor}'" for nome, valor in valores.items()])
        condicao =f"{valores.get('id')}"
        # print(set_clause)
        # print(condicao)
        bq.update(tab, set_clause, "id", "=", condicao)
        row, nomesrow = bq.select_cond(tabela,"*","1","=","1")
        alterar.destroy()
        atualizar(texto,tabela,janela,row, nomesrow)
    
    