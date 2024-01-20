from pylab import pie
from pylab import show
from pylab import title


produtos = ['A', 'B', 'C', 'D', 'E']
quantidades = [6, 10, 15, 3, 12]
cores = ['b', 'y', 'm', 'g', 'r']

pie(
    quantidades,
    labels=produtos,
    colors=cores,
    radius=1,
    autopct='%.1f%%'
)

title('Venda de Produtos')

show()
