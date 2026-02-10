class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):

        # Verificando se é um dicionario
        if not isinstance(dataset, dict):
         raise ValueError("ERRO: O dataset não é um dicionário.") 

        self.dataset = dataset
        self.colunas = list(dataset.keys())

        # Verificando se o dataset está vazio
        if not self.colunas:
            
            return
    
        # Verificando o tamanho da lista
        tamanho_esperado = len(dataset[self.colunas[0]])

        # Verificando se as colunas tem tamanhos diferentes
        for coluna in self.colunas:
            if len(dataset[coluna]) != tamanho_esperado:
                raise ValueError(f"ERRO: A coluna '{coluna}' tem um tamanho diferente das outras.")

        # Verificando se o tipo das colunas estão diferentes
            if len(dataset[coluna]) > 0:
                tipo_primeiro = type(dataset[coluna][0])
                for item in dataset[coluna]:
                    if type(item) != tipo_primeiro:
                        raise ValueError(f"ERRO: A coluna '{coluna}' tem diferentes tipos de dados.")
    

    def mean(self, column):
        
        # Pegando os dados dentro do dataset
        dados = self.dataset[column]

        # Verificando se os dados são números
        if not isinstance(dados[0], (int, float)):
            raise ValueError(f"ERRO: A coluna '{column}' não é numérica.")
        
        soma_total = 0
        quantidade_elementos = 0

        for valor in dados:
            soma_total += valor
            quantidade_elementos += 1

        media = soma_total / quantidade_elementos

        return media

    pass

    def median(self, column):

            dados = self.dataset[column]
            # Criando valores baseados nos dados da coluna "priority"
            if column == "priority":
                ordem = {"baixa": 0, "media": 1, "alta": 2}

                # Ordenando os valores e validando se está corretamente numérica e com ordem
                dados_ordenados = sorted(dados, key=lambda x: ordem[x])
            else:
                try:
                    dados_ordenados = sorted(dados)
                except TypeError:
                    raise ValueError(f"ERRO: A coluna '{column}' não é numérica e não tem ordem definida.")

            # Fórmula da Mediana
            n = len(dados_ordenados)
            meio = n // 2

            if n % 2 != 0:
                return dados_ordenados[meio]
            else:

                if isinstance(dados_ordenados[meio], (int, float)):
                    return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
                else:
                    return dados_ordenados[meio - 1]

    pass

    def mode(self, column):

        dados = self.dataset[column]

        # Criando um dicionário para contar ocorrências
        contagem = {}

        # Criando fórmula de contagem, os itens serão associados à quantidade de vezes em que aparecem,
        # assumindo um valor

        for item in dados:
            if item in contagem:
                contagem[item] += 1
            else:
                contagem[item] = 1

        # Max retorna o maior valor entre os itens contados anteriormente
        max_frequencia = max(contagem.values())


        # Criando fórmula de Moda, verifica o valor adquirido por cada item e compara com o maior registrado no 'max',
        # O item que for igual ao 'max', será considerado o contado mais vezes, ou seja, a Moda
        modas = []
        for item in contagem:
            if contagem[item] == max_frequencia:
                modas.append(item)

        # Retorna a Moda
        return sorted(modas)

    pass

    def variance(self, column):

        dados = self.dataset[column]

        # Reuso da media
        media_valores = self.mean(column)

        # Cálculo da soma das diferenças ao quadrado
        soma_varianca = 0
        for valor in dados:
            diferenca = valor - media_valores
            soma_varianca += diferenca ** 2

        # Divisão pelo total de elementos
        return soma_varianca / len(dados)

    pass

    def stdev(self, column):

        # Reuso da variância
        valor_variancia = self.variance(column)

        # Cálculo da raiz quadrada
        resultado = valor_variancia ** 0.5

        return resultado

    pass

    def covariance(self, column_a, column_b):

        # Capturando os dados das colunas que serão comparadas
        dados_x = self.dataset[column_a]
        dados_y = self.dataset[column_b]
        n = len(dados_x)

        # Raproveitando metodo mean utilizado anteriormente, e extraindo a média em cada coluna
        media_x = self.mean(column_a)
        media_y = self.mean(column_b)

        # Criando a variável para realizar a fórmula da covariância
        soma_produtos = 0

        # Criando a fórmula da covariância (Somatório)
        for i in range(n):
            soma_produtos += (dados_x[i] - media_x) * (dados_y[i] - media_y)
        # Segunda parte da fórmula (divide o somatório pela quantidade de elementos)
        return soma_produtos / n

    pass

    def itemset(self, column):

        dados = self.dataset[column]

        # Uso de set para selecionar itens únicos
        itens_unicos = set(dados)

        return itens_unicos

    pass

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        pass

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """
        pass

    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        pass

    def quartiles(self, column):
        """
        Calcula os quartis (Q1, Q2 e Q3) de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário com os quartis Q1, Q2 (mediana) e Q3.
        """
        pass

    def histogram(self, column, bins):
        """
        Gera um histograma baseado em buckets (intervalos).

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        bins : int
            Número de buckets (intervalos).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os intervalos (tuplas)
            e os valores são as contagens.
        """
        pass

