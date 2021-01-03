# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Small helper functions."""

import os
from pathlib import Path
import shlex
from typing import List


def only(filter_fn, iterable):
    it = filter(filter_fn, iterable)
    result = next(it)
    assert next(it, None) is None
    return result


def expand_ninja_response_files(argv: List[str]) -> List[str]:
    """
    Extend argument list with MSVC-style '@'-prefixed response files.

    Ninja build rules support this mechanism to allow passing a very long list of inputs
    that may exceed the shell's maximum command-line length.

    References:
    https://ninja-build.org/manual.html ("Rule variables")
    https://docs.microsoft.com/en-us/cpp/build/reference/at-specify-a-compiler-response-file
    """
    result = []
    for arg in argv:
        if arg.startswith("@"):
            with open(arg[1:], "r") as rspfile:
                rspfile_content = rspfile.read()
            result.extend(shlex.split(rspfile_content))
        else:
            result.append(arg)
    return result


def fs_root() -> Path:
    return Path("/").resolve()


def rel(from_path: Path, to_path: Path) -> Path:
    # relative_to(A,B) doesn't like it if B doesn't start with A
    return Path(os.path.relpath(str(to_path.resolve()), str(from_path.resolve())))


def build_n_ary_tree(leaves, n):
    """Build N-ary tree from sequence of leaf nodes.

    Return a list of lists where each non-leaf node is a list containing
    max n nodes.
    """
    assert len(leaves) > 0
    assert n > 1

    tree = list(leaves)
    # group values into sub-lists until none contains > n items
    while len(tree) > n:
        tree = [tree[k : k + n] for k in range(0, len(tree), n)]

    # try to compress the right-most branches to minimize the total number of nodes
    stack = [tree]
    while stack:
        node = stack.pop()

        while isinstance(node[-1], list) and len(node) - 1 + len(node[-1]) <= n:
            # unpack and replace the last item with its children
            node[-1:] = node[-1]

        # only the last non-leaf node at each level can be incomplete, so we
        # only need to traverse those
        if isinstance(node[-1], list):
            stack.append(node[-1])

    return tree
