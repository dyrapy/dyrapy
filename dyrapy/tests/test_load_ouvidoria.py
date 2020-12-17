from dyrapy.datasets import load_ouvidoria


def test_load_ouvidoria():
    data = load_ouvidoria()
    assert data is not None
