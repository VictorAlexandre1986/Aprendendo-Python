from datetime import date


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criarPessoa(cls, nome, ano_nascimento):
        return cls(nome, date.today().year - ano_nascimento)

    def mostrar(self):
        print(f"Nome: {self.nome} e tem {self.idade} anos.")

pessoa = Pessoa.criarPessoa("Victor", 1986)
pessoa.mostrar()

class Seila:
    movimento="correndo"

    def estado_atual(self):
        print(f"Está se movimentando ? : {self.movimento}")

Seila.estado_atual = classmethod(Seila.estado_atual)
Seila.estado_atual()


class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    @staticmethod
    def obter_maior_valor(x, y):
        return max(x, y)


obj = MinhaClasse(10)  # Esse atributo “valor” não será usado

print(MinhaClasse.obter_maior_valor(20, 30))

print(obj.obter_maior_valor(20, 30))

outro exemplo:


class Dates:

    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace(" / ", "-")

        date = Dates("15-12-2016")
        dateFromDB = "15/12/2016"
        dateWithDash = Dates.toDashDate(dateFromDB)

        if (date.getDate() == dateWithDash):
            print("Igual")
        else:
            print("Diferente")


from datetime import date


class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFatherAge(name, fatherAge, fatherPersonAgeDiff):
        return Pessoa(name, date.today().year - fatherAge + fatherPersonAgeDiff)

        @classmethod
        def fromBirtthYear(cls, name, birthYear):
            return cls(name, date.today().year - birthYear)

        def display(self):
            print(self.name + " 's age is: " + str(self.age))

class Man(Pessoa):
    sex = "Male"

    man = Man.fromBirthYear("John", 1985)
    print(isinstance(man, Man))

    man1 = Man.fromFathersAge("John", 1965, 20)
    print(isinstance(man1, Man))

class Dates:
	def __init__(self, date):
		self.date = date

	def getDate(self):
		return self.date

	@staticmethod
	def toDashDate(date):
		return date.replace("/","-")

class DatesWithSlashes(Dates):
	def getDate(self):
		return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/2/2016")

if(date.getDate() == dateFromDB.getDate()):
	print("Equal")
else:
	print("Unequal")

from datetime import date

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	#O método de classe irá criar objetos com os atributos nome e idade
	@classmethod
	def criar_pessoa(cls, nome, ano_nascimento):
		return cls(nome, date.today().year - ano_nascimento)


from datetime import date


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Vai retornar objetos com os atributos nome e idade
    @classmethod
    def criarPessoa(cls, nome, ano_nascimento):
        return cls(nome, date.today().year - ano_nascimento)

    def mostrar(self):
        print(f"Nome: {self.nome} e tem {self.idade} anos.")

        pessoa = Pessoa.criarPessoa("Victor", 1986)
        pessoa.mostrar()


class Pessoa:
    movimento ="correndo"

    def estado_atual(self):
        print(f"Está se movimentando ?: {self.movimento}")


        Pessoa.estado_atual = classmethod(Pessoa.estado_atual)
        Pessoa.estado_atual()


class Pessoa():
	def __init__(self, altura, idade):
		self.altura = altura
		self.idade = idade

class Aluno():
	def __init__(self, altura, idade):
		self.altura = altura
		self.idade = idade

	@classmethod
	def construir_aluno_pessoa(cls, pessoa):
		return cls(pessoa.altura, pessoa.idade)

	def estudar(self):
		print("Estou estudando")

carlos = Pessoa(1.84, 36)
joaquina = Aluno()
joaquina.estudar() # Vai funcionar

#Construindo um objeto da classe Aluno através da instância da classe Pessoa
victor = Aluno.construir_aluno_pessoa(carlos)
victor.estudar()

class Escritor():
	def __init__(self):
		pass

	def escreve(self,text):
		print(text)

	@classmethod
	def escreve_novo(cls, text):
		print(text)


Escritor.escreve("Olá") #Não vai executar
Escritor.escreve_novo("Ola") #Vai executar