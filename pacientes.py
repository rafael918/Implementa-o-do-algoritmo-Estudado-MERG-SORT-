class Node:
    def __init__(self, nome, idade, registro_medico):
        self.nome = nome
        self.idade = idade
        self.registro_medico = registro_medico
        self.next = None

class ListaPaciente:
    def __init__(self):
        self.head = None

    def add_paciente(self, nome, idade, registro_medico):
        novo_paciente = Node(nome, idade, registro_medico)
        if self.head is None:
            self.head = novo_paciente
        else:
            paciente_atual = self.head
            while paciente_atual.next is not None:
                paciente_atual = paciente_atual.next
            paciente_atual.next = novo_paciente

    def lista_pacientes(self):
        lista = []
        paciente_atual = self.head
        while paciente_atual is not None:
            lista.append((paciente_atual.nome, paciente_atual.idade, paciente_atual.registro_medico))
            paciente_atual = paciente_atual.next
        return lista

    @staticmethod
    def merge_sort(array):
        if len(array) <= 1:
            return array
        meio = len(array) // 2
        esquerda = ListaPaciente.merge_sort(array[:meio])
        direita = ListaPaciente.merge_sort(array[meio:])
        return ListaPaciente.merge(esquerda, direita)

    @staticmethod
    def merge(esquerda, direita):
        lista_ordenada = []
        while len(esquerda) > 0 and len(direita) > 0:
            if esquerda[0][1] < direita[0][1]:  # Comparação de idades
                lista_ordenada.append(esquerda.pop(0))
            else:
                lista_ordenada.append(direita.pop(0))
        lista_ordenada.extend(esquerda)
        lista_ordenada.extend(direita)
        return lista_ordenada

# Criar instância da lista de pacientes e adicionar pacientes
pacientes = ListaPaciente()
pacientes.add_paciente("Alice", 30, "A123")
pacientes.add_paciente("Bob", 25, "B456")
pacientes.add_paciente("Charlie", 35, "C789")
pacientes.add_paciente("David", 20, "D012")
pacientes.add_paciente("Eva", 28, "E345")
pacientes.add_paciente("Frank", 40, "F678")
pacientes.add_paciente("Grace", 32, "G901")
pacientes.add_paciente("Helen", 45, "H234")
pacientes.add_paciente("Ivan", 27, "I567")
pacientes.add_paciente("Jack", 38, "J890")
pacientes.add_paciente("Kate", 29, "K123")
pacientes.add_paciente("Liam", 33, "L456")
pacientes.add_paciente("Megan", 42, "M789")
pacientes.add_paciente("Nora", 26, "N012")
pacientes.add_paciente("Oliver", 37, "O345")
pacientes.add_paciente("Patricia", 31, "P678")
pacientes.add_paciente("Quinn", 44, "Q901")
pacientes.add_paciente("Ryan", 36, "R234")
pacientes.add_paciente("Candido", 39, "C567")

# Listar pacientes antes da ordenação
print("Lista de Pacientes antes da ordenação:")
for paciente in pacientes.lista_pacientes():
    print(f"Nome: {paciente[0]}, Idade: {paciente[1]}, Prontuário: {paciente[2]}")

# Ordenar pacientes
lista_ordenada = pacientes.merge_sort(pacientes.lista_pacientes())
pacientes.head = None
for paciente_data in lista_ordenada:
    pacientes.add_paciente(*paciente_data)

# Listar pacientes após a ordenação
print("\nLista de Pacientes após a ordenação:")
for paciente in pacientes.lista_pacientes():
    print(f"Nome: {paciente[0]}, Idade: {paciente[1]}, Prontuário: {paciente[2]}")









