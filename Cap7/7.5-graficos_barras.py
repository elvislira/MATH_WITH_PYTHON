from random import randint
from string import ascii_uppercase
from pylab import subplot
from pylab import bar
from pylab import barh
from pylab import show
from pylab import axis
from pylab import xlabel
from pylab import ylabel
from pylab import title


# Retorna os dados para o gráfico
def dados(nprodutos):
    # Gera uma lista com as letras maiúsculas do alfabeto
    produtos = list(ascii_uppercase)
    print(len(produtos))
    # Gera uma lista de quantidades
    quantidades = [randint(1, 10) for i in range(len(produtos))]
    return (
        produtos[:nprodutos],
        quantidades[:nprodutos]
    )

produtos = dados(9)[0]
quantidades = dados(9)[1]

# Barras verticais
subplot(121)
bar(
    produtos,
    quantidades,
    # width=0.5,
    align='center',
    color=['k', 'y']
)

xlabel('Produtos')
ylabel('Quantidades')
title('Produtos x Quantidades')

axis(ymin=0, ymax=10)

# Barras horizontais
subplot(122)
barh(
    produtos,
    quantidades,
    align='center',
    color=['b', 'm']
)

xlabel('Quantidades')
ylabel('Produtos')
title('Produtos x Quantidades')

axis(xmin=0, xmax=10)

show()
