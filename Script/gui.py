import customtkinter as ctk
from tkinter import messagebox

def inserir():

    def func_arvore():
        arvore = ctk.CTkToplevel(root)
        arvore.title("Árvore")
        arvore.geometry("400x320")

        
        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=100)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

       
        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            arvore.destroy()

        
        id = criar_linha(arvore, "ID:")
        latitude = criar_linha(arvore, "Latitude:")
        longitude = criar_linha(arvore, "Longitude:")
        especie = criar_linha(arvore, "Especie:")
        locais = criar_linha(arvore, "Local:")
        cliente = criar_linha(arvore, "Cliente:")

        salvar = ctk.CTkButton(arvore, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_especie():
        especie = ctk.CTkToplevel(root)
        especie.title("Espécie")
        especie.geometry("400x400")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=100)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            especie.destroy()

        id = criar_linha(especie, "ID:")
        nome = criar_linha(especie, "Nome:")
        descricao = criar_linha(especie, "Descrição:")
        expectativa_vida = criar_linha(especie, "Expec de vida:")
        nome_cientifico = criar_linha(especie, "Nome Científico:")

        salvar = ctk.CTkButton(especie, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_bioma():
        bioma = ctk.CTkToplevel(root)
        bioma.title("Bioma")
        bioma.geometry("400x320")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=100)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            bioma.destroy()

        id = criar_linha(bioma, "ID:")
        nome = criar_linha(bioma, "Nome:")
        descricao = criar_linha(bioma, "Descrição:")

        salvar = ctk.CTkButton(bioma, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_uf():
        uf = ctk.CTkToplevel(root)
        uf.title("UF")
        uf.geometry("400x320")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=100)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            nome_info = nome.get()
            uf.destroy()
        
        id = criar_linha(uf, "ID:")
        nome = criar_linha(uf, "Nome:")
        sigla = criar_linha(uf, "Sigla:")

        salvar = ctk.CTkButton(uf, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_local():
        local = ctk.CTkToplevel(root)
        local.title("Local")
        local.geometry("400x600")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=100)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            local.destroy()

        id = criar_linha(local, "ID:")
        nome = criar_linha(local, "Nome:")
        cidade = criar_linha(local, "Cidade:")
        bairro = criar_linha(local, "Bairro:")
        numero = criar_linha(local, "Numero:")
        rua = criar_linha(local, "Rua:")
        complemento = criar_linha(local, "Complemento:")
        uf = criar_linha(local, "UF:")
        bioma = criar_linha(local, "Bioma:")
        descricao = criar_linha(local, "Descrição:")
        croqui = criar_linha(local, "Croqui:")
        tipo_plantio = criar_linha(local, "Tipo de Plantio:")
        area_total = criar_linha(local, "Área Total:")

        salvar = ctk.CTkButton(local, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_CAR():
        CAR = ctk.CTkToplevel(root)
        CAR.title("CAR")
        CAR.geometry("400x400")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=150)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            CAR.destroy()

        id = criar_linha(CAR, "ID:")
        reserva_legal = criar_linha(CAR, "Reserva Legal:")
        APPs = criar_linha(CAR, "APPs:")
        uso_da_terra = criar_linha(CAR, "Uso da Terra:")
        local = criar_linha(CAR, "Local:")

        salvar = ctk.CTkButton(CAR, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)

    def func_funcionario():
        funcionario = ctk.CTkToplevel(root)
        funcionario.title("Funcionário")
        funcionario.geometry("400x500")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=150)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            funcionario.destroy()

        id = criar_linha(funcionario, "ID:")
        nome = criar_linha(funcionario, "Nome:")
        cpf = criar_linha(funcionario, "CPF:")
        cidade = criar_linha(funcionario, "Cidade:")
        bairro = criar_linha(funcionario, "Bairro:")
        numero = criar_linha(funcionario, "Número:")
        rua = criar_linha(funcionario, "Rua:")
        data_nascimento = criar_linha(funcionario, "Data de Nascimento:")
        uf = criar_linha(funcionario, "UF:")
        complemento = criar_linha(funcionario, "Complemento:")

        salvar = ctk.CTkButton(funcionario, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)
    
    def func_cliente():
        cliente = ctk.CTkToplevel(root)
        cliente.title("Cliente")
        cliente.geometry("400x500")

        def criar_linha(parent, texto_label):
            frame = ctk.CTkFrame(parent)
            frame.pack(pady=5, fill='x', padx=10)
            
            frame_inner = ctk.CTkFrame(frame)
            frame_inner.pack(fill='x')

            label = ctk.CTkLabel(frame_inner, text=texto_label, width=150)
            label.pack(side='left', padx=5)

            textbox = ctk.CTkTextbox(frame_inner, width=200, height=25)
            textbox.pack(side='left', padx=5)
            
            return textbox

        def salvar_informacoes():
            messagebox.showinfo("Notificação", "Informações salvas")
            cliente.destroy()

        id = criar_linha(cliente, "ID:")
        nome = criar_linha(cliente, "Nome:")
        cpf = criar_linha(cliente, "CPF:")
        cidade = criar_linha(cliente, "Cidade:")
        bairro = criar_linha(cliente, "Bairro:")
        numero = criar_linha(cliente, "Número:")
        complemento = criar_linha(cliente, "Complemento:")
        rua = criar_linha(cliente, "Rua:")
        uf = criar_linha(cliente, "UF:")
        telefone = criar_linha(cliente, "Telefone:")
        email = criar_linha(cliente, "Email:")

        salvar = ctk.CTkButton(cliente, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)


    nova = ctk.CTkToplevel(root)
    nova.title("Inserir")
    nova.geometry("400x500")

    titulo = ctk.CTkLabel(nova,text = "Escolha uma tabela", font=ctk.CTkFont(size=30,weight = "bold"))
    titulo.pack(padx=10,pady=(40,20))

    scroll = ctk.CTkScrollableFrame(nova,width=700, height=400)
    scroll.pack(pady=10)

    arvore_botao = ctk.CTkButton(scroll,text="Arvore",width=200,height=50,command = func_arvore)
    arvore_botao.pack(pady=20)

    especie_botao = ctk.CTkButton(scroll,text="Especie",width=200,height=50, command = func_especie)
    especie_botao.pack(pady=20)

    bioma_botao = ctk.CTkButton(scroll,text="Bioma",width=200,height=50, command = func_bioma)
    bioma_botao.pack(pady=20)

    uf_botao = ctk.CTkButton(scroll,text="UF",width=200,height=50, command = func_uf)
    uf_botao.pack(pady=20)

    local_botao = ctk.CTkButton(scroll,text="Local",width=200,height=50,command = func_local)
    local_botao.pack(pady=20)

    CAR_botao = ctk.CTkButton(scroll,text="CAR",width=200,height=50,command = func_CAR)
    CAR_botao.pack(pady=20)

    func_botao = ctk.CTkButton(scroll,text="Funcionario",width=200,height=50,command = func_funcionario)
    func_botao.pack(pady=20)

    cliente_botao = ctk.CTkButton(scroll,text="Cliente",width=200,height=50,command = func_cliente)
    cliente_botao.pack(pady=20)

    

root = ctk.CTk()
root.geometry("750x550")
root.title("AdotaArvore")
root.resizable(False, False) 

ctk.set_default_color_theme("green")

title_label = ctk.CTkLabel(root,text = "Banco de dados", font=ctk.CTkFont(size=30,weight = "bold"))
title_label.pack(padx=10,pady=(40,20))

client_button = ctk.CTkButton(root,text="Inserir",width=200,height=50, command = inserir)
client_button.pack(pady=20)

tree_button = ctk.CTkButton(root,text="Excluir",width=200,height=50)
tree_button.pack(pady=20)

db_button = ctk.CTkButton(root,text="Atualizar",width=200,height=50)
db_button.pack(pady=20)

db_button = ctk.CTkButton(root,text="Consultar",width=200,height=50)
db_button.pack(pady=20)

root.mainloop()

