#!/usr/bin/env python

"""
testing of chrombits_good.py code
"""

import sys
import chrombits_good

arr = chrombits_good.ChromosomeLocationBitArrays(fname=sys.argv[1])

CTCF = arr.copy()
BEAF = arr.copy()

CTCF.set_bits_from_file(sys.argv[2])
BEAF.set_bits_from_file(sys.argv[3])

program = BEAF.intersect(CTCF.complement())
program2 = program.a_and_not_b()

print program2