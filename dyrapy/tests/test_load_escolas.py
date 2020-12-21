# Copyright (c) 2020 Marco Mangan <marco.mangan@gmail.com>
# License: BSD 3 clause

from dyrapy.datasets import load_escolas


def test_load_escolas():
    cadastro, matriculas = load_escolas()
    assert cadastro is not None
    assert matriculas is not None
