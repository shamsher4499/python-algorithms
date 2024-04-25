class ClassList(list):
    def __hash__(self):
        return 0

_dict = {}
_list = ClassList([1, 2, 3])
_dict[_list] = 'Added'
# print(_dict)

class MyDict(dict):
    def __missing__(self, key):
        self[key] = rv = []
        return rv

m = MyDict()
m["foo"].append(1)
m["foo"].append(2)

# print(dict(m))  # {'foo': [1, 2]}
# print(m["x"])   # []

set_ex = frozenset({1, 2, 3})
dict_obj = {set_ex: "This is a Set"}