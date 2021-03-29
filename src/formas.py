class Figura:
  def __init__(self, tamanho=(12, 12)):
    self.figure, self.axes = plt.subplots(figsize=tamanho)
    self.axes.set_xlim([-10, 10])
    self.axes.set_ylim([-10, 10])
    self.axes.set_aspect( 1 )
    
def criar_figura():
  return Figura()

def adicionar(forma, figura):
  figura.axes.add_artist( forma.desenho )

def desenhar(figura, titulo=""):
  plt.title(titulo)
  plt.axis('off')
  plt.show()

class Circulo:
  def __init__(self, raio, centro=(0, 0), cor="#000000", transparencia=1.0):
    self.raio = raio
    self.centro = centro
    self.cor = cor
    self.desenho = plt.Circle(centro, raio, color=cor, alpha=transparencia)
