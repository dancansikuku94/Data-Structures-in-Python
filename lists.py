# A list is a collection of arbitrary objects somewhat to arrays in other programming language but more flexible.
#  It is an ordered collection of
#  objects
# 1. Lists are ordered
list_color = ["Red", "Blue", "Green"]
list_numbers = [1, 2, 3, 4, 5]
# Print the elements of a list
print(list_color + list_numbers)  # List concatenation
# Print element at index 1
print(list_color[1])
# Blue
# 2.Lists Can Contain Arbitrary Objects
# Elements can be of a varying types
a = ["Black", 1, 8, 2.45, "foobar"]
print(a)  # ['Black', 1, 8, 2.45, 'foobar']
# Reversing a list
print(list_numbers[::-1])  # [5, 4, 3, 2, 1]
# using not in and in operators in  lists
print(8 in list_numbers)  # False
# using not in
print(9 not in list_numbers)  # True
# Replication operator in lists
print(list_numbers * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(a * 2)
# In built functions in list i.e max(),min(),len()
print(max(list_numbers))  # 5
print(min(list_numbers))  # 1
print(len(list_numbers))  # 5

# 3. Lists can be nested
a = ["a", ["b", "c", ["dd", "ee"]], "ii", "jj"]
b = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]
print(a)
print(b)
print(
    len(a)
)  # 4 , the length of the list is 4 since we are having 3 strings and 1 sub-lists , the individual elements in sublits dont count to the length
print(len(b))
# Accessing the element in a nested list
print(b[1][0])  # bb
print(b[3][1])  # ii
# 4. Lists are mutable
# once a list has been created its elements can be deleted , shifted or added
# Modifying a single value
c = [1, 2, 8, 4]
c[1] = 5
print(c)  # [1, 5, 8, 4] 2 has been modified
# Delete an element using Del command
del c[3]
print(c)  # [1,5,8]
# Append and prepend functions in a list
d = ["a", "b", "c"]
d += ["ff"]  # is added as a singleton
print(d)  # ['a', 'b', 'c', 'ff']
# Append function
d.append(3)
print(d)  # ['a', 'b', 'c', 'ff', 3]
# .extend() method adds elements to the end of a list but the argument is iterable . Behaves like the plus operator since it modifies the list in place
e = ["a", "b"]
e.extend([1, 2, 3])
print(e)  # ['a', 'b', 1, 2, 3]
# .insert() method inserts an element at the specified index
dd = [5, 6, 7, 8, 9]
dd.insert(1, 100)
print(dd)  # [5, 100, 6, 7, 8, 9]
# .remove() method removes an object in the list
ff = ["aa", "bb", "cc", "dd", "ff"]
ff.remove("bb")
print(ff)  # ['aa', 'cc', 'dd', 'ff']
# pop() method  differs from remove() method since you specify the index of the element to be removed and it returns the removed element
gg = ["purple", "green", "black", "white"]
print(gg.pop(0))  # purple
print(gg)  # ['green', 'black', 'white']

# Lists are dynamic
# when items are added it grows as needed and shrinks as needed
