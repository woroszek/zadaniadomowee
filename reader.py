import sys, csv

try:

    csv_items = []
    csv_in = sys.argv[1]
    csv_out = sys.argv[2]
    item_to_modi = []

    with open(csv_in) as f:
        reader = csv.reader(f)
        for line in reader:
            csv_items.append(line)

    for x in sys.argv[3:]:
        item_to_modi.append(x.split(','))

    for y in item_to_modi:
        csv_items[int(y[1])][int(y[0])] = y[2]

    with open(csv_out, 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter=',')
        for item in csv_items:
            csvwriter.writerow(item)
    print('Twój plik po zmianaych wygląda następująco:')
    print('------------------------------')
    for i in csv_items:
        print(' | '.join(str(x) for x in i))
    print('------------------------------')
except IndexError:
    print('Poprawna instrukcja dla programu to:')
    print('python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>')
except FileNotFoundError:
    print('Podany plik, który pragniesz zmodyfikować, nie istnieje')