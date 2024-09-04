import statistics

# Dados de faturamento diário
faturamento_diario = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Função para calcular estatísticas
def calcular_estatisticas(dados):
    valores = [dia["valor"] for dia in dados if dia["valor"] > 0]
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media = statistics.mean(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media)
    
    return menor_valor, maior_valor, media, dias_acima_media

# Calcular estatísticas
menor, maior, media, dias_acima_media = calcular_estatisticas(faturamento_diario)

# Imprimir resultados
print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Média mensal de faturamento: R$ {media:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Função para encontrar o dia com maior faturamento
def dia_maior_faturamento(dados):
    return max(dados, key=lambda x: x["valor"])

dia_maior = dia_maior_faturamento(faturamento_diario)
print(f"Dia com maior faturamento: Dia {dia_maior['dia']} (R$ {dia_maior['valor']:.2f})")

# Calcular faturamento total
faturamento_total = sum(dia["valor"] for dia in faturamento_diario)
print(f"Faturamento total do mês: R$ {faturamento_total:.2f}")