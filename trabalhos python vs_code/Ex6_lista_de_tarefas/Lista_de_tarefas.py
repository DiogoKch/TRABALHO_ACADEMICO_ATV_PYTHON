import tkinter as tk
from tkinter import messagebox

class Lista_de_tarefas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de tarefas")
        self.geometry("500x450+500+200")

        self.caixa = tk.Frame(self)
        self.caixa.pack(pady=10)

        self.caixa_lista = tk.Listbox(self.caixa, width=25, height=8, font=("Arial", 18), bd=0, highlightthickness=0, selectbackground="#89CFF0", activestyle="none")
        self.caixa_lista.pack(side=tk.LEFT, fill=tk.BOTH)

        self.lista_tarefas = ["tomar cafe da manha",
                              "trabalhar",
                              "almoçar",
                              "trabalhar",
                              "tomar cafe da tarde",
                              "tomar banho",
                              "estudar",
                              "jantar",
                              "fazer tarefas",
                              "jogar",
                              "dormir"]
        
        for item in self.lista_tarefas:
            self.caixa_lista.insert(tk.END, item)

        self.sb = tk.Scrollbar(self.caixa) 
        self.sb.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.caixa_lista.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.caixa_lista.yview)

        self.entrada = tk.Entry(self, font=("Arial", 24))
        self.entrada.pack(pady=20)

        self.add_tarefa = tk.Button(self, text="Adicionar tarefa", width=13, height=1, font=("Arial", 14), command=self.nova_tarefa)
        self.add_tarefa.pack(pady=10)

        self.del_tarefa = tk.Button(self, text="Deletar tarefa", width=13, height=1, font=("Arial", 14), command=self.deletar_tarefa)
        self.del_tarefa.pack()

    def nova_tarefa(self):
        self.tarefa = self.entrada.get()
        if self.tarefa != "":
            self.caixa_lista.insert(tk.END, self.tarefa)
            self.entrada.delete(0, "end")
        else:
            messagebox.showwarning("Erro:", "Favor informe uma tarefa")

    def deletar_tarefa(self):
        self.caixa_lista.delete(tk.ANCHOR) 

if __name__ == "__main__":
    lista_de_tarefas = Lista_de_tarefas()
    lista_de_tarefas.mainloop()