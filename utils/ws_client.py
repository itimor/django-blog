# -*- coding: utf-8 -*-
# author: itimor

a = """
aaaaa

-- readmore

> eqeqw
> 312321
"""

readmore_index = a.find('-- readmore')
print(readmore_index)
print(a[:readmore_index])

import re

comp = re.compile(r'-- readmore')
b = re.sub(comp, '', a)
print(b)
