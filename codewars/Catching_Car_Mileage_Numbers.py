def is_interesting(x, awesome_phrases):
    '''
    Функция определяет, является ли число "интересным".
    Возвращает 2 если число интересное, 1 если интересное число есть в двух последующих числах, 0 во всех остальных случаях.
    Интересные числа - это 3 или более значные числа, которые соответствуют одному или нескольким из следующих критериев:
    - Любая цифра, за которой следуют все нули: 100, 90000
    - Каждая цифра - это одно и то же число: 1111
    - Цифры идут последовательно, дополняя *: 1234
    - Цифры идут последовательно, уменьшаясь на **: 4321
    - Цифры представляют собой палиндром: 1221 или 73837
    - Цифры соответствуют одному из значений в массиве awesome_phrases
    * Для увеличивающихся последовательностей 0 должно быть после 9, а не перед 1, как в 7890.
    ** Для уменьшающихся последовательностей 0 должно быть после 1, а не перед 9, как в 3210.
    '''
    
    def checker(x):
        if x > 99:
            x = str(x)
            def is_round_num(x):
                '''Любая цифра, за которой следуют все нули: 100, 90000.'''
                return x.count('0') == len(x) - 1

            def is_one_component(x):
                '''Каждая цифра - это одно и то же число: 1111'''
                return len(set(x)) == 1
            
            def is_num_incementing_or_decrementing(x):
                '''Цифры идут последовательно, дополняя: 1234
                   или
                   Цифры идут последовательно, уменьшаясь на: 4321
                '''
                x = list(map(int, x))
                y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                z = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
                i, j = y.index(x[0]), z.index(x[0])
                return x == y[i:i+len(x)] or x == z[j:j+len(x)] 

            def is_palindrom(x):
                '''Является ли число палиндромом?'''
                return x == x[::-1]

            def is_in_awesome(x):
                '''Находится ли число в списке awesome_phrases?'''
                return int(x) in awesome_phrases

            return any(i for i in (is_round_num(x),
                                  is_one_component(x),
                                  is_num_incementing_or_decrementing(x),
                                  is_palindrom(x),
                                  is_in_awesome(x)))
        else:
            return False

    if checker(x): return 2
    elif any(checker(i) for i in range(x + 1, x + 3)): return 1
    else: return 0


def testing():
    # тестовые данные
    # ((аргументы для функции), правильный ответ)
    test_data = (
        # ((number, awesome_phrases), right_answer)
        ((3, [1337, 256]), 0),
        ((3236, [1337, 256]), 0),
        ((11207, []), 0),
        ((11208, []), 0),
        ((11209, []), 1),
        ((11210, []), 1),
        ((11211, []), 2),
        ((1335, [1337, 256]), 1),
        ((1336, [1337, 256]), 1),
        ((1337, [1337, 256]), 2),
    )
    for func_args, right_answer in test_data:
        number, awesome_phrases = func_args
        answer = is_interesting(number, awesome_phrases)
        print(f"number: {number}, awesome_phrases: {awesome_phrases}, " + \
            f"right_answer: {right_answer}, answer: {answer}, " + \
            f"test: {right_answer == answer}")


if __name__ == '__main__':
    testing()
