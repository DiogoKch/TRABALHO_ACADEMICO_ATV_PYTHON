import tkinter as tk

class Cronometro(tk.Tk):
    def __init__(self):
       super().__init__()
       self.title("Cronometro")
       self.geometry("300x300")
       self.tempo = 0
       self.rodando = False
       
       self.rotulo = tk.Label(self, text="00:00:00", pady="20", font=("Arial", 35)) 
       self.rotulo.pack()
       
       self.botao_iniciar = tk.Button(self, text="Iniciar", width=10, height=2, font=("Arial", 14),command=self.iniciar)
       self.botao_iniciar.pack()

       self.botao_parar = tk.Button(self, text="Parar", width=10, height=2, font=("Arial", 14), command=self.parar)
       self.botao_parar.pack()

       self.botao_resetar = tk.Button(self, text="Reset", width=10, height=2, font=("Arial", 14), command=self.resetar)
       self.botao_resetar.pack()

    def iniciar(self):
        self.rodando = True
        self.contar()

    def parar(self):
        self.rodando = False

    def resetar(self):
        self.rodando = False
        self.tempo = 0
        self.rotulo.config(text="00:00:00")

    def contar(self):
        if self.rodando:
            self.tempo += 1
            minutos, segundos = divmod(self.tempo, 60)
            horas, minutos = divmod(minutos, 60)
            self.rotulo.config(text="{:01d}:{:02d}:{:02d}".format(horas, minutos, segundos))
            self.after(1000, self.contar)

if __name__ == "__main__":
    cronometro = Cronometro()
    cronometro.mainloop()


    