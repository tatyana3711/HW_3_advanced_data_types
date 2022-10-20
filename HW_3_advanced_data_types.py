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
print("Anna has {0} apples and {1} peaches.".format(apples, peaches))

# 7. By using keyword arguments into the curly braces.
print("Anna has {a} apples and {p} peaches.".format(a=apples, p=peaches))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)



# 9. With f-strings and variables
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %s apples and %s peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
d = {apples: 5, peaches: 10}
print(f"Anna has {d[apples]} apples and {d[peaches]} peaches.")