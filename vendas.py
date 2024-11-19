import numpy as np
import datetime as dt

def carregar_dados(filename):
    dados = np.genfromtxt(
        filename,
        delimiter=",",
        dtype=None,
        names=True,
        encoding="utf-8",
        converters={
            "Data": lambda x: dt.datetime.strptime(x, "%Y-%m-%d"),
            "Quantidade_Vendida": int,
            "Preço_Unitário": float,
            "Valor_Total": float,
        },
    )
    return dados

dados = carregar_dados("vendas.csv")

media_valor_total = np.mean(dados["Valor_Total"])
mediana_valor_total = np.median(dados["Valor_Total"])
desvio_padrao_valor_total = np.std(dados["Valor_Total"])

print(f"Média do Valor Total: {media_valor_total:.2f}")
print(f"Mediana do Valor Total: {mediana_valor_total:.2f}")
print(f"Desvio Padrão do Valor Total: {desvio_padrao_valor_total:.2f}")

produtos, quantidade_por_produto = np.unique(dados["Produto"], return_counts=True)
produto_mais_vendido = produtos[np.argmax(quantidade_por_produto)]

produto_valor_total = {}
for produto in produtos:
    produto_valor_total[produto] = np.sum(
        dados["Valor_Total"][dados["Produto"] == produto]
    )
produto_maior_valor = max(produto_valor_total, key=produto_valor_total.get)

print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Produto com maior valor total de vendas: {produto_maior_valor}")

regioes = np.unique(dados["Região"])
vendas_por_regiao = {}
for regiao in regioes:
    vendas_por_regiao[regiao] = np.sum(dados["Valor_Total"][dados["Região"] == regiao])

print("Valor total de vendas por região:")
for regiao, valor in vendas_por_regiao.items():
    print(f"{regiao}: {valor:.2f}")

datas_unicas = np.unique(dados["Data"])
venda_total_por_dia = [
    np.sum(dados["Valor_Total"][dados["Data"] == data]) for data in datas_unicas
]
venda_media_por_dia = np.mean(venda_total_por_dia)

print(f"Venda média por dia: {venda_media_por_dia:.2f}")

dias_da_semana = [data.strftime("%A") for data in dados["Data"]]
dias_semana_unicos = np.unique(dias_da_semana)
vendas_por_dia_semana = {dia: 0 for dia in dias_semana_unicos}

for i, dia in enumerate(dias_da_semana):
    vendas_por_dia_semana[dia] += dados["Valor_Total"][i]

dia_com_mais_vendas = max(vendas_por_dia_semana, key=vendas_por_dia_semana.get)

print(f"Dia da semana com maior valor total de vendas: {dia_com_mais_vendas}")

vendas_por_data = {
    data: np.sum(dados["Valor_Total"][dados["Data"] == data]) for data in datas_unicas
}
datas_ordenadas = sorted(vendas_por_data.keys())
variacao_diaria = [
    vendas_por_data[datas_ordenadas[i]] - vendas_por_data[datas_ordenadas[i - 1]]
    for i in range(1, len(datas_ordenadas))
]

variacao_diaria_formatada = [f"{v:.2f}" for v in variacao_diaria]
print("Variação diária no valor total de vendas:", variacao_diaria_formatada)