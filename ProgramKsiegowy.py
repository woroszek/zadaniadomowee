balance = 0
history = []
warehouse = []

def is_or_not(item):
    if len(warehouse) > 0:
        for i in warehouse:
            if i[0] == item:
                return True
            
        return False
    else:
        return False    
    
def all_items():
    for i in warehouse:
        ilosc = i[1]['ilosc']
        koszt = i[1]['koszt']
        print(f'{i[0]}({ilosc}x) w cenie {koszt} za sztukę. Łącznie: {ilosc*koszt}')    

def item_in(item):
    for i in warehouse:
        if i[0] == item:
            ilosc = i[1]['ilosc']
            return ilosc
        
def item_cost(item):
    for i in warehouse:
        if i[0] == item:
            koszt = i[1]['koszt']
            return koszt

def item_in_cost(item):
    for i in warehouse:
        if i[0] == item:
            cena = i[1]['koszt']
            return cena

def history_number(od, do):
    od = int(od)
    do = int(do)
    if od > 0:
        for i in history:
            a = history.index(i) + 1
            if a >= od and a <= do:
                print(f'Opercja numer: {history.index(i)+1} to  {i}')
                print('***************************************************')
            else:
                continue

while True:
    print('Podaj komendę. Wpisz pomoc, jeśli chcesz zobaczyć dostępne komendy')
    command = input().lower()
    if command == 'pomoc':
        print('s - dodanie lub odjecie kwoty z konta')
        print('z - zakup')
        print('sp - sprzedaż')
        print('sk - stan konta')
        print('st - stan magaznu')
        print('m - stan magazynu dla konkretnego produktu')
        print('h - historia działań aplikacji')
        print('k - zamknięcie programu')

    if command == 's':
        print('Wpisz: D, jeśli chcesz dodać lub O, jeśli odjać: ')
        command_s = input().lower()
        if command_s == 'd':
            add = input('Podaj kwotę do dodania: ')
            if add.isnumeric() == True:
                add = float(add)
                balance += add
                history.append((f'Dodano {add}'))
            else:
                print('Podano nieprawidłowe dane. Podaj liczbę.')
        elif command_s == 'o':
            sub = input('Podaj kwotę do odjęcia: ')
            if sub.isnumeric() == True:
                sub = float(sub)
                if balance - sub < 0:
                    print('Nieprawidlowe dane. Saldo Twojego konta nie może być ujemne.')
                else:
                    balance -= sub
                    history.append(f'Odjęto {sub}')
            else:
                print('Podano nieprawidłowe dane. Podaj liczbę.')
        else:
            print('Nieprawidłowa komenda.')
                
    if command == 'z':
        item = input('Podaj nazwę produktu: ').upper()
        quantity = int(input('Podaj ilość zakupionego produktu: '))
        cost = float(input('Podaj cenę produktu: '))
        if is_or_not(item) == True:
            for i in warehouse:
                if balance - quantity * cost < 0:
                        print('Zakup nie jest możliwy. Brak środków.') 
                        break 
                if i[0] == item and balance - quantity * cost >= 0:
                    if i[1]['koszt'] != cost:
                        print('Niestety. Podaleś różne ceny dla tego samego produktu.')
                        break
                        
                    print('Produkt już znajduje się w magazynie. Ilość poprawnie zmieniona.')
                    i[1]['ilosc'] += quantity
                    history.append(f'Zaaktualizowano ilość produktu {item} o {quantity}')
                    balance = balance - quantity * cost
                    break

        if is_or_not(item) == False:
            if balance - quantity * cost >= 0:
                warehouse.append([item,{'ilosc': quantity,'koszt': cost}])
                history.append(f'Dodano produkt {item} w cenie {cost} w ilości {quantity}')
                balance = balance - quantity * cost
            else:
                print('Brak środków na pokrycie zakupu.')

    if command == 'sp':
        item = input('Podaj nazwę produktu: ').upper()
        if is_or_not(item) == True:
            print('Produkt znajduje się w magazynie.')
            print(f'Mamy {item_in(item)} sztuk. Ile pragniesz sprzedać?')
            quantity = int(input())
            if quantity > item_in(item):
                print(f'Podano liczbę większą niz stan magazynu. Nie możesz sprzedać więcej niż {item_in(item)}')
            else:   
                balance = balance + item_cost(item) * quantity
                for a in warehouse:
                    a[1]['ilosc'] -= quantity
                    if item == a[0]:
                        if a[1]['ilosc'] <= 0:
                            history.append(f'Sprzedano {quantity} sztuk przedmiotu {item}')
                            warehouse.remove(a)
                            break

                        else:
                            history.append(f'Sprzedano {quantity} sztuk przedmiotu {item}')
                            break    
        else:
            print(f'Brak produktu {item} na stanie magazynu.')                

    if command == 'sk':
        print(f'Stan Twojego konta to: {balance}')

    if command == 'st':
        if len(warehouse) < 1:
            print('Magazyn jest pusty.')
        else:
            print('Stan magazynu:')
            for i in warehouse:
                ilosc = i[1]['ilosc']
                koszt = i[1]['koszt']
                print(f'{i[0]}({ilosc}x) w cenie {koszt} za sztukę. Wartość łącznie: {ilosc*koszt}')

    if command == 'm':
        item = input('Podaj nazwę produktu: ').upper()
        if is_or_not(item) == True:
            for i in warehouse:
                if i[0] == item:
                    ilosc = i[1]['ilosc']
                    cena = i[1]['koszt']
                    print('Stan magazynu:')
                    print(f'Dla produktu {item}, to {ilosc}. Cena jednej sztuki: {cena}.')

    if command == 'h':
        if len(history) > 0:
            print(f'Wykonano łącznie {len(history)} operacji.')
            print('Możesz wybrać zakres operacji. ')
            print(f'Możliwy przedział to: 1 do {len(history)}')
            od = input("Wprowadź numer operacji od której pragniesz zaczać.")
            if od.isnumeric() == False or int(od) < 1 or int(od) > len(history):
                print(f'Błędna wartość. Możliwy przedział to: 1 do {len(history)}')
                print('Wyświetlam wyniki od operacji pierwszej.')
                od = 1
            do = input("Wprowadź numer operacji na której pragniesz zakończyć.")
            if do.isnumeric() == False or int(do) > len(history) or int(od) > int(do):
                print(f'Błędna wartość. Możliwy przedział to: 1 do {len(history)}')
                print('Wyświetlam wyniki do samego końca.')
                do = int(len(history))
            history_number(od, do)
        else:
            print("Historia wykonanych operacji jest pusta.")


    if command == 'k':
        break
