def say_saimon(func):
    x = 'Саймон сказал:'
    return f'{x} {func()}'

@say_saimon
def hi():
    return 'привет'

print(hi)

