global_variable = 'Глобальная'


def some_func(passed_variable):
    local_variable = 'Локальная'

    def inside_func():
        inside_local_variable = 'Внутренняя'
        return(f'{global_variable} '
               f'{local_variable} '
               f'{passed_variable} '
               f'{inside_local_variable}')
print(inside_func())

some_func('Параметр')
# Будет намечатано: Глобальная Локальная Параметр Внутренняя