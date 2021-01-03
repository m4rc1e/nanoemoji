from nanoemoji.util import build_n_ary_tree

import pytest


@pytest.mark.parametrize(
    "lst, n, expected",
    [
        ([0], 2, [0]),
        ([0, 1], 2, [0, 1]),
        ([0, 1, 2], 2, [[0, 1], 2]),
        ([0, 1, 2], 3, [0, 1, 2]),
        ([0, 1, 2, 3], 2, [[0, 1], [2, 3]]),
        ([0, 1, 2, 3], 3, [[0, 1, 2], 3]),
        ([0, 1, 2, 3, 4], 3, [[0, 1, 2], 3, 4]),
        ([0, 1, 2, 3, 4, 5], 3, [[0, 1, 2], [3, 4, 5]]),
        (list(range(7)), 3, [[0, 1, 2], [3, 4, 5], 6]),
        (list(range(8)), 3, [[0, 1, 2], [3, 4, 5], [6, 7]]),
        (list(range(9)), 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]),
        (list(range(10)), 3, [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], 9]),
        (list(range(11)), 3, [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], 9, 10]),
        (list(range(12)), 3, [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [9, 10, 11]]),
        (list(range(13)), 3, [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [9, 10, 11], 12]),
        (
            list(range(14)),
            3,
            [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [9, 10, 11], [12, 13]],
        ),
        (
            list(range(15)),
            3,
            [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [9, 10, 11], [12, 13, 14]],
        ),
        (
            list(range(16)),
            3,
            [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], 15]],
        ),
        (
            list(range(23)),
            3,
            [
                [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
                [[18, 19, 20], 21, 22],
            ],
        ),
        (
            list(range(27)),
            3,
            [
                [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
                [[18, 19, 20], [21, 22, 23], [24, 25, 26]],
            ],
        ),
        (
            list(range(28)),
            3,
            [
                [
                    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                    [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
                    [[18, 19, 20], [21, 22, 23], [24, 25, 26]],
                ],
                27,
            ],
        ),
        (list(range(257)), 256, [list(range(256)), 256]),
        (list(range(258)), 256, [list(range(256)), 256, 257]),
        (list(range(512)), 256, [list(range(256)), list(range(256, 512))]),
        (list(range(512 + 1)), 256, [list(range(256)), list(range(256, 512)), 512]),
        (
            list(range(256 ** 2)),
            256,
            [list(range(k * 256, k * 256 + 256)) for k in range(256)],
        ),
    ],
)
def test_build_n_ary_tree(lst, n, expected):
    assert build_n_ary_tree(lst, n) == expected
