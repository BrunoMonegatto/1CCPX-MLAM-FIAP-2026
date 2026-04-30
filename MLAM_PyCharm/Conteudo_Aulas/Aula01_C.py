from collections import Counter
import matplotlib.pyplot as plt

# Dados da pesquisa
dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

# Conta respostas
respostas1 = Counter(dados1)
print(respostas1)

# Gráfico de Barras Horizontal
plt.barh(
    y=list(respostas1.keys()),        # categorias (Sim / Não)
    width=list(respostas1.values()),  # valores
    color=['blue', 'red']             # cores
)

# Título
plt.title('Resultado da Pesquisa Aplicada pelo McDonalds - 2026')

# Legenda
plt.legend(respostas1.keys(), loc='upper right')

# Mostrar gráfico
plt.show()