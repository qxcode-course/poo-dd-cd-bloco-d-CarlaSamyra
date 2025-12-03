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
        
    def rmFone (self, index: int):
        if 0 <= index and index < len(self.__fones):
            self.__fones.pop(index)
            return

class Agenda:
    def __init__ (self):
        self.__contatos: list[Contato] = []

    def __str__ (self):
        sorted_contato = sorted(self.__contatos, key=lambda c: c.get_name())
        return "\n".join(str(i) for i in sorted_contato)
    
    def getContato (self, name:str):
        posicao = self.findPosByName(name)
        if posicao >= 0:
                return self.__contatos[posicao]
        return None
    
    def findPosByName (self, name: str):
        for i, contato in enumerate(self.__contatos):
            if contato.get_name() == name:
                return i 
        return -1
        
    def addContato (self, name: str, fones: list[Fone]):
        posicao = self.findPosByName(name)
        if posicao >= 0:
            for i in fones:
                self.__contatos[posicao].addFone(i.get_id(), i.get_number())
            return
        else:
            contato = Contato(name)
            for i in fones:
                contato.addFone(i.get_id(), i.get_number())
            self.__contatos.append(contato)
    
    def rmContato (self, name: str):
        contato = self.findPosByName(name)
        if contato >= 0:
            self.__contatos.pop(contato)
            return
        
    def search (self, pattern: str) -> list[Contato]:
        resultados = []
        for contato in self.__contatos:
            contato_str = str(contato)
            if pattern in contato_str:
                resultados.append(contato)
        return resultados

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
            elif args[0] == "rmFone":
                name = args[1]
                index = int(args[2])
                contato = agenda.getContato(name)
                contato.rmFone(index)
            elif args[0] == "rm":
                name = args[1]
                agenda.rmContato(name)
            elif args[0] == "search":
                pattern = args[1]
                resultados = agenda.search(pattern)
                for contato in sorted(resultados, key=lambda c: c.get_name()):  # Ordena os resultados
                        print(contato)
            else:
                print("fail: comando inválido")

        except Exception as e:
            print(e)

main()