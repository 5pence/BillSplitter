# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
number = int(input())
amount = []
for num in range(0, 9):
    if num < number:
        amount.append(int(input()))
    else:
        amount.append(None)
fruity_dictionary = dict(zip(groups, amount))
print(fruity_dictionary)
