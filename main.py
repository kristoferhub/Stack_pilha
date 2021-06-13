"""
Kristofer R.K

Rodando a pilha!

"""
# ======================================================================================================================
from stack import Stack

pilha = Stack()

# Tamanho da pilha
print('=======================================================')
print(len(pilha))
print('======================================================= \n')

# Mostrando a pilha
print(pilha)

print('=======================================================')
# Adicionando itens na pilha
pilha.add(1)
pilha.add('Kristofer')
pilha.add(5.5)
pilha.add(True)
print('======================================================= \n')


# Mostrando a pilha
print(pilha)

# Exibir o top da pilha
print(pilha.peek())
print('\n')

# Remover elemento do topo da pilha
print(pilha.remove())
print('\n')

# Mostrando a pilha
print(pilha)

# Exibir o top da pilha
print(pilha.peek())

# ======================================================================================================================
