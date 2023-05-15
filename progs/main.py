from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.funI())

""" v. 2
from sys import path
path.append('..\\packages')

from extra.iota import funI
print(funI())


"""

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())


