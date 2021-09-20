class Classe():
    def __init__(self, nome : str, valor : float):
        self.valor = valor
        self.nome = nome

class Atributo():
    def __init__(self, nome : str, valor : float):
        self.classe : str = ''
        self.nome = nome
        self.atributo_2 : str = ''
        self.valor =  valor
        self.ligado_a : str = ''
        self.valor_calculado : float = 0.0

    def calc_com_um_atributo(self):
        #self.valor_calculado = ...
        pass

    def calc_com_dois_atributo(self):
        #self.valor_calculado = ...
        pass


def povoar(lista: list, classes : list, valores : list):
    while classes:
        obj : Atributo = Atributo(classes.pop(0), valores.pop(0))
        lista.append(obj)


def min(lista: list, K : int) -> int:
    if len(lista) < K:
        return len(lista)
    else:
        return K


def arg_max(lista: list) -> list:
    valores_ordenados = sorted(lista, key=lambda x: x.valor)
    return valores_ordenados


def main():
    #V = lista de nós
    V : list = []
    #quantidade de conexões no atributo com outro atributo
    K : int = 0
    #V = contem todas arestas/ligações
    A : list = []
    #temp = lista de auxílio
    temp : list = []

    lista : list = []

    #imput dos dados - 1º é a classe os demais atributos: J, V, T, U
    #imput dos dados - valores do K, da classe e atributos respectivamente: 1, 1, 10, 9, 8
    S = map(str, input().split(' '))
    valores = map(int, input().split(' '))
    S = list(S)
    valores = list(valores)
    K = valores.pop(0)
    
    # print(f'K: {K}')
    #classe pai (jogar tênis)
    jog_t : Classe = Classe(S.pop(0), valores.pop(0))
    V.append(jog_t)
    tamanho_s : int = len(S)

    povoar(lista, S, valores)

    # for obj in lista:
    #     print(f'classes: {obj.nome} ')

    Xmax : Atributo = None
    lista_aux = arg_max(lista)
    
    while len(temp) != tamanho_s:
        Xmax = lista_aux.pop(-1)
        V.append(Xmax)

        #conectando atributo a classe pai, garantindo o 0-DBC
        for obj in lista:
            if obj == Xmax:
                obj.classe = jog_t.nome

        conexoes = min(temp, K)
        if conexoes > 0:
            for obj in lista:
                if obj == Xmax:
                    obj.ligado_a = "LIGADO" # FALTA FAZER 1:04:41 video professor
            
        # print(Xmax.valor)

        temp.append(Xmax)


if __name__ == "__main__":
    main()
