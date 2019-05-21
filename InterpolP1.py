#Autor: Pablo Gullith
#Bibliotecas
from numpy import linspace, zeros, loadtxt 
from scipy.interpolate import interp1d
from pylab import plot, show, legend, ylabel, xlabel, clf

informacoes = loadtxt("scattering.data")

xinf = informacoes[:,0]
yinf = informacoes[:,1]

def funcao(x1,y1,x2,y2,x):
    return 1/(x2-x1)*(y1*(x2-x)+y2*(x-x1))

tam = xinf.size

for i in range(tam-1): 
    m1 = linspace(xinf[i],xinf[i+1],100)
    m = m1.size
    m2 = zeros(m,float)
    for j in range(m):        
        m2[j] = funcao(xinf[i],yinf[i],xinf[i+1],yinf[i+1],m1[j])
    plot(m1,m2,'b')


plot(xinf,yinf,"ko",label="Dados experimentais")
legend()
show()
clf()
fnum1 = interp1d(xinf,yinf)
fnum2 = interp1d(xinf,yinf,kind="cubic") 
e = linspace(0,200,1000)
Fnum1 = fnum1(e)
Fnum2 = fnum2(e)
plot(e,Fnum1,label="Interpolação Linear")
xlabel("Energia (MeV)")
ylabel("Seção de choque")
plot(xinf,yinf,"ko",label="Pontos experimentais")
legend()
show()
clf()
plot(e,Fnum2,label="interpolação Linear")
xlabel("Energia (MeV)");
ylabel("Seção de choque");
plot(xinf,yinf,"ko",label="Pontos experimentais")
legend()
show()

