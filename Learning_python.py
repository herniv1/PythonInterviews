# swap two variables
a = 5 
b = 10
a, b = 3,6
print(a)
print(b)

# Data structure
###############################

list_a = [2, 5, 8, 12, 5, 37, 92, 34, 1, 4]
list_a.append(19)
list_a.insert(0,44)
list_a.remove(2)
print(list_a)
list_a.pop(2)
print(list_a)
c = list_a.index(5)
print(c)
smallest = 1

dna =10
dna = 20 & 1
print(dna)

list_a = [2, 5, 8, 12, 5, 37, 92, 34, 1, 4]
print(list_a)
lista_c = list_a[::-1]
print(lista_c)
word = "Samuel Hernandez"
print(word[::-1])

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["age"] = 26  # Update
person["gender"] = "Female"  # Add new key-value pair
print(person)
del person['city']
print(person)

squares = {x: x**2 for x in range(1, 6)}
print(squares)  

def first_unique_char(s):
    from collections import Counter
    count = Counter(s)
    
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1
result = first_unique_char('loveleetcode')
print(result)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}






# prefix_map = {(0, 0): 1}

# odd_prefix = 0
# even_prefix = 0
# count = 0
# prefix_map = {(0, 0): 1}
# componentValue = [2, 4, 3]
# n = len(componentValue)
# for i in range(n):
#     if componentValue[i] % 2 == 1:
#         odd_prefix += 1
#     else:
#         even_prefix += 1

#     key = (odd_prefix % 2, even_prefix % 2)
#     if key in prefix_map:
#         count += prefix_map[key]
#         prefix_map[key] += 1
#     else:
#         prefix_map[key] = 1
# print(prefix_map)

# def count_balanced_subarrays(componentValue):
#     n = len(componentValue)
#     balanced_count = 0

#     # Iterate over all possible subarrays
#     for start in range(n):
#         odd_count = 0
#         even_count = 0

#         for end in range(start, n):
#             if componentValue[end] % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1

#             # Check if the subarray is balanced
#             if odd_count % 2 == 1 and even_count % 2 == 0:
#                 balanced_count += 1

#     return balanced_count

# # Example usage
# componentValue = [2, 4, 3]
# print(count_balanced_subarrays(componentValue)) 
