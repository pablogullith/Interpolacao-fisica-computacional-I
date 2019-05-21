#Autor: Pablo Gullith 
# Bibliotecas
from numpy import loadtxt, arange, size , linspace, zeros
from pylab import plot, show, xlabel, ylabel
dados = loadtxt("scattering.data", float)
x = dados[:,0]
y = dados[:,1]
soma = 0
prod = 0

#Interpolação de lagrange
def funcao_g(x, valores_lista_x, valores_lista_y):
    tam = len(valores_lista_y)
    soma = 0
    for n in range(0,tam):
        soma = soma + valores_lista_y[n]*prod(x, n, tam, valores_lista_x)
    return soma

#Produtório nº1
def prod(x, j, tam, lista):
    p = 1
    x_j = lista[j]
    for i in range(0, tam):
        if(i != j):
            p = p*((x - lista[i])/(x_j - lista[i]))
    return p

x_axis = []
y_axis = []

for i in arange(0, 200, 0.1):
    x_axis.append(i)
    y_axis.append(funcao_g(i, x, y))

#Plot do primeiro gráfico
plot(x_axis, y_axis,'c')
plot(x, y, "ko")
xlabel("Energia (MeV)")
ylabel("Seção Transversal")
show()

#Produtório nº2
def prod_n2(i,x1,x): 
    n = size(x1)
    p = 1.0
    for j in range(n):
        if (j != i):
            p = p * (x - x1[j])/(x1[i] - x1[j])
    return p


#Interpolação de lagrange 
def funcao_g2(xa,ya,n): 

#Laço 1  
    for t in range(0,xa.size,n):
        x1 = xa[t:t+n+1] 
        y1 = ya[t:t+n+1]
        M = linspace(x1[0],x1[-1],100)
        N = zeros(M.size,float)
        k = size(x1)

#Laço 2        
        for w in range(M.size):
            GM = 0.0

#Laço 3           
            for i in range(k):
                GM = GM + y1[i]*prod_n2(i,x1,M[w])
            N[w] = GM
        
        
#Plot do segundo gráfico 
            
        plot(M,N,'c')

    xlabel("Energia (MeV)")
    ylabel("Seção Transversal") 
    plot(x,y,"ko") 
    show()


N = 2
funcao_g2(x,y,N)  
