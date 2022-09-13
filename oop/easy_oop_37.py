import sys
class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = list(range(10))

head_obj = ListObject(lst_in[0])
current_obj = head_obj
for i in range(1, len(lst_in)):
    next_obj = ListObject(lst_in[i])
    current_obj.link(next_obj)
    current_obj = next_obj