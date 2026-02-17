import csv
from dende_statistics import Statistics


def carregar_csv(caminho_arquivo):
    colunas_numericas = [
        'track_number', 'track_popularity', 'artist_popularity',
        'artist_followers', 'album_total_tracks', 'track_duration_min'
    ]
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            dataset = {col: [] for col in leitor.fieldnames}
            for linha in leitor:
                for col in leitor.fieldnames:
                    valor = linha[col]
                    if col in colunas_numericas:
                        try:
                            dataset[col].append(float(valor))
                        except (ValueError, TypeError):
                            dataset[col].append(0.0)
                    else:
                        dataset[col].append(str(valor))
            return dataset
    except FileNotFoundError:
        print(f"ERRO: Arquivo {caminho_arquivo} não encontrado.")
        return None


# --- EXECUÇÃO DO TESTE COMPLETO ---
dados = carregar_csv('spotify_data clean.csv')

if dados:
    s = Statistics(dados)

    print("=" * 60)
    print("   RELATÓRIO COMPLETO: BIBLIOTECA DENDE STATISTICS")
    print("=" * 60)

    # 1. Média, 2. Mediana, 3. Moda
    print(f"\n[1] Média (Popularidade): {s.mean('track_popularity'):.2f}")
    print(f"[2] Mediana (Duração min): {s.median('track_duration_min'):.2f}")
    print(f"[3] Moda (Tipo de Álbum): {s.mode('album_type')}")

    # 4. Variância, 5. Desvio Padrão
    print(f"[4] Variância (Popularidade): {s.variance('track_popularity'):.2f}")
    print(f"[5] Desvio Padrão (Popularidade): {s.stdev('track_popularity'):.2f}")

    # 6. Covariância
    print(f"[6] Covariância (Popularidade x Seguidores): {s.covariance('track_popularity', 'artist_followers'):.2f}")

    # 7. Itemset
    print(f"[7] Itemset (Tipos de Álbum): {s.itemset('album_type')}")

    # 8. Frequência Absoluta
    print(f"[8] Freq. Absoluta (Tipo de Álbum): {s.absolute_frequency('album_type')}")

    # 9. Frequência Relativa
    print(f"[9] Freq. Relativa (Tipo de Álbum): {s.relative_frequency('album_type')}")

    # 10. Frequência Acumulada
    # Usando 'album_type' para mostrar a soma progressiva
    print(f"[10] Freq. Acumulada Absoluta (Álbum): {s.cumulative_frequency('album_type', 'absolute')}")

    # 11. Probabilidade Condicional
    # Ex: Qual a chance de vir um 'single' logo após um 'album' na lista?
    prob = s.conditional_probability('album_type', 'single', 'album')
    print(f"[11] Prob. de (Single | Album): {prob * 100:.2f}%")

    # 12. Quartis
    q = s.quartiles('track_popularity')
    print(f"[12] Quartis (Popularidade): Q1: {q['Q1']:.2f}, Q2: {q['Q2']:.2f}, Q3: {q['Q3']:.2f}")

    # 13. Histograma
    print(f"[13] Histograma (Popularidade - 5 faixas):")
    hist = s.histogram('track_popularity', bins=5)
    for intervalo, contagem in hist.items():
        print(f"     Faixa {intervalo}: {contagem} músicas")

    print("=" * 60)
    print("   FIM DO TESTE - TODAS AS FUNÇÕES EXECUTADAS")
    print("=" * 60)