import tkinter as tk

class Calc_IMC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora IMC")
        self.geometry("350x400")

        self.rotulo_peso = tk.Label(self, text="Digite seu peso (Kg):", pady="20", font=("Arial", 15, "bold")) 
        self.rotulo_peso.pack(pady=5)

        self.entrada_peso = tk.Entry(self, font=("Arial", 15))
        self.entrada_peso.pack()

        self.rotulo_altura = tk.Label(self, text="Digite sua altura (Cm):", pady="20", font=("Arial", 15, "bold")) 
        self.rotulo_altura.pack(pady=5)

        self.entrada_altura = tk.Entry(self, font=("Arial", 15))
        self.entrada_altura.pack()

        self.botao_calcular = tk.Button(self, text="Calcular", width=8, height=1, font=("Arial", 14), command=self.calcular)
        self.botao_calcular.pack(pady=15)

        self.resultado_IMC = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_IMC.pack()

        self.relatorio = tk.Label(self, text="", font=("Arial", 14))
        self.relatorio.pack(pady=10)

    def calcular(self):
        self.peso = float(self.entrada_peso.get())
        self.altura = float(self.entrada_altura.get())
        self.altura = self.altura/100

        imc = self.peso/(self.altura*self.altura)
        self.resultado_IMC.config(text="Seu IMC : {:.2f}".format(imc))

        if imc <= 18.4:
            self.relatorio.config(text="Relatorio: Abaixo do peso")
        elif imc > 18.5 and imc < 24.9:
            self.relatorio.config(text="Relatorio: Normal")
        elif imc > 25.0 and imc < 39.9:
            self.relatorio.config(text="Relatorio: Acima do peso")
        else:
            self.relatorio.config(text="Relatorio: Obeso")

if __name__ == "__main__":
    cal_IMC = Calc_IMC()
    cal_IMC.mainloop()