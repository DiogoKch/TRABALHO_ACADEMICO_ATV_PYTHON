class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"
    
class Agenda_telefonica:
    def __init__(self):
        self.contatos = []

    def add_contato(self, contato):
        self.contatos.append(contato)

    def deletar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)

    def procurar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
    
    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

def main():
    agenda_telefonica = Agenda_telefonica()

    while True:
        print("\n")
        print("-"*30)
        print("MENU DA AGENDA TELEFÔNICA:")
        print("\n1. Adicionar contato")
        print("2. Deletar contato")
        print("3. Procurar contato")
        print("4. Listar contatos")
        print("5. Sair")
        print("-"*30)

        escolha = input("\nOque deseja fazer? ")

        if escolha == "1":
            nome = input("\nInforme o nome: ")
            telefone = input("Informe o telefone: ")
            contato = Contato(nome, telefone)
            agenda_telefonica.add_contato(contato)
            print("Contato adicionado com sucesso!")
            

        elif escolha == "2":
            nome = input("\nInforme o contato que deseja deletar: ")
            agenda_telefonica.deletar_contato(nome)
            print("Contato foi deletado com sucesso!")

        elif escolha == "3": 
            nome = input("\nQual contato deseja procurar? ")
            contato = agenda_telefonica.procurar_contato(nome)
            if contato:
                print("Contato foi encontrado!")
                print(contato)
            else:
                print("Contato não encontrado")

        elif escolha == "4":
            print("\nListando contatos")
            agenda_telefonica.listar_contatos()

        elif escolha == "5":
            print("\nFechando agenda, até mais!")
            print("\n")
            print("-"*30)
            break
        else:
            print("\nErro: Escolha invalida!")

if __name__ == "__main__":
    main()