import pandas as pd
from sys import argv


class Reader:
    def __init__(self, file_path, items_to_change):
        self.file_path = file_path
        self.items_to_change = [x.split(',') for x in items_to_change]

    def file_read(self):
        file = self.file_path.split('.')[-1]
        if file == 'csv':
            return pd.read_csv(self.file_path, header=None)
        elif file == 'json':
            return pd.read_json(self.file_path)
        elif file == 'pkl':
            return pd.read_pickle(self.file_path)
        elif file == 'txt':
            return pd.read_csv(self.file_path, header=None)

    def modified(self):
        df = self.file_read()
        for y in self.items_to_change:
            df.iloc[int(y[1])][int(y[0])] = y[2]
        return df


class CsvRead(Reader):
    def modi(self, file_out):
        df = self.modified()
        df.to_csv(file_out,index=False, header=False)
class JsonRead(Reader):
    def modi(self, file_out):
        df = self.modified()
        df.to_json(file_out)

class PickleRead(Reader):
    def modi(self, file_out):
        df = self.modified()
        df.to_pickle(file_out)

class TXTRead(Reader):
    def modi(self, file_out):
        df = self.modified()
        df.to_csv(file_out, index=False, header=False)

file_in = argv[1]
file_out = argv[2]
items_to_change = argv[3:]
what_file = file_out.split(".")[-1]

try:
    if what_file == 'csv':
        a = CsvRead(file_in, items_to_change)
        a.modi(file_out)
    elif what_file == 'json':
        a = JsonRead(file_in, items_to_change)
        a.modi(file_out)

    elif what_file == 'pkl':
        a = PickleRead(file_in, items_to_change)
        a.modi(file_out)
    elif what_file == 'txt':
        a = TXTRead(file_in, items_to_change)
        a.modi(file_out)

except IndexError:
    print('Poprawna instrukcja dla programu to:')
    print('python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>')
except FileNotFoundError:
    print('Podany plik, który pragniesz zmodyfikować, nie istnieje')

print('Twój plik po zmianach:' + '\n')
print(a.modified())