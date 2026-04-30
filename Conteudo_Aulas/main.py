# Preparando o ambiente:
from collections import Counter
import matplotlib.pyplot as plt

# ==============================
# Gráficos para variáveis qualitativas
# ==============================

# Gráfico de Setores (Pizza)

# 1) Conjunto de dados:
# Simulando respostas de uma pesquisa
dados1 = ["Sim"] * 20 + ["Não"] * 45

# Mostra a lista completa (opcional, só para conferir)
print(dados1)

# Conta quantas vezes cada resposta aparece
respostas1 = Counter(dados1)

# ==============================
# 2) Construção do gráfico
# ==============================

plt.pie(
    list(respostas1.values()),   # valores (quantidade de Sim e Não)
    labels=list(respostas1.keys()),  # nomes das categorias
    autopct='%1.2f%%',           # mostra porcentagem com 2 casas decimais
    colors=['blue', 'red']       # cores das fatias
)

# Título do gráfico
plt.title('Resultado da Pesquisa Aplicada pelo McDonalds - 2026')

# Legenda (mostra Sim e Não fora do gráfico)
plt.legend(respostas1.keys(), loc='upper right')

# Exibe o gráfico na tela
plt.show()