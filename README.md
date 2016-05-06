# A Simple Trace Checker
Written in Python, it accepts MTL formulae.

### Example
```
# import the checker
from stc import *

# load the trace from file
trace = load_trace('filename.trace', separator=',')

# write a formula
a = ap('a', trace)
b = ap('b', trace)

formula = globally(implies(a, eventually(b, [0, 4])), [3, 7])

# print its truth values
print formula

# done
```

### Developing
```
$ source projrc
$ make test
```
