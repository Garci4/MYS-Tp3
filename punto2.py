import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
import numpy as numpy
#Distribuciones
from scipy.stats import uniform
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import expon

class P2:

  tamaño_muestra = 1000

  def get_media(self, _muestra):
    return numpy.mean(_muestra)

  def get_desvio_estandar(self, _muestra):
    return numpy.nanstd(_muestra)

  def get_varianza(self, _muestra):
    return numpy.var(_muestra)

  def unifrome(self, min, max):
    muestra = uniform.rvs(size=self.tamaño_muestra, loc=min, scale=max)
    media = self.get_media(muestra)
    desvio_estandar = self.get_desvio_estandar(muestra)
    varianza =  self.get_varianza(muestra)
    print("muestra: ")
    print(muestra)
    print("media: " + str(media))
    print("desvio estandar: " + str(desvio_estandar))
    print("varianza: " + str(varianza))
    x = pd.Series(muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto2_graph/uniforme.png')

  def normal(self, media, desvio):
    muestra = norm.rvs(size=self.tamaño_muestra, loc=media, scale=desvio)
    media = self.get_media(muestra)
    desvio_estandar = self.get_desvio_estandar(muestra)
    varianza =  self.get_varianza(muestra)
    print("muestra: ")
    print(muestra)
    print("media: " + str(media))
    print("desvio estandar: " + str(desvio_estandar))
    print("varianza: " + str(varianza))
    x = pd.Series(muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto2_graph/normal.png')  

  def poisson(self, lambd):
    muestra = poisson.rvs(lambd, size=self.tamaño_muestra)
    media = self.get_media(muestra)
    desvio_estandar = self.get_desvio_estandar(muestra)
    varianza =  self.get_varianza(muestra)
    print("muestra: ")
    print(muestra)
    print("media: " + str(media))
    print("desvio estandar: " + str(desvio_estandar))
    print("varianza: " + str(varianza))
    x = pd.Series(muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto2_graph/poisson.png')  

  def exponencial(self, beta):
    muestra = expon.rvs(scale=beta, size=self.tamaño_muestra)
    media = self.get_media(muestra)
    desvio_estandar = self.get_desvio_estandar(muestra)
    varianza =  self.get_varianza(muestra)
    print("muestra: ")
    print(muestra)
    print("media: " + str(media))
    print("desvio estandar: " + str(desvio_estandar))
    print("varianza: " + str(varianza))
    x = pd.Series(muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto2_graph/exponencial.png')  

p2 = P2()
#p2.unifrome(0,1)
#p2.normal(0,1)
p2.exponencial(0.25)