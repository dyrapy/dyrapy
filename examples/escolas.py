# Copyright (c) 2020 Marco Mangan <marco.mangan@gmail.com>
# License: BSD 3 clause

from dyrapy.datasets import load_escolas

print('Dyrapy Examples - Escolas Dataset')
print('=================================')

print('Open files...')
data_cadastro, data_matriculas = load_escolas()

print('Data head...')
print(data_cadastro.head())
print(data_matriculas.head())

print('Data describe..')
print(data_cadastro.describe())
print(data_matriculas.describe())

