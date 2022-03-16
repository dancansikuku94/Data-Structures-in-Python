# Sets are unordered
# sets elements are unique , duplicate elements not allowed
# A set itself may be modified,but the elements contained in the set must be of an immutable type.
# Creating a set using inbuilt python function
numbers = set([1, 2, 3, 4])
print(numbers)
# Sets are unordered
letters = set(["foo", "bar", "foo", "faxx", "lette", "xx"])
print(letters)  # {'letter', 'xx', 'fax', 'bar', 'foo'}
# u can create a set from tuples or list as shown above and below
a = set((1, 2, 3, 4))
print(a)
# Sets methods .add() ,.discard(),.clear(),.pop()
set_colors = {"Black", "Green", "Blue", "Black", "White"}  # Creating set from scratch
print(set_colors)  # {'White', 'Green', 'Black', 'Blue'}
print(type(set_colors))  # Check data types # <class 'set'>
# Sets methods
aa = {"a", "b", "c", 1, 2, 3}  #
print(aa)  # {1, 2, 3, 'c', 'a', 'b'}
aa.add("rr")
print(f"Set aa after adding element rr is ->{aa}")  # {1, 2, 3, 'c', 'rr', 'a', 'b'}

aa.remove(3)
print(f"Set aa after removing 3 is ->{aa}")  # {1, 2, 'c', 'rr', 'a', 'b'}
aa.discard("a")
print(f"Set aa after applying discard method to a is ->{aa}")  # {1, 2, 'c', 'rr', 'b'}

print("Pop removes a random element ->", aa.pop())  # 1
print(f"Set aa after applying pop() method is ->{aa}")  # {2, 'c', 'rr', 'b'}

print(aa.clear())
# Modifying a set

# Sets operations

bb = {"aa", "bb", "cc", "dd", "ff"}
cc = {"bb", "gg", "kk", "ll", "mm"}
# Union - Is a set containing elements in either sets
print(
    f"After applying union operation ->{bb.union(cc)}"
)  # {'mm', 'aa', 'll', 'gg', 'ff', 'dd', 'bb', 'cc', 'kk'}
