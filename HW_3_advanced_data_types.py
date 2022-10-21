#1. Define the id of next variables:
int_a = 55
print("id variable int_a", id(int_a))
str_b = 'cursor'
print("id variable str_b", id(str_b))
set_c = {1, 2, 3}
print("id variable set_c", id(set_c))
lst_d = [1, 2, 3]
print("id variable lst_d", id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print("id variable dict_e", id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print("lst_d Append 4 and 5:", lst_d)
print("id variable lst_d", id(lst_d))

# 3. Define the type of each object from step 1.
print(list(map(type, (int_a, str_b, set_c, lst_d, set_c, dict_e))))

#4. Check the type of the objects by using isinstance.
print("int_a is it int?",isinstance(int_a, int))
print("str_b id it str?", isinstance(str_b, str))
print("set_c is it  set?", isinstance(set_c, set))
print("lst_d is it list?", isinstance(lst_d, list))
print("dict_e is it dict?", isinstance(dict_e, dict))

#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."

apples = 6
peaches = 7

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(apples, peaches))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(peaches, apples))

# 7. By using keyword arguments into the curly braces.
print("Anna has {a} apples and {p} peaches.".format(a=apples, p=peaches))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {apple:5} apples and {peache:3} peaches.".format(apple=6, peache=7))


# 9. With f-strings and variables
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %s apples and %d peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
d = {apples: 6, peaches: 7}
print(f"Anna has {d[apples]} apples and {d[peaches]} peaches.")

#12. Convert (1) to list comprehension
list_comprehension_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension_1)

#13. Convert (2) to regular for with if-else
lst1 = []
for num in range(10):
    if num % 2 == 0:
        lst1.append(num // 2)
    else:
        lst1.append(num * 10)
print(lst1)

#14. Convert (3) to dict comprehension.
dict_comprehension = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)

#15*. Convert (4) to dict comprehension.
dict_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)

#16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)

#17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)

#18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else x

#19*. Convert (8) to regular function
def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y

#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_lmb = list(map(lambda x: x*2, lst_to_sort))
print(lst_lmb)

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

lst_lmb = list(map(lambda x, y: x**y, list_A, list_B))
print(lst_lmb)

#24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
filtered = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(filtered)

#25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
filtered_2 = list(filter(lambda x: x < 0, b))
print(filtered_2)

#26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
common = list(filter(lambda n: n in list_1, list_2))
print(common)