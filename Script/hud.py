import customtkinter as ctk
import banquinho as bq
from tkinter import messagebox
import bdtesthud as bdt
import tkinter as tk
from datetime import date



def icone(janela):
    janela.after(250, lambda: janela.iconbitmap('OIP.ico'))



root = ctk.CTk()
root.geometry("1000x550")
root.title("AdotaArvore")
root.resizable(False, False) 
icone(root)


ctk.set_default_color_theme("green")

def inserir():
    def func_arvore():
        arvore = ctk.CTkToplevel(root)
        arvore.title("Árvore")
        arvore.geometry("400x320")
        icone(arvore)
       
        
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
        icone(especie)

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
        icone(bioma)

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
        icone(uf)

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
        icone(local)

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
        icone(CAR)

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
        icone(funcionario)

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
        icone(cliente)

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
        icone(bioma_especie)

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
    icone(nova)

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
        row, nomesrow = bq.select("arvore")
        bdt.func_alterar("Alterar arvore","arvore",nova,row, nomesrow)

    def alterar_uf():
        row, nomesrow = bq.select("uf")
        bdt.func_alterar("Alterar UF","uf",nova,row, nomesrow)

    def alterar_especie():
        row, nomesrow = bq.select("especie")
        bdt.func_alterar("Alterar Especie","especie",nova,row, nomesrow)

    def alterar_bioma():
        row, nomesrow = bq.select("bioma")
        bdt.func_alterar("Alterar Bioma","bioma",nova,row, nomesrow)

    def alterar_local():
        row, nomesrow = bq.select("locais")
        bdt.func_alterar("Alterar Local","locais",nova,row, nomesrow)

    def alterar_car():
        row, nomesrow = bq.select("car")
        bdt.func_alterar("Alterar CAR","CAR",nova,row, nomesrow)

    def alterar_func():
        row, nomesrow = bq.select("funcionario")
        bdt.func_alterar("Alterar Funcionario","funcionario",nova,row, nomesrow)

    def alterar_cliente():
        row, nomesrow = bq.select("cliente")
        bdt.func_alterar("Alterar Cliente","cliente",nova,row, nomesrow)

    def alterar_bioma_especie():
        row, nomesrow = bq.select("bioma_especie")
        bdt.func_alterar("Alterar Bioma/Especie","bioma_especie",nova,row, nomesrow)


    

    nova = ctk.CTkToplevel(root)
    nova.title("Excluir")
    nova.geometry("400x500")
    nova.resizable(False, False) 
    icone(nova)

    titulo = ctk.CTkLabel(nova, text="Excluir Informações", font=ctk.CTkFont(size=30, weight="bold"))
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
    icone(nova)

    titulo = ctk.CTkLabel(nova,text = "Views", font=ctk.CTkFont(size=30,weight = "bold"))
    titulo.pack(padx=10,pady=(40,20))

    scroll = ctk.CTkScrollableFrame(nova,width=700, height=400)
    scroll.pack(pady=10)

    # Views
    botao_protocolo = ctk.CTkButton(scroll,text="Protocolo",width=200,height=50,command = consulta_protocolo)
    botao_protocolo.pack(pady=20)

    botao_arvore2 = ctk.CTkButton(scroll,text="Arvore Informações",width=200,height=50,command = consultar_ArvInformacao)
    botao_arvore2.pack(pady=20)

    # Views Select ArvInformacao
    botao_arvore = ctk.CTkButton(scroll,text="Clientes com mais Árvores",width=200,height=50,command = consultar_ClienteArvore)
    botao_arvore.pack(pady=20)

    botao_arvore = ctk.CTkButton(scroll,text="Árvores em parques",width=200,height=50,command = consultar_funcArvore)
    botao_arvore.pack(pady=20)

    # Views Select Protocolo

    botao_arvore = ctk.CTkButton(scroll,text="Protocolos mensal",width=200,height=50,command = consultar_prot_mes)
    botao_arvore.pack(pady=20)

    botao_arvore = ctk.CTkButton(scroll,text="Funcionários com mais deferidos",width=200,height=50,command = consultar_prot_func)
    botao_arvore.pack(pady=20)



