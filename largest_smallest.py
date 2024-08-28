iteration = [5,2,19,56,83,65,4,21,54,28,79]

def largest(values: list) -> str:
    largest_num = None
    for value in values:
        # check if number is larger then previous one and assign if yes
        if largest_num is None or value > largest_num:
            largest_num = value 
    # return largest_num
    return f"Largest_num: {largest_num}"

def smallest(values: list) -> str:
    smallest_num = None
    for value in values:
        if smallest_num is None or value < smallest_num:
            smallest_num = value
    return f"Smallest_num: {smallest_num}"

print(largest(iteration))
print(smallest(iteration))
