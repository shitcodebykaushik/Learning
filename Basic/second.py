dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'c': 6}
combined_dict = {}

for key in dict1.keys():
 combined_dict[key] = [dict1[key], dict2[key]]

print(combined_dict)