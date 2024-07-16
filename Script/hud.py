import customtkinter as ctk
import banquinho as bq
from tkinter import messagebox
import bdtesthud as bdt

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
            latitude_info = latitude.get("1.0", "end-1c")
            longitude_info = longitude.get("1.0", "end-1c")
            especie_info = especie.get("1.0","end-1c")
            locais_info = locais.get("1.0","end-1c")
            cliente_info = cliente.get("1.0","end-1c")
           
            bq.insert_arvore(cliente_info, especie_info, locais_info, latitude_info, longitude_info)
            arvore.destroy()

        
        
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
            nome_info = nome.get("1.0", "end-1c")
            descricao_info = descricao.get("1.0", "end-1c")
            expectativa_vida_info = expectativa_vida.get("1.0", "end-1c")
            nome_cientifico_info = nome_cientifico.get("1.0", "end-1c")
            bq.insert_especie(nome_info,descricao_info,expectativa_vida_info,nome_cientifico_info)
            especie.destroy()

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
            nome_get = nome.get("1.0","end-1c")
            descricao_get = descricao.get("1.0","end-1c")

            bq.insert_bioma(nome_get, descricao_get)
            bioma.destroy()

       
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
            nome_info = nome.get("1.0", "end-1c")
            sigla_info = sigla.get("1.0", "end-1c")
            bq.insert_uf(nome_info,sigla_info)
            uf.destroy()

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
            bairro_info = bairro.get("1.0", "end-1c")
            cidade_info = cidade.get("1.0", "end-1c")
            complemento_info = complemento.get("1.0","end-1c")
            numero_info = numero.get("1.0","end-1c")
            rua_info = rua.get("1.0","end-1c")
            uf_info = uf.get("1.0", "end-1c")
            bioma_info = bioma.get("1.0", "end-1c")
            nome_info = nome.get("1.0","end-1c")
            descricao_info = descricao.get("1.0","end-1c")
            croqui_info = croqui.get("1.0","end-1c")
            area_total_info = area_total.get("1.0","end-1c")
            tipo_plantio_info = tipo_plantio.get("1.0","end-1c")
            bq.insert_locais(bairro_info, cidade_info, complemento_info, numero_info, rua_info,uf_info, bioma_info, nome_info, descricao_info, croqui_info, area_total_info, tipo_plantio_info)

            local.destroy()

        
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
            reserva_legal_info = reserva_legal.get("1.0","end-1c")
            APPs_info = APPs.get("1.0","end-1c")
            uso_da_terra_info = uso_da_terra.get("1.0","end-1c")
            local_info = local.get("1.0","end-1c")
            bq.insert_car(reserva_legal_info, APPs_info, uso_da_terra_info, local_info)
            CAR.destroy()

       
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
            nome_info = nome.get("1.0","end-1c")
            cpf_info = cpf.get("1.0","end-1c")
            cidade_info = cidade.get("1.0","end-1c")
            bairro_info = bairro.get("1.0","end-1c")
            complemento_info = complemento.get("1.0","end-1c")
            numero_info = numero.get("1.0","end-1c")
            rua_info = rua.get("1.0","end-1c")
            uf_info = uf.get("1.0","end-1c")
            data_nascimento_info = data_nascimento.get("1.0","end-1c")
            bq.insert_funcinario(nome_info, bairro_info, cidade_info, complemento_info, numero_info, rua_info, cpf_info, uf_info, data_nascimento_info)
            funcionario.destroy()

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
            bairro_info = bairro.get("1.0", "end-1c")
            cidade_info = cidade.get("1.0", "end-1c")
            complemento_info = complemento.get("1.0","end-1c")
            numero_info = numero.get("1.0","end-1c")
            rua_info = rua.get("1.0","end-1c")
            uf_info = uf.get("1.0", "end-1c")
            cpf_info = cpf.get("1.0", "end-1c")
            nome_info = nome.get("1.0","end-1c")
            telefone_info = telefone.get("1.0","end-1c")
            email_info = email.get("1.0","end-1c")
            bq.insert_cliente(nome_info, bairro_info, cidade_info, complemento_info, numero_info, rua_info, cpf_info,uf_info,telefone_info,email_info)
            cliente.destroy()

        
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

    def func_bioma_especie():
        bioma_especie = ctk.CTkToplevel(root)
        bioma_especie.title("Bioma/Especie")
        bioma_especie.geometry("400x320")

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
            id_bioma_info = id_bioma.get("1.0","end-1c")
            id_especie_info = id_especie.get("1.0","end-1c")

            bq.insert_bioma_especie(id_bioma_info, id_especie_info)
            bioma_especie.destroy()

       
        id_bioma = criar_linha(bioma_especie, "Id Bioma:")
        id_especie = criar_linha(bioma_especie, "Id Especie:")

        salvar = ctk.CTkButton(bioma_especie, text="Salvar", command=salvar_informacoes)
        salvar.pack(pady=10)


    nova = ctk.CTkToplevel(root)
    nova.title("Inserir")
    nova.geometry("400x500")
    nova.resizable(False, False) 

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

    bioma_especie_botao = ctk.CTkButton(scroll,text="Cliente",width=200,height=50,command = func_bioma_especie)
    bioma_especie_botao.pack(pady=20)

def atualizar():

    def abrir_alterar_arvore():
        bdt.func_alterar("Alterar arvore","arvore",nova)


    def alterar_uf():
        bdt.func_alterar("Alterar UF","uf",nova)
        

    def alterar_especie():
        bdt.func_alterar("Alterar Especie","especie",nova)

    def alterar_bioma():
        bdt.func_alterar("Alterar Bioma","bioma",nova)

    def alterar_local():
        bdt.func_alterar("Alterar Local","locais",nova)

    def alterar_car():
        bdt.func_alterar("Alterar CAR","CAR",nova)

    def alterar_func():
        bdt.func_alterar("Alterar Funcionario","funcionario",nova)

    def alterar_cliente():
        bdt.func_alterar("Alterar Cliente","cliente",nova)

    def alterar_bioma_especie():
        bdt.func_alterar("Alterar Bioma/Especie","bioma_especie",nova)


    

    nova = ctk.CTkToplevel(root)
    nova.title("Atualizar/Excluir")
    nova.geometry("400x500")
    nova.resizable(False, False) 

    titulo = ctk.CTkLabel(nova, text="Alterar Informações", font=ctk.CTkFont(size=30, weight="bold"))
    titulo.pack(padx=10, pady=(40, 20))

    scroll = ctk.CTkScrollableFrame(nova,width=700, height=400)
    scroll.pack(pady=10)

    arvore_botao = ctk.CTkButton(scroll,text="Arvore",width=200,height=50,command=abrir_alterar_arvore)
    arvore_botao.pack(pady=20)

    especie_botao = ctk.CTkButton(scroll,text="Especie",width=200,height=50,command = alterar_especie)
    especie_botao.pack(pady=20)

    bioma_botao = ctk.CTkButton(scroll,text="Bioma",width=200,height=50,command=alterar_bioma)
    bioma_botao.pack(pady=20)

    uf_botao = ctk.CTkButton(scroll,text="UF",width=200,height=50,command= alterar_uf)
    uf_botao.pack(pady=20)

    local_botao = ctk.CTkButton(scroll,text="Local",width=200,height=50,command=alterar_local)
    local_botao.pack(pady=20)

    CAR_botao = ctk.CTkButton(scroll,text="CAR",width=200,height=50, command = alterar_car)
    CAR_botao.pack(pady=20)

    func_botao = ctk.CTkButton(scroll,text="Funcionario",width=200,height=50,command = alterar_func)
    func_botao.pack(pady=20)

    cliente_botao = ctk.CTkButton(scroll,text="Cliente",width=200,height=50,command=alterar_cliente)
    cliente_botao.pack(pady=20)

    bioma_especie_botao = ctk.CTkButton(scroll,text="Bioma/Especuie",width=200,height=50,command=alterar_bioma_especie)
    bioma_especie_botao.pack(pady=20)

def consultar():
    nova = ctk.CTkToplevel(root)
    nova.title("Consultar")
    nova.geometry("400x500")
    nova.resizable(False, False) 

    titulo = ctk.CTkLabel(nova,text = "Consultas", font=ctk.CTkFont(size=30,weight = "bold"))
    titulo.pack(padx=10,pady=(40,20))

    botao_protocolo = ctk.CTkButton(nova,text="Protocolo",width=200,height=50,command = consulta_protocolo)
    botao_protocolo.pack(pady=20)

    botao_arvore = ctk.CTkButton(nova,text="Quantidade árvores por local",width=200,height=50,command = consultar_qtd_arvore)
    botao_arvore.pack(pady=20)



def consulta_protocolo():
    # titulo = ctk.CTkLabel(nova,text = "Visualização dos protocolos criados", font=ctk.CTkFont(size=30,weight = "bold"))
    # titulo.pack(padx=10,pady=(40,20))
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1200x500")
    nova.resizable(False, False) 
    row,nomesrow=bq.select("protocoloview") 
    bdt.tabela(nova,nomesrow,row)

def consultar_qtd_arvore():
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1200x500")
    nova.resizable(False, False) 
    row,nomesrow=bq.select("qtdarvoreslocalview") 
    bdt.tabela(nova,nomesrow,row)

root = ctk.CTk()
root.geometry("750x550")
root.title("AdotaArvore")
root.resizable(False, False) 

ctk.set_default_color_theme("green")

title_label = ctk.CTkLabel(root,text = "Banco de dados", font=ctk.CTkFont(size=30,weight = "bold"))
title_label.pack(padx=10,pady=(40,20))

client_button = ctk.CTkButton(root,text="Inserir",width=200,height=50, command = inserir)
client_button.pack(pady=20)

db_button = ctk.CTkButton(root,text="Excluir",width=200,height=50, command=atualizar)
db_button.pack(pady=20)

db_button = ctk.CTkButton(root,text="Consultar",width=200,height=50, command=consultar)
db_button.pack(pady=20)

root.mainloop()
