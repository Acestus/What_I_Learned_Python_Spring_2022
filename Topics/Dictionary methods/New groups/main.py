# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

active_groups = int(input())
class_sizes = []
kindergarten_dict = dict.fromkeys(groups)

for i in range(active_groups):
    kindergarten_dict[groups[i]] = int(input())
print(kindergarten_dict)
