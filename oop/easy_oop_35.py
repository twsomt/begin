class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = len(mem_slots) if len(mem_slots) <= 4 else 4
        self.mem_slots = mem_slots

    def get_config(self):
        str_memory = ''
        for i in range(self.total_mem_slots):
            str_memory += f'{self.mem_slots[i].name} - {self.mem_slots[i].volume}; '
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {cpu.name}, {cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {str_memory.strip("; ")}' ]


cpu = CPU('имя проца', 'тактовая частота')
mem = Memory('имя оперативы1', 'размер памяти1')
mem1 = Memory('имя оперативы2', 'размер памяти2')
mb = MotherBoard('имя материнки', cpu, mem, mem1)


print(mb.get_config())


