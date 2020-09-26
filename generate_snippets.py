#!/usr/bin/env python3

import os
import json
if "GLOBAL":
    path = "/Users/nishio/Library/Application Support/Code/User/snippets/python.code-snippets"
else:
    DIR = os.path.dirname(__file__)
    path = os.path.join(DIR, ".vscode/snippet.code-snippets")

snippets = {}


def push(prefix, desc, body=None):
    if not body:
        body = desc
        desc = prefix
    body = body.strip()
    if desc in snippets:
        print(f"{desc} already exists")
        desc = desc + "'"
    snippets[desc] = dict(
        scope="python",
        prefix=prefix,
        body=body.splitlines(),
        description=desc
    )


push("profile", """
try:
    profile
except:
    def profile(f): return f
""")

push("test", '''
T${1:} = """
$2
"""
TEST_T$1 = """
>>> as_input(T$1)
>>> main()
${3:result}
"""
''')

push("dp", """
debug("$2$1", $1)
""")

push("perf", """
start_time = perf_counter()
${TM_SELECTED_TEXT}
debug(f"$1: {(perf_counter() - start_time):.2f}")
""")

push("impperf", "from time import perf_counter")

push("bp", """
if ${1:True}:
    import pdb
    pdb.set_trace()
""")

# def
push("deftest", """
def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)
""")

push("defdebug", """
def debug(*x):
    print(*x, file=sys.stderr)
""")

push("defdebugindent", """
debug_indent = 0
def debug(*x):
    import sys
    global debug_indent
    x = list(x)
    indent = 0
    if x[0].startswith("enter") or x[0][0] == ">":
        indent = 1
    if x[0].startswith("leave") or x[0][0] == "<":
        debug_indent -= 1
    x[0] = "  " * debug_indent + x[0]
    print(*x, file=sys.stderr)
    debug_indent += indent
""")

push("ifmain", """
if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
""")

# import
push("impdef", "from collections import defaultdict")
push("impcou", "from collections import Counter")
push("impdeq", "from collections import deque")
push("impheap", "from heapq import heappush, heappop")
push("impnp", "import numpy as np")

path = os.path.join(path)
json.dump(snippets, open(path, "w"), indent=2)
