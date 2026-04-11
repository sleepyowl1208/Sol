import pytest
from testbook import testbook
from testbook.exceptions import TestbookRuntimeError

@testbook('Sol1_Hydrogen/C3_Vectors/vectors.ipynb')
def test_vectors_notebook(tb):
    # execute valid cells
    tb.execute_cell(list(range(6)))

    x = tb.ref("x")
    assert x.tolist() == [12, 8, 92]

    y = tb.ref("y")
    assert y.tolist() == [12, 8, 92]

    z = tb.ref("z")
    assert z.tolist() == [12, 8, 92]

    # test float96 raises error
    with pytest.raises(TestbookRuntimeError) as exc_info:
        tb.execute_cell(6)
    assert "AttributeError" in str(exc_info.value)
    assert "float96" in str(exc_info.value)

    # test float128 may raise error or succeed depending on platform (x86_64 linux usually has float128)
    try:
        tb.execute_cell(7)
    except TestbookRuntimeError as e:
        assert "AttributeError" in str(e)
        assert "float128" in str(e)
