def my_func(a, b, *args, nickname='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(nickname, age)
    print(kwargs)

my_func(1, 2, 3, 4, nickname='twsomt', age=29, job='dev', language='Python')