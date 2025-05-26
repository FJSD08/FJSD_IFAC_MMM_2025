import os
import pandas as pd
import matplotlib.pyplot as plt
import time

# Testes IFAC

# Coverage (%)
# Mean Width (t/h)
# Computational Cost (s)
# Rodar no termina o seguinte comoando 
# python executar_metricas.py

class ResidualProcessor:
    def __init__(self, n_residuos, alpha):
        self.n_residuos = n_residuos
        self.alpha = alpha
        self.reset()

    def reset(self):
        self.residuos = []
        self.q_value = 0.0

    def update(self, mode, taxa_ss, taxa_real):
        if mode != 1:
            return None, None, None
        taxa_pred = taxa_ss
        erro_taxa = abs(taxa_real - taxa_pred)
        if len(self.residuos) >= self.n_residuos:
            self.residuos.pop(0)
        self.residuos.append(erro_taxa)
        if self.residuos:
            sorted_res = sorted(self.residuos)
            idx = round((1 - self.alpha) * len(sorted_res)) - 1
            idx = max(0, min(idx, len(sorted_res)-1))
            self.q_value = sorted_res[idx] #* 0.95
        else:
            self.q_value = 0.0
        return (taxa_ss - self.q_value,
                taxa_ss + self.q_value,
                self.q_value)

# === CONFIGURAÇÕES ===
pasta_dados = r'C:\Users\franc\Downloads\dados'
prefixo_arquivo = 'dados_'
extensao = '.xlsx'
num_arquivos = 15
n_residuos = 100
alpha = 0.05

# === ARMAZENAR RESULTADOS ===
resultados = []

for i in range(num_arquivos):
    nome_arquivo = f"{prefixo_arquivo}{i:02d}{extensao}"
    caminho = os.path.join(pasta_dados, nome_arquivo)

    try:
        df = pd.read_excel(caminho, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao abrir {nome_arquivo}: {e}")
        continue

    processor = ResidualProcessor(n_residuos, alpha)
    reais, lowers, uppers, widths, coberturas = [], [], [], [], []

    start_time = time.perf_counter()

    for _, row in df.iterrows():
        lower, upper, _ = processor.update(1, row['taxa_ss'], row['taxa_real'])
        reais.append(row['taxa_real'])
        lowers.append(lower)
        uppers.append(upper)
        widths.append(upper - lower)
        coberturas.append(1 if lower <= row['taxa_real'] <= upper else 0)

    elapsed_time = time.perf_counter() - start_time
    largura_media = sum(widths) / len(widths)
    cobertura = sum(coberturas) / len(coberturas) * 100
    tempo_medio = elapsed_time / len(df)

    resultados.append({
        'Arquivo': nome_arquivo,
        'Largura Média': round(largura_media, 2),
        'Cobertura (%)': round(cobertura, 2),
        'Nível de Confiança (%)': round((1 - alpha) * 100, 2),
        'Tempo Total (s)': round(elapsed_time, 6),
        'Tempo Médio por Amostra (s)': round(tempo_medio, 6)
    })

# === SALVAR EM CSV ===
df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv('metricas_resultado.csv', index=False)
print("✅ Resultados salvos em 'metricas_resultado.csv'")