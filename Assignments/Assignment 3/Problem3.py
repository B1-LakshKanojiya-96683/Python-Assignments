#3) Replace single element ‘b’ in given
# list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

GivenList = ["a","b","c","d","e"]

GivenList.pop(1)
GivenList.insert(1,[1,2,3])

print(f"{GivenList}")
