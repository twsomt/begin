import sys
class ListObject:
    head_obj = None

    def __init__(self, data, next_obj=None):
            self.data = data
            self.next_obj = next_obj

    def link(self, obj):
        if not self.head_obj:
            self.head_obj = ListObject(obj)
        else:
            self.data = obj
        node = self.head_obj

        while node.next_obj:
            node = node.next_obj

        node.next_obj = ListObject(obj)

# lst_in = list(map(str.strip, sys.stdin.readlines())) 
lst_in = list(range(10))
print(*lst_in)

for lst_elem in lst_in:
    head_obj = ListObject(lst_elem)
    print(head_obj.data, end=' ')