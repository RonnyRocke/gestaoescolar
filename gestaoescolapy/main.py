import tkinter as tk
import cadastro_aluno
import adicao_notas
import visualizacao_notas

def cadastrar_aluno():
    cadastro_aluno.cadastrar_aluno_interface()

def adicionar_nota():
    adicao_notas.adicionar_nota_interface()

def visualizar_notas():
    visualizacao_notas.visualizar_notas_interface()

root = tk.Tk()
root.title("Sistema Escolar")
root.geometry("400x200+400+200")  

cadastrar_button = tk.Button(root, text="Cadastrar Aluno", command=cadastrar_aluno)
cadastrar_button.pack()

adicionar_button = tk.Button(root, text="Adicionar Nota", command=adicionar_nota)
adicionar_button.pack()

visualizar_button = tk.Button(root, text="Visualizar Notas", command=visualizar_notas)
visualizar_button.pack()

root.mainloop()