def func_read():
    nova = ctk.CTkToplevel(root)
    nova.title("Read")
    nova.geometry("400x500")
    nova.resizable(False, False)
    icone(nova)

    def abrir_read_arvore():
        row, nomesrow = bq.select("arvore")
        bdt.func_read("Arvore","arvore",nova,row, nomesrow)

    def read_uf():
        row, nomesrow = bq.select("uf")
        bdt.func_read("UF","uf",nova,row, nomesrow)

    def read_especie():
        row, nomesrow = bq.select("especie")
        bdt.func_read("Especie","especie",nova,row, nomesrow)

    def read_bioma():
        row, nomesrow = bq.select("bioma")
        bdt.func_read("Bioma","bioma",nova,row, nomesrow)

    def read_local():
        row, nomesrow = bq.select("locais")
        bdt.func_read("Local","locais",nova,row, nomesrow)

    def read_car():
        row, nomesrow = bq.select("car")
        bdt.func_read("CAR","CAR",nova,row, nomesrow)

    def read_func():
        row, nomesrow = bq.select("funcionario")
        bdt.func_read("Funcionario","funcionario",nova,row, nomesrow)

    def read_cliente():
        row, nomesrow = bq.select("cliente")
        bdt.func_read("Cliente","cliente",nova,row, nomesrow)

    def read_bioma_especie():
        row, nomesrow = bq.select("bioma_especie")
        bdt.func_read("Bioma/Especie","bioma_especie",nova,row, nomesrow)

    titulo = ctk.CTkLabel(nova, text="Ver Informações", font=ctk.CTkFont(size=30, weight="bold"))
    titulo.pack(padx=10, pady=(40, 20))

    scroll = ctk.CTkScrollableFrame(nova,width=700, height=400)
    scroll.pack(pady=10)

    arvore_botao = ctk.CTkButton(scroll,text="Arvore",width=200,height=50,command=abrir_read_arvore)
    arvore_botao.pack(pady=20)

    especie_botao = ctk.CTkButton(scroll,text="Especie",width=200,height=50,command = read_especie)
    especie_botao.pack(pady=20)

    bioma_botao = ctk.CTkButton(scroll,text="Bioma",width=200,height=50,command=read_bioma)
    bioma_botao.pack(pady=20)

    uf_botao = ctk.CTkButton(scroll,text="UF",width=200,height=50,command= read_uf)
    uf_botao.pack(pady=20)

    local_botao = ctk.CTkButton(scroll,text="Local",width=200,height=50,command=read_local)
    local_botao.pack(pady=20)

    CAR_botao = ctk.CTkButton(scroll,text="CAR",width=200,height=50, command = read_car)
    CAR_botao.pack(pady=20)

    func_botao = ctk.CTkButton(scroll,text="Funcionario",width=200,height=50,command = read_func)
    func_botao.pack(pady=20)

    cliente_botao = ctk.CTkButton(scroll,text="Cliente",width=200,height=50,command=read_cliente)
    cliente_botao.pack(pady=20)

    bioma_especie_botao = ctk.CTkButton(scroll,text="Bioma/Especuie",width=200,height=50,command=read_bioma_especie)
    bioma_especie_botao.pack(pady=20)

    
