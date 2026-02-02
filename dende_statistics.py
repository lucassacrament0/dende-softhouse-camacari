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

        return soma_total / quantidade_elementos

        pass

    def median(self, column):

        dados = self.dataset[column]

        if not isinstance(dados[0], (int, float)):
            raise ValueError(f"ERRO: A coluna '{column}' não é numérica.")
        
        dados_ordenados = sorted(dados)
        n = len(dados_ordenados)
        meio = n // 2
    
        if n % 2 != 0:
            resultado = dados_ordenados[meio]
        else:
            valor_1 = dados_ordenados[meio - 1]
            valor_2 = dados_ordenados[meio]
            resultado = (valor_1 + valor_2) / 2
            
        return resultado

        pass

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        pass

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        pass

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        pass

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
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

