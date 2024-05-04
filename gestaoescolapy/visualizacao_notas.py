import tkinter as tk
from tkinter import ttk
import mysql.connector

def visualizar_notas(matricula):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escola"
        )
        cursor = connection.cursor()

        query = "SELECT disciplina, nota FROM notas WHERE matricula_aluno = %s"
        cursor.execute(query, (matricula,))
        notas = cursor.fetchall()

        root = tk.Tk()
        root.title("Visualização de Notas")
        root.geometry("400x200+400+200")  

        tree = ttk.Treeview(root, columns=("Disciplina", "Nota"), show="headings")
        tree.heading("Disciplina", text="Disciplina")
        tree.heading("Nota", text="Nota")

        for nota in notas:
            tree.insert("", "end", values=nota)

        tree.pack()

        root.mainloop()
    except Exception as e:
        print(f"Erro ao visualizar notas: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def visualizar_notas_interface():
    def visualizar():
        matricula = matricula_entry.get()
        visualizar_notas(matricula)

    root = tk.Tk()
    root.title("Visualização de Notas")
    root.geometry("400x200+400+200")  

    tk.Label(root, text="Matrícula do Aluno:").pack()
    matricula_entry = tk.Entry(root)
    matricula_entry.pack()

    visualizar_button = tk.Button(root, text="Visualizar Notas", command=visualizar)
    visualizar_button.pack()

    root.mainloop()

if __name__ == "__main__":
    visualizar_notas_interface()