def consulta_protocolo():
    
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1200x500")
    nova.resizable(False, False) 
    row, nomesrow = bq.select("protocoloview") 
    bdt.tabela(nova, nomesrow, row)
    icone(nova)
    texto = ctk.CTkLabel(nova, text=""" View contendo informações das árvores e os seus relacionados. """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    

def consultar_prot_mes():
   
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1500x500")
    nova.resizable(False, False)
    texto = ctk.CTkLabel(nova, text=""" Protocolos deferidos do mes atual """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    data_atual = date.today()
    data_mes=data_atual.month
    data_ano = data_atual.year
    row,nomesrow=bq.select_comando(f"""SELECT protocoloview.ID_Cli AS ID_Cliente, protocoloview.ID_Arvore AS ID_Arvore, protocoloview.NomeCli AS NomeCliente,
                                   protocoloview.Prot_id AS ID_Protocolo,protocoloview.cidade AS Cidade, protocoloview.Estado AS Estado, protocoloview.LocalArvore 
                                   AS LocalPlantado,  protocoloview.DT_plant AS Data_Plant FROM protocoloview WHERE YEAR(protocoloview.DT_plant) = {data_ano} 
                                   AND MONTH(protocoloview.DT_plant) = {data_mes};""") 
    bdt.tabela(nova,nomesrow,row)
    icone(nova)


def consultar_ArvInformacao():
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1500x500")
    nova.resizable(False, False)
    texto = ctk.CTkLabel(nova, text=""" View contendo informações das árvores e os seus relacionados. """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    row,nomesrow=bq.select("arvoreinformacao") 
    bdt.tabela(nova,nomesrow,row)
    icone(nova)

def consultar_ClienteArvore():
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1200x500")
    nova.resizable(False, False)
    texto = ctk.CTkLabel(nova, text=""" Esta consulta informa a quantidade de árvores plantadas por cliente, ordenado de maneira decrescente.Assim, sistem de bonificação 
                                   presenteia o cliente que mais ajudou o meio-ambiente. """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    row,nomesrow=bq.select_comando("SELECT DISTINCT arvoreinformacao.id_cliente, arvoreinformacao.nome_cliente, cliente.cpf, cliente.cidade As Cidade_Cliente, \
        arvoreinformacao.cli_tel, arvoreinformacao.cli_email, COUNT(*) As Qtd_Arvores FROM arvoreinformacao INNER JOIN cliente on \
        cliente.id = arvoreinformacao.id_cliente GROUP BY arvoreinformacao.id_cliente ORDER BY COUNT(*) DESC;")
    bdt.tabela(nova,nomesrow,row)
    icone(nova)
    

def consultar_funcArvore():
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1500x500")
    nova.resizable(False, False)
    texto = ctk.CTkLabel(nova, text=""" Informações de árvores plantadas em parques. Estes são os locais no qual o cliente pode visitar sem a necessidade de uma permissão. """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    row,nomesrow =bq.select_comando("""SELECT arvoreinformacao.id As Arvore_id, arvoreinformacao.cord_latitude, arvoreinformacao.cord_longitude, arvoreinformacao.id_especie, 
        arvoreinformacao.nome_especie, arvoreinformacao.id_locais, arvoreinformacao.Estado , arvoreinformacao.nome_local FROM arvoreinformacao 
        WHERE arvoreinformacao.nome_local LIKE "%Parque%";""")
    bdt.tabela(nova,nomesrow,row)
    icone(nova)
    

def consultar_prot_func():
    nova = ctk.CTkToplevel(root)
    nova.title("View")
    nova.geometry("1500x500")
    nova.resizable(False, False)
    texto = ctk.CTkLabel(nova, text=""" Informações de quais funcionarios mais plantaram e tiveram protocolos deferidos. """, font=ctk.CTkFont(size=15, weight="bold"))
    texto.pack(pady=20)
    row,nomesrow =bq.select_comando("""SELECT DISTINCT protocoloview.ID_Func, protocoloview.NomeFunc, funcionario.cpf, funcionario.cidade As Cidade_func, 
                                    funcionario.data_nascimento, COUNT(*) AS Qtd_arvores_plantadas FROM protocoloview 
                                    INNER JOIN funcionario on funcionario.id = protocoloview.ID_Func WHERE Deferido = 1 GROUP BY protocoloview.NomeFunc;""")
    bdt.tabela(nova,nomesrow,row)
    icone(nova)

    



def func_update():
   
    def abrir_alterar_arvore():
        row, nomesrow = bq.select("arvore")
        bdt.atualizar("Árvore","arvore",nova,row,nomesrow)

    def alterar_uf():
       row, nomesrow = bq.select("uf")
       bdt.atualizar("UF","uf",nova,row,nomesrow)

    def alterar_especie():
        row, nomesrow = bq.select("especie")
        bdt.atualizar("Especie","especie",nova,row,nomesrow)

    def alterar_bioma():
        row, nomesrow = bq.select("bioma")
        bdt.atualizar("Bioma","bioma",nova,row,nomesrow)

    def alterar_local():
        row, nomesrow = bq.select("locais")
        bdt.atualizar("Locais","locais",nova,row,nomesrow)

    def alterar_car():
        row, nomesrow = bq.select("car")
        bdt.atualizar("Alterar CAR","CAR",nova,row, nomesrow)

    def alterar_func():
        row, nomesrow = bq.select("funcionario")
        bdt.atualizar("Alterar Funcionario","funcionario",nova,row, nomesrow)

    def alterar_cliente():
        row, nomesrow = bq.select("cliente")
        bdt.atualizar("Alterar Cliente","cliente",nova,row, nomesrow)

    def alterar_bioma_especie():
        row, nomesrow = bq.select("bioma_especie")
        bdt.atualizar("Alterar Bioma/Especie","bioma_especie",nova,row, nomesrow)   
   
    nova = ctk.CTkToplevel(root)
    nova.title("Atualizar")
    nova.geometry("400x500")
    nova.resizable(False, False) 
    icone(nova)

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



title_label = ctk.CTkLabel(root, text="Banco de dados", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20),anchor="n")

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20, padx=60, anchor='n')

client_button = ctk.CTkButton(button_frame, text="Inserir", width=130, height=50, command=inserir)
client_button.pack(side='left', padx=5)

db_button1 = ctk.CTkButton(button_frame, text="Excluir", width=130, height=50, command=atualizar)
db_button1.pack(side='left', padx=5)

db_button2 = ctk.CTkButton(button_frame, text="Views", width=130, height=50, command=consultar)
db_button2.pack(side='left', padx=5)

db_button3 = ctk.CTkButton(button_frame, text="Ver Tabelas", width=130, height=50, command=func_read)
db_button3.pack(side='left', padx=5)

db_button3 = ctk.CTkButton(button_frame, text="Update", width=130, height=50, command=func_update)
db_button3.pack(side='left', padx=5)

texto_protocolo = ctk.CTkLabel(root, text="Protocolos não deferidos", font=ctk.CTkFont(size=20, weight="bold"))
texto_protocolo.place(rely=0.45, anchor='w') 

bdt.protocolo(root,"protocolo")


root.mainloop()
