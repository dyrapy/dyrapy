# Copyright (c) 2020 Marco Mangan <marco.mangan@gmail.com>
# License: BSD 3 clause

from dyrapy.datasets import load_ouvidoria

def test_load_ouvidoria():
    data = load_ouvidoria()
    assert data is not None
