from string import ascii_lowercase
x = {v: k for k, v in enumerate(ascii_lowercase, start=1)}
def alphabet_position(text):
    return ' '.join([str(x[i.lower()]) for i in text if i.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))  # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11