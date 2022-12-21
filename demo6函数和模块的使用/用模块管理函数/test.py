"""
from module1 import foo
# 输出 111
foo()

from module2 import foo

# 输出 222
foo()

"""

# 或者
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

"""
from module1 import foo
from module2 import foo

# 输出 222
foo()

"""

