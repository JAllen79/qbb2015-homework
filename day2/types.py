#!/usr/bin/env python

#Integer, can be unlimited size
i = 10000

#Floating point / real number using a decimal
f = 0.333

i_as_f = float(i)
f_as_i = int(f)

#String
s = "A String"

#Boolean
truthy = True
falsy = False

#Dictionary
d1 = {"key1": "value 1", "key2": "value 2"}
d2 = dict(key1="value1", key2="value2")
d3 = dict([("key1", "value1"), ("key2", "value2")])
#d3 is a list of tuples that is made into a dictionary

#Lists
l = [1,2,3,4]
#Lists are mutable and have elements all of the same type by convention, except for nested lists.

#Tuple
t = (1, "foo", 5.0)
#Tuples are immutable, cannot be appended to etc, contain multiple types.

for value in (i, f, s, truthy, l, t, d1, d2, d3):
    print value, type(value)
