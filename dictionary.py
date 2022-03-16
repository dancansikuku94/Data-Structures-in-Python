# A data structure in python which is mutable
# Elements are accessed via keys
# Dictionaries are dynamic they can grow and shrink
# Dictionaries contain key-value pairs
teams_dictionary = {"A": "Man City", "B": "Ars", "C": "Che"}
print(teams_dictionary)  # {'A': 'Man City', 'B': 'Ars', 'C': 'Che'}
# U can also create dictionaries using python in-built function dict()
# The argument to dict() should be a sequence of key-value pairs. A list of tuples works well for this:
color_teams_dictionary = dict(
    [("Blue", "Chelsea"), ("Red", "Man Utd"), ("White", "Swansea"), ("Black", "Tote")]
)
print(
    color_teams_dictionary
)  # {'Blue': 'Chelsea', 'Red': 'Man Utd', 'White': 'Swansea', 'Black': 'Tote'}
# 1. Accesing dictionary Values
# A value is retrieved from a dictionary by specifying its corresponding key in square brackets
print(teams_dictionary["B"])  # Ars
# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value
teams_dictionary["D"] = "Liverpool"
print(
    f"Teams dictionary after adding liverpool is ->{teams_dictionary}"
)  # {'A': 'Man City', 'B': 'Ars', 'C': 'Che', 'D': 'Liverpool'}
# Updating dictionary , just specify the key to be updated
teams_dictionary["D"] = "Barcelona"
print(
    f"Teams dictionary after updating the dictionary is ->{teams_dictionary}"
)  # {'A': 'Man City', 'B': 'Ars', 'C': 'Che', 'D': 'Barcelona'}
# Deleting an element in a dictionary use del word specifying the key
del teams_dictionary["D"]
print(
    f"Teams dictionary after deleting Barcelona is ->{teams_dictionary}"
)  # {'A': 'Man City', 'B': 'Ars', 'C': 'Che'}
# Building a dictionary incrementally
person_dictionary = {}
# Check the type of data structure created
print(type(person_dictionary))  # <class 'dict'>
# Adding items in the dictionary
person_dictionary["firstName"] = "Dan"
person_dictionary["lastName"] = "Sikuku"
person_dictionary["gender"] = "Male"
person_dictionary["location"] = "Nairobi"
person_dictionary["pet"] = {"A": "B", "C": "D"}
person_dictionary["courses"] = ["introduction to C", "Data structures", "Algorithms"]
print(
    f"Personal Dictionary after adding items to the empty dictionary is ->{person_dictionary}"
)
# Retrieving values in the sub-lists requires additional key
cc = person_dictionary["pet"]["A"]
print(f"Results after retrieving B is ->{cc}")  # B
dd = person_dictionary["courses"][2]
print(
    f"Results of personal dictionary when accesing at index 2 is ->{dd}"
)  # Algorithms
# Duplicate keys are not allowed
# Dictionary keys are immutable  like float , int so tuples can be a dictionary key
ff = {(1, 2): "AA", (3, 4, "CC"): "WW"}
print(ff[1, 2])
# Dictionary with not in and in operators
color_dictionary = {"A": "Black", "B": "Grey", "C": "Green", "D": "Maroon"}
ab = "A" in color_dictionary
print(ab)  # True
ad = "B" not in color_dictionary
print(ad)  # False
# Built - in Dictionary functions .clear(),.get(),.items(),.keys(),.values(),.pop() .popitem() removes a key pair in the dict
# update() merges a dictionary with another dictionary
