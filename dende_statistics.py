class Statistics:

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


    def stdev(self, column):

        # Reuso da variância
        valor_variancia = self.variance(column)

        # Cálculo da raiz quadrada
        resultado = valor_variancia ** 0.5

        return resultado


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


    def itemset(self, column):

        dados = self.dataset[column]

        # Uso de set para selecionar itens únicos
        itens_unicos = set(dados)

        return itens_unicos


    def absolute_frequency(self, column):

        dados = self.dataset[column]

        # Dicionário para contar ocorrências
        frequencias = {}

        # Definindo contagem para associar itens a suas frequencias
        for item in dados:
            if item in frequencias:
                frequencias[item] += 1
            else:
                frequencias[item] = 1

        return frequencias


    def relative_frequency(self, column):
        # Reaproveitando metodo absolute_frequency utilizado anteriormente
        contagens = self.absolute_frequency(column)

        # Pega o total de linhas na coluna
        total_elementos = len(self.dataset[column])

        # Dicionário para as proporções
        frequencias_relativas = {}

        # Calculando a proporção para cada item
        for item, contagem in contagens.items():
            frequencias_relativas[item] = contagem / total_elementos

        return frequencias_relativas


    def cumulative_frequency(self, column, frequency_method='absolute'):
        # Reaproveitando metodo absolute_frequency e relative_frequency utilizado anteriormente
        # Escolhe se usa a contagem numeral ou percentual
        if frequency_method == 'relative':
            frequencia_base = self.relative_frequency(column)
        else:
            frequencia_base = self.absolute_frequency(column)

        # Pega as chaves do dicionário
        categorias = list(frequencia_base.keys())

        # Mesma lógica da Mediana
        if column == "priority":
            ordem_customizada = {"baixa": 0, "media": 1, "alta": 2}
            categorias_ordenadas = sorted(categorias, key=lambda x: ordem_customizada.get(x, 0))
        else:
            categorias_ordenadas = sorted(categorias)

        # Lógica da Acumulação
        acumulada = {}
        soma_progressiva = 0

        for item in categorias_ordenadas:
            soma_progressiva += frequencia_base[item]
            acumulada[item] = soma_progressiva

        return acumulada


    def conditional_probability(self, column, value1, value2):

        dados = self.dataset[column]
        n = len(dados)

        # Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        contagem_b = 0
        contagem_ab = 0


        # O último item não tem ninguém depois dele, então não gera uma sequência
        # Por isso percorre a lista até o penúltimo item
        for i in range(n - 1):
            # Se encontramos o valor condicionante (B)
            if dados[i] == value2:
                contagem_b += 1
                # Verificamos se o próximo item é o valor consequente (A)
                if dados[i + 1] == value1:
                    contagem_ab += 1

        # Evita divisão por zero
        if contagem_b == 0:
            return 0.0

        return contagem_ab / contagem_b


    def quartiles(self, column):

        dados = sorted(self.dataset[column])
        n = len(dados)

        # Reuso da mediana para o Q2
        q2 = self.median(column)

        # Função interna para calcular a posição (Interpolação)
        def calcular_posicao(percentil):
            # Localiza o índice (posição teorica)
            indice = percentil * (n + 1)
            idx_baixo = int(indice)
            idx_alto = idx_baixo + 1

            # Ajuste de limites para não sair da lista
            if idx_baixo < 1: return dados[0]
            if idx_baixo >= n: return dados[-1]

            # Calcula o valor entre dois índices (Interpolação)
            peso = indice - idx_baixo
            return dados[idx_baixo - 1] + peso * (dados[idx_alto - 1] - dados[idx_baixo - 1])

        return {
            "Q1": calcular_posicao(0.25),
            "Q2": q2,
            "Q3": calcular_posicao(0.75)
        }


    def histogram(self, column, bins):

        dados = self.dataset[column]

        # Valida e anota os limites
        min_val = min(dados)
        max_val = max(dados)

        # Se todos os valores forem iguais, teremos apenas 1 intervalo
        if min_val == max_val:
            return {(min_val, max_val): len(dados)}

        # Cálculo da largura de cada intervalo (bin)
        amplitude = max_val - min_val
        largura_bin = amplitude / bins

        # Criação dos intervalos e contagem
        histograma = {}
        intervalos = []

        # Logica para os intervalos desejados
        for i in range(bins):
            inicio = min_val + (i * largura_bin)
            fim = min_val + ((i + 1) * largura_bin)
            intervalo = (inicio, fim)
            intervalos.append(intervalo)
            histograma[intervalo] = 0

        # Distribuí os dados nos intervalos
        for valor in dados:
            # Se for o valor máximo, ele entra no último intervalo
            if valor == max_val:
                indice_bin = bins - 1
            else:
                indice_bin = int((valor - min_val) / largura_bin)

            # Proteção contra erros de arredondamento
            if indice_bin >= bins:
                indice_bin = bins - 1

            histograma[intervalos[indice_bin]] += 1

        return histograma
