def solution(s):
    if s == '':
        return []

    else:
        x = []
        for i in range(0, len(s), 2):
            try:
                x.append(f'{s[i]}{s[i+1]}')
            except:
                x.append(f'{s[i]}_')
        return x

print(solution('asdfadsfD'))