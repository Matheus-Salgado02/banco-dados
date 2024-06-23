import customtkinter as ctk

root = ctk.CTk()
root.geometry("750x550")
root.title("AdotaArvore")

title_label = ctk.CTkLabel(root,text = "Banco de dados", font=ctk.CTkFont(size=30,weight = "bold"))
title_label.pack(padx=10,pady=(40,20))

client_button = ctk.CTkButton(root,text="Adicionar Cliente",width=200,height=100)
client_button.pack(pady=20)

tree_button = ctk.CTkButton(root,text="Cadastrar Árvore",width=200,height=100)
tree_button.pack()

db_button = ctk.CTkButton(root,text="Ver banco de dados",width=200,height=100)
db_button.pack(pady=20)

root.mainloop()

