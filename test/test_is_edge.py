from main import is_edge

################
#  Small Cube  #
################

small_cube_dims = (3, 3)


def test_small_cube_top_left():
    val = is_edge(0, 0, small_cube_dims)
    assert val


def test_small_cube_left():
    val = is_edge(0, 2, small_cube_dims)
    assert val


def test_small_cube_top():
    val = is_edge(1, 0, small_cube_dims)
    assert val


def test_small_cube_right():
    val = is_edge(2, 1, small_cube_dims)
    assert val


def test_small_cube_bottom():
    val = is_edge(1, 2, small_cube_dims)
    assert val


def test_small_cube_center():
    val = is_edge(1, 1, small_cube_dims)
    assert not val


################
#  Large Cube  #
################

large_cube_dims = (24, 24)


def test_large_cube_bottom_right():
    val = is_edge(large_cube_dims[0] - 1, large_cube_dims[1] - 1, large_cube_dims)
    assert val


def test_large_cube_left():
    val = is_edge(0, 8, large_cube_dims)
    assert val


def test_large_cube_top():
    val = is_edge(13, 0, large_cube_dims)
    assert val


def test_large_cube_right():
    val = is_edge(large_cube_dims[0] - 1, 9, large_cube_dims)
    assert val


def test_large_cube_bottom():
    val = is_edge(21, large_cube_dims[1] - 1, large_cube_dims)
    assert val


def test_large_cube_1_2():
    val = is_edge(1, 2, large_cube_dims)
    assert not val


def test_large_cube_11_17():
    val = is_edge(11, 17, large_cube_dims)
    assert not val