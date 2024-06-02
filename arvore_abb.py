class No:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def inserir(self, valor):

        if valor is None:
            raise ValueError("Necessário inserir o valor")
        if self.root is None:
            self.root = No(valor)
        else:
            self._inserir_rec(self.root, valor)

    def _inserir_rec(self, no_atual, valor):

        if valor < no_atual.valor:
            if no_atual.left is None:
                no_atual.left = No(valor)
            else:
                self._inserir_rec(no_atual.left, valor)
        elif valor > no_atual.valor:
            if no_atual.right is None:
                no_atual.right = No(valor)
            else:
                self._inserir_rec(no_atual.right, valor)

    def excluir(self, valor):

        self.root = self._excluir(self.root, valor)

    def _excluir(self, no_atual, valor):

        if no_atual is None:
            return no_atual
        if valor < no_atual.valor:
            no_atual.left = self._excluir(no_atual.left, valor)
        elif valor > no_atual.valor:
            no_atual.right = self._excluir(no_atual.right, valor)
        else:
            if no_atual.left is None:
                return no_atual.right
            elif no_atual.right is None:
                return no_atual.left

            temp = self._min_val(no_atual.right)
            no_atual.valor = temp.valor
            no_atual.right = self._excluir(no_atual.right, temp.valor)

    def _min_val(self, no_atual):

        current = no_atual
        while current.left is not None:
            current = current.left
        return current

    def altura(self, no_atual):

        if no_atual is None:
            return 0
        else:
            altura_esquerda = self.altura(no_atual.left)
            altura_direita = self.altura(no_atual.right)
        return 1 + max(altura_esquerda, altura_direita)

    def buscar(self, valor):
        return self._buscar_rec(self.root, valor)

    def _buscar_rec(self, no_atual, valor):

        if no_atual is None or no_atual.valor == valor:
            return no_atual
        if valor < no_atual.valor:
            return self._buscar_rec(no_atual.left, valor)
        else:
            return self._buscar_rec(no_atual.right, valor)

    def in_ordem(self, no_atual):
        if no_atual is not None:
            self.in_ordem(no_atual.left)
            print(no_atual.valor)
            self.in_ordem(no_atual.right)


    def pre_ordem(self, no_atual):

        if no_atual is not None:
            print(no_atual.valor)
            self.pre_ordem(no_atual.left)
            self.pre_ordem(no_atual.right)

    def pos_ordem(self, no_atual):

        if no_atual is not None:
            self.pos_ordem(no_atual.left)
            self.pos_ordem(no_atual.right)
            print(no_atual.valor)

if __name__ == "__main__":

    tree = ABB()

    valores = [2, 10, 5, 9, 23, 20, 56]

    for val in valores:
        tree.inserir(val)

    print("Travessia em ordem:")
    tree.in_ordem(tree.root)

    print("\nTravessia pré-ordem:")
    tree.pre_ordem(tree.root)

    print("\nTravessia pós-ordem:")
    tree.pos_ordem(tree.root)

    busca_no = tree.buscar(9)
    if busca_no:
        print(f'Possui o {busca_no.valor} na árvore')
    else:
        print(f'Não tem o {busca_no.valor} na árvore')

    print(f"ALtura da árvore: {tree.altura(tree.root)}")

