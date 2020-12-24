# Copyright (c) 2020 Marco Mangan <marco.mangan@gmail.com>
# License: BSD 3 clause

"""
Base IO code for all datasets
"""
import logging

import pandas
from os.path import dirname, join


def load_ouvidoria():
    """Load and return the dadosabertos.poa.br ouvidoria dataset.

    The ouvidoria dataset is a public open dataset from Prefeitura de Porto Alegre, Rio Grande do Sul, Brazil.

    Examples
    --------
    >>> from dyrapy.datasets import load_ouvidoria
    >>> data = load_ouvidoria()
    >>> data.head()

    """
    module_path = dirname(__file__)
    ouvidoria_csv_filename = join(module_path, 'data', 'ouvidoria.csv')

    data = pandas.read_csv(ouvidoria_csv_filename, sep=';', na_values=".")

    logging.info('Data head...')
    logging.info(data.head())

    logging.info('Data describe..')
    logging.info(data.describe())

    logging.info("Recoding categories...")
    data.descricao = data.descricao.astype('category')
    data.sigla = data.sigla.astype('category')
    data.statussolicitacao = data.statussolicitacao.astype('category')
    data.tipofim = data.tipofim.astype('category')

    logging.info('Recodind dates..')
    data.data_extracao = pandas.to_datetime(data.data_extracao)
    data.dataregistro = pandas.to_datetime(data.dataregistro)
    data.datafinalprevista = pandas.to_datetime(data.datafinalprevista)
    data.dataenvioresposta = pandas.to_datetime(data.dataenvioresposta)

    logging.info("Boxplot and Scatter Matrix")
    data['previsto'] = (data.datafinalprevista - data.dataregistro).astype('timedelta64[D]')
    data['realizado'] = (data.dataenvioresposta - data.dataregistro).astype('timedelta64[D]')
    data['delta'] = data.previsto - data.realizado

    return data


def load_escolas():
    """

    Returns
    -------

    """
    module_path = dirname(__file__)
    cadastro_csv_filename = join(module_path, 'data', 'cadastro_escolas.csv')
    matriculas_csv_filename = join(module_path, 'data', 'matriculas_escolas.csv')

    data_cadastro = pandas.read_csv(cadastro_csv_filename, sep=';', na_values=".")
    data_matriculas = pandas.read_csv(matriculas_csv_filename, sep=';', na_values=".")

    logging.info('Data head...')
    logging.info(data_cadastro.head())
    logging.info(data_matriculas.head())

    logging.info('Data describe..')
    logging.info(data_cadastro.describe())
    logging.info()
    logging.info(data_matriculas.describe())

    logging.info('Recodind dates..')
    data_cadastro.data_extracao = pandas.to_datetime(data_cadastro.data_extracao)
    data_matriculas.data_extracao = pandas.to_datetime(data_matriculas.data_extracao)

    return data_cadastro, data_matriculas
