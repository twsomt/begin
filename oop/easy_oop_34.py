# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True
        
    def set_data(self, data):
        self.data = data

    def lst_to_str(self):
        return " ".join(map(str, self.data))

    def check_is_show(self, *args):
        if args:
            args = "".join(args)
            
        if self.is_show:
            print(f'{args}{self.lst_to_str()}')
        else:
            print('Отображение данных закрыто')

    def show_table(self):
        self.check_is_show()

    def show_graph(self):
        self.check_is_show('Графическое отображение данных: ')

    def show_bar(self):
        self.check_is_show('Столбчатая диаграмма: ')
    
    def set_show(self, fl_show):
        self.is_show = fl_show
    
        
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, '8 11 10 -32 0 7 18'.split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False) 
gr.show_table()