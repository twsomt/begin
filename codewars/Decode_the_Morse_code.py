from preloaded import MORSE_CODE

def decode_morse(morse_code):

    morse_code = morse_code.strip().replace('   ', ' X ').split()
    
    print(morse_code)
    for i in range(len(morse_code)):
        if morse_code[i] == 'X':
            morse_code[i] = ' '
        else:
            morse_code[i] = MORSE_CODE[morse_code[i]]
        
        
    return ''.join(morse_code)