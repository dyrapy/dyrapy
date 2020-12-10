print('Open file...')
import pandas
data = pandas.read_csv('../dyrapy/datasets/data/ouvidoria.csv', sep=';', na_values=".")

print('Data head...')
print(data.head())

print('Data describe..')
print(data.describe())

print("Recoding categories...")
data.descricao = data.descricao.astype('category')
data.sigla = data.sigla.astype('category')
data.statussolicitacao = data.statussolicitacao.astype('category')
data.tipofim = data.tipofim.astype('category')

print('Recodind dates..')
data.data_extracao = pandas.to_datetime(data.data_extracao)
data.dataregistro = pandas.to_datetime(data.dataregistro)
data.datafinalprevista = pandas.to_datetime(data.datafinalprevista)
data.dataenvioresposta = pandas.to_datetime(data.dataenvioresposta)

print("Boxplot and Scatter Matrix")
data['previsto'] = (data.datafinalprevista - data.dataregistro).astype('timedelta64[D]')
data['realizado'] = (data.dataenvioresposta - data.dataregistro).astype('timedelta64[D]')
data['delta'] = data.previsto - data.realizado

data.boxplot()

from pandas.plotting import scatter_matrix
scatter_matrix(data[['previsto', 'realizado', 'delta']])

import matplotlib.pyplot as plt
plt.show()
