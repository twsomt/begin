class ListObject:
    def __init__(next_obj=None, data):
        self.next_obj = next_obj
        self.data = data

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

#some_code
