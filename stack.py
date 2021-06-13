"""
Kristofer R.K
Estrutura de dados

PILHA!

@Lifo = Last In First Out = O último a entrar é o primeiro a sair

"""

from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Inserir um elemento na pilha.
    def add(self, elem):
        node = Node(elem)
        # Novo topo da pilha
        node.next = self.top
        self.top = node
        self._size = self._size + 1
        print('Elemento inserido!')

    # Remover o elemento do topo da pilha.
    def remove(self):
        # Verificar se a pilha possui itens.
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            # Diminuir o tamanho (len)
            self._size = self._size - 1
            print('Elemento do topo da pilha removido!')
            return node.data
        raise IndexError("Erro, a pilha está vazia!")

    # Retorna o topo da pilha sem remover
    def peek(self):
        # Verificar se a pilha possui itens.
        if self._size > 0:
            print('Topo da pilha!')
            return self.top.data
        raise IndexError("Erro, a pilha está vazia!")

    # Retornar o tamanho da pilha
    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        if self._size <= 0:
            print('=======================================================')
            return f'Pilha vazia \n======================================================= \n'
        else:
            print('=======================================================')
            while pointer:
                r = r + str(pointer.data) + "\n"
                pointer = pointer.next
            return f'{r}=======================================================\n'

    def __str__(self):
        return self.__repr__()