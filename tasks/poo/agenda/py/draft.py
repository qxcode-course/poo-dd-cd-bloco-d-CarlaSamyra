class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id 
        self.__number = number

    def __str__ (self):
        return f"{self.__id}:{self.__number}"

    def get_number (self):
        return self.__number
    
    def get_id (self):
        return self.__id 
    
    def isValid (self):
        return all(i.isdigit() for i in self.__number)

class Contato:
    def __init__ (self, name: str): 
        self.__name = name 
        self.__fones: list[Fone] = []
        self.__favorited = False

    def __str__ (self):
        fones = ", ".join(str(i) for i in self.__fones)
        return f"- {self.__name} [{fones}]"
    
    def get_name(self):
        return self.__name
    
    def addFone (self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)

class Agenda:
    def __init__ (self):
        self.__contatos: list[Contato] = []

    def __str__ (self):
        sorted_contato = sorted(self.__contatos, key=lambda c: c.get_name())
        return "\n".join(str(i) for i in sorted_contato)
    
    def get_contato (self):
        return self.__contatos
    
    def addContato (self, name: str, fones: list[Fone]):
        verificarContato = None
        for contato in self.__contatos:
            if contato.get_name() == name:
                verificarContato = contato
                break
        if verificarContato:
            for i in fones:
                verificarContato.addFone(i.get_id(), i.get_number())
            return
        if verificarContato is not True:
            contato = Contato(name)
            for i in fones:
                contato.addFone(i.get_id(), i.get_number())
            self.__contatos.append(contato)

def main():
    agenda = Agenda()
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)

        try:
            if args[0] == "end":
                break
            elif args[0] == "add":
                name = args[1]
                fone: list[Fone] = []
                for i in args[2:]:
                    id, number = i.split(":")
                    fone.append(Fone(id, number))
                agenda.addContato(name, fone)
            elif args[0] == "show":
                print(agenda)
            else:
                print("fail: comando inválido")

        except Exception as e:
            print(e)

main()