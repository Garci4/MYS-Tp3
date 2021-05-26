import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
import numpy as numpy
#Distribuciones
from scipy.stats import uniform, expon

class P3:

  tamaño_muestra = 1000
  muestra = None
  media = None
  desvio_estandar = None
  varianza = None
  muestra_exponencial = []

  def get_muestra(self):
    return self.muestra

  def get_media(self, _muestra):
    self.media = numpy.mean(_muestra)
    return self.media

  def get_desvio_estandar(self, _muestra):
    self.desvio_estandar = numpy.nanstd(_muestra)
    return self.desvio_estandar

  def get_varianza(self, _muestra):
    self.varianza = numpy.var(_muestra)
    return self.varianza

  def unifrome(self, min, max):
    self.muestra = uniform.rvs(size=self.tamaño_muestra, loc=min, scale=max)
    print("muestra: ")
    print(self.muestra)
    print("media: " + str(self.get_media(self.muestra)))
    print("desvio estandar: " + str(self.get_desvio_estandar(self.muestra)))
    print("varianza: " + str(self.get_varianza(self.muestra)))

    _file = open("muestra_3.txt", "w+")
    _muestra = str(self.muestra)
    _file.write(_muestra)    
    _file.close()

    x = pd.Series(self.muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto3_graph/uniforme.png')

  def transform_to_exponencial(self, _muestra):
    for x in _muestra:
      self.muestra_exponencial.append(-0.125 * numpy.log(x))

    x = pd.Series(self.muestra_exponencial, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto3_graph/inciso_b.png') 

  '''inciso c y d'''
  def exponencial(self, beta, _tamaño_muestra):
    muestra_c = expon.rvs(scale=beta, size=_tamaño_muestra)
    media = self.get_media(muestra_c)
    desvio_estandar = self.get_desvio_estandar(muestra_c)
    varianza =  self.get_varianza(muestra_c)
    print("muestra: ")
    print(muestra_c)
    print("media: " + str(media))
    print("desvio estandar: " + str(desvio_estandar))
    print("varianza: " + str(varianza))
    x = pd.Series(muestra_c, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto3_graph/inciso_c.png')  


p3 = P3()
#inciso a y b
#p3.unifrome(0,1)
#p3.transform_to_exponencial(p3.get_muestra())

#inciso c
#p3.exponencial(0.5, 1000)
#inciso d
p3.exponencial(0.5, 100)