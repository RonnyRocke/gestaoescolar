import tkinter as tk
from tkinter import messagebox
import mysql.connector

def adicionar_nota(matricula, nome_aluno, disciplina, nota):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escola"
        )
        cursor = connection.cursor()

        query = "INSERT INTO notas (matricula_aluno, nome_aluno, disciplina, nota) VALUES (%s, %s, %s, %s)"
        values = (matricula, nome_aluno, disciplina, nota)
        cursor.execute(query, values)

        connection.commit()
        messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar nota: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def adicionar_nota_interface():
    root = tk.Tk()
    root.title("Adição de Nota")
    root.geometry("400x200+400+200")  # Mesmo tamanho da tela de cadastro de aluno

    tk.Label(root, text="Matrícula do Aluno:").pack()
    matricula_entry = tk.Entry(root)
    matricula_entry.pack()

    tk.Label(root, text="Nome do Aluno:").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    tk.Label(root, text="Disciplina:").pack()
    disciplina_entry = tk.Entry(root)
    disciplina_entry.pack()

    tk.Label(root, text="Nota:").pack()
    nota_entry = tk.Entry(root)
    nota_entry.pack()

    def adicionar():
        matricula = matricula_entry.get()
        nome_aluno = nome_entry.get()
        disciplina = disciplina_entry.get()
        nota = nota_entry.get()
        adicionar_nota(matricula, nome_aluno, disciplina, nota)

    adicionar_button = tk.Button(root, text="Adicionar Nota", command=adicionar)
    adicionar_button.pack()

    root.mainloop()

if __name__ == "__main__":
    adicionar_nota_interface()
