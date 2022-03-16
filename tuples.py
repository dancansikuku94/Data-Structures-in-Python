# Tuples are immutable , ones created they cannot be modified through deletion , insertion
# an ordered collection objects
# use parenthesis when creating a tuple
t = ("foo", "bar", "bazz", "corge")
# operations are similar to that of a list
# reversing a tuple
print(t[::-1])  # ('corge', 'bazz', 'bar', 'foo')
# Accessing element by index
print(t[0])  # foo
# Tuples unpacking
# The number of values on the left must be equal to the number of elements in the tuple
t = ("foo", "bar", "baz", "qux")
(s1, s2, s3, s4) = t
print(s2)  # bar
# packing and unpacking can be combined
(s1, s2, s3, s4) = ("foo", "bar", "baz", "qux")
print(s4)  # qux
t1 = 1, 2, 3, 4, 5, 6  # you can create tuples without necessary including brackets
print(t1)  # (1, 2, 3, 4, 5, 6)
# swapping in python
kk = "Sikuku"
ll = "Dancan"
print(f"Before swapping-> {kk} {ll}")
kk, ll = ll, kk
print("After swapping->", kk, ll)
# print(a, b)
