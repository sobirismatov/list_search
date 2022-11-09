def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    mx=data[0]
    for i in data:
        if i>mx:
            mx=i
    return mx
print(find_max([1,2,3]))
    