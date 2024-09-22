from Televisor import *
from Televisor import televisor

tv= televisor('sony', 'sony-123')


controle= ControleRemoto(tv)


controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)
