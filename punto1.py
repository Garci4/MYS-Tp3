import matplotlib.pyplot as pyplot
import seaborn as sns
import numpy as numpy
from scipy.stats import poisson


class P1:
  muestra = None
  media = None
  desvio_estandar = None
  varianza = None

  def resultados(self):
    return {
      'muestra': self.muestra,
      'media': self.media,
      'desvio_estandar': self.desvio_estandar,
      'varianza': self.varianza
    }

  '''
  La muestra tiene que ser de 100 numeros, generados aleatoriamente.
  '''
  def get_muestra(self):
    mu = 4
    datos = poisson.rvs(mu, size=100)
    print("Muestra obtenida: ")
    print(datos)
    self.muestra = datos

  def get_media(self):
    media = numpy.mean(self.muestra)
    print("Media obtenida: ")
    print(media)
    self.media = media

  def get_desvio_estandar(self):
    self.desvio_estandar = numpy.nanstd(self.muestra)
    print("desvío estandar obtenido: ")
    print(self.desvio_estandar)

  def get_varianza(self):
    self.varianza = numpy.var(self.muestra)
    print("varianza obtenida: ")
    print(self.varianza)

  def get_graficos(self):
    import pandas as pd
    x = pd.Series(self.muestra, name="x variable")
    ax = sns.distplot(x)
    pyplot.savefig('punto1.png')


p1 = P1()
p1.get_muestra()
p1.get_media()
p1.get_desvio_estandar()
p1.get_varianza()
p1.get_graficos()