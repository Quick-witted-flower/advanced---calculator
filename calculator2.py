import logging

logging.basicConfig(level=logging.INFO)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def get_numbers(multiple=False):
    if multiple:
        numbers_input = input("Podaj kilka liczb oddzielonych spacją:")
        numbers = numbers_input.split()

        if all(is_float(num)for num in numbers):
            return[float(num) for num in numbers]
        else:
            print("Niepoprawna wartość. Spróbuj ponownie.")
            return get_numbers(multiple=True)
    else:
        liczba1 = input("Podaj pierwszą liczbę:")
        liczba2 = input("Podaj drugą liczbę: ")
        if is_float(liczba1) and is_float(liczba2):
            return float(liczba1), float(liczba2)
        else:
            print("Niepoprawna wartość.Spróbuj ponownie.")
            return get_numbers(multiple=False)


operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie : ")

if operation == '1':
    liczby = get_numbers(multiple=True)
    wynik = sum(liczby)
    logging.info(f"Dodaję {','.join(map(str, liczby))}")
elif operation == '2':
    liczba1, liczba2 = get_numbers(multiple=False)
    wynik = liczba1 - liczba2
    logging.info(f"Odejmuję {liczba1} i {liczba2}")
elif operation == '3':
    liczby = get_numbers(multiple=True)
    wynik = 1
    for liczba in liczby:
        wynik *= liczba
        logging.info(f"Mnożę {','.join(map(str, liczby))}")
elif operation =='4':
    liczba1, liczba2 =get_numbers(multiple=False)
    if liczba2 !=0:
        wynik= liczba1 / liczba2
        logging.info(f"Dzielę {liczba1} przez {liczba2}")
    else:
        wynik = "Błąd: nie można dzielić przez 0!"
        logging.error("Próba dzielenia przez 0")
else:
    wynik = "Błędny wybór operacji!"
    logging.warning("Niepoprawna operacja została wybrana" )

print(f"Wynik to:  {wynik}")









