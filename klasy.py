class Student:
    
    def __init__(self, name, lname, klasa ) -> None:
        self.name = name
        self.lname = lname
        self.klasa = klasa

    def full_name(self):
        self.fullname = self.name + ' ' + self.lname

    def add_user(self):
        self.full_name()
        class_exists = False
        if len(students) == 0:
                students.append([self.klasa, [self.fullname]])
        else:
            for a, b in students:
                if self.klasa in a:
                    b.append(self.fullname)
                    class_exists = True
                    break
            if class_exists == False:
                students.append([self.klasa, [self.fullname]])

    def stud_search(self):
        self.full_name()
        for a, b in students:
            for c in b:
                if self.fullname == c:
                    klasa = a
                    print(f'Uczeń {self.fullname} uczęszcza do klasy {klasa}.')
                    print('Ma następujące przedmioty:')
                    for a, b in subjects.items():
                        for c, d in b.items():
                            if klasa in d:
                                print(f'{c} - nauczyciel: {a}')
                                break 
                

class Nauczyciel:
    def __init__(self, name, lname) -> None:
        self.name = name
        self.lname = lname
        

    def full_name(self):
        self.fullname = self.name + ' ' + self.lname

    def add_teach(self):
        self.full_name()
        while True:
            klasa = input('Podaj nauczaną klasę: ').upper()
            if not klasa:
                break
            if len(subjects) == 0:
                subjects[self.fullname] = {subject: [klasa]}
            else:
                if self.fullname in subjects:
                    if subject in subjects[self.fullname]:
                        subjects[self.fullname][subject].append(klasa)
                    else:
                        subjects[self.fullname][subject] = [klasa]
                else:
                    subjects[self.fullname] = {subject: [klasa]}
            print('Aby przestać dodawać klasy, naciśnij enter.')
        

    def add_precep(self):
        self.full_name()
        klasa = input('Podaj klasę, której jest wychowawcą: ').upper()
        if len(preceptors) == 0:
            preceptors[self.fullname] = [klasa]
        if self.fullname not in preceptors:
            preceptors[self.fullname] = [klasa]
        else:
            for a, b in preceptors.items():
                if klasa not in b:
                    preceptors[self.fullname].append(klasa)


def isis(klasa):
    for a, b in students:
        if klasa in a:
            return True
        
def class_searching(klasa):
    if len(preceptors) > 0:
        for r, e in students:
            if klasa in r:
                print(f'Klasa: {klasa}')
                for a, b in preceptors.items():
                    if klasa in b:
                        wychowawca = a
                        print(f'Wychowawca klasy: {wychowawca}')
                    else:
                        print('Nie podano wychowawcy')
                        break
                print(f'Uczniowie: ')
                for c in e:
                    print(c)
    else:
        for r, e in students:
            if klasa in r:
                print(f'Klasa: {klasa}')
                print('Nie podano wychowawcy')
                print(f'Uczniowie: ')
                for c in e:
                    print(c)

def stop():
    print('**************************************')

def isin(aa):
    for a, b in students:
        for c in b:
            if aa == c:
                return True



students = [
    # ['3C', ['KRZYSZTOF WOROCH', 'MAREK FLORCZAK', 'MARCIN BLACHNIEREK']],
    # ['2A', ['MICHAL PACZA']],
    # ['1B', ['Marek PACZA']]
    ]
subjects = {"JAN KULA": {"math": ["2A", "3C"], "physics": ["1B"]},
            "Anna Nowak": {"biology": ["2A", "11d"], "chemistry": ["2A"]}
}
preceptors = {}


uczen = Student('','','')
naucz = Nauczyciel('', '')
wych = Nauczyciel('', '')

while True:
    print('Podaj instrukcję:')
    print('[U]twórz - [Z]arządzaj - [K]oniec')
    instr = input().upper()
    if instr == 'UTWORZ' or instr == 'UTWÓRZ' or instr == 'U':
        while True:
            print('Jeśli chcesz stworzyć nowego UCZNIA - wciśnij U.')
            print('Jeśli chcesz stworzyć nowego NAUCZYCIELA - wciśnij N.')
            print('Jeśli chcesz stworzyć nowego WYCHOWAWCE - wciśnij W.')
            print('Jeśli chcesz powrócić do menu głównego - wciśnij K.')
            instr2 = input().upper()
            if instr2 == 'U':
                uczen.name = input('Podaj imię ucznia: ').upper()
                uczen.lname = input('Podaj nazwisko ucznia: ').upper()
                uczen.klasa = input('Podaj klasę ucznia: ').upper()
                uczen.add_user()
                stop()
            elif instr2 == 'N':
                naucz.name = input('Podaj imię nauczyciela: ').upper()
                naucz.lname = input('Podaj nazwisko nauczyciela: ').upper()
                subject = input('Podaj nauczany przedmiot: ').upper()
                naucz.add_teach()
                stop()
            elif instr2 == 'W':
                wych.name = input('Podaj imię wychowawcy: ').upper()
                wych.lname = input('Podaj nazwisko wychowawcy: ').upper()
                wych.add_precep()
                stop()
            elif instr2 == 'K':
                stop()
                break
            else:
                print('Błędna instrukcja.')
    elif instr == "Z" or instr == "ZARZĄDZAJ" or instr == 'ZARZADZAJ':
        while True:
            print('Jeśli chcesz wyświetlić klasę - wciśnij C.')
            print('Jeśli chcesz pobrać lekcję dla podanego ucznia - wciśnij U.')
            print('Jeśli chcesz wyświetlić klasy, które prowadzi nauczyciel - wciśnij N.')
            print('Jeśli chcesz wyświetlić klasy, które prowadzi wychowawca - wciśnij W.')
            print('Jeśli chcesz powrócić do menu głównego - wciśnij K.')
            instr2 = input().upper()
            if instr2 == 'C':
                print('Podaj klasę: ')
                klasa = input().upper()
                if isis(klasa) == True:
                    class_searching(klasa)
                    stop()
                else:
                    print('Brak podanej klasy. ')
                    stop()    
            elif instr2 == 'U':
                uczen.name = input('Podaj imię ucznia: ').upper()
                uczen.lname = input('Podaj naziwsko ucznia: ').upper()
                uczen.klasa = 0
                uczen.full_name()
                imie = uczen.fullname
                if isin(imie) == True:
                    uczen.stud_search()
                else:
                    print('Brak podanego ucznia.')
                stop()
            elif instr2 == 'N':
                naucz.name = input('Podaj imię nauczyciela: ').upper()
                naucz.lname = input('Podaj naziwsko nauczyciela: ').upper()
                naucz.full_name()
                imie = naucz.fullname
                if imie in subjects.keys():
                    for a, b in subjects[imie].items():
                        print(f'{imie} uczy {a} w klasach: {sorted(b)}')
                else:
                    print('Podany nauczyciel nie istnieje')
            elif instr2 == 'K':
                stop()
                break
    elif instr == 'KONIEC' or instr == 'K':
        break
    else:
        print('Błędna instrukcja. Spróbuj ponownie.')
    print(students)
    print(subjects)
    print(preceptors)

