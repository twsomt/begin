def less_60(line):
    time = line.split(', ')[1:]
    
    def time_min(item):
        item = list(map(int, item.split(':')))
        return item[0]*60 + item[1]
        
      
    return time_min(time[1]) - time_min(time[0]) >= 60



with open('logfile.txt', 'r', encoding='utf-8') as read_file, open('output.txt', 'w', encoding='utf-8') as out_file:
    lines = list(map(lambda x: x.strip(), read_file.readlines()))
    for line in lines:
        if less_60(line):
            print(line.split(', ')[0], file=out_file)


