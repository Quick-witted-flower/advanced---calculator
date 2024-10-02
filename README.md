# Kalkulator w Pythonie o dodatkowych rozszerzeniach

## Opis projektu

Jest to prosty kalkulator w języku Python, który pozwala użytkownikowi wykonywać podstawowe operacje matematyczne: dodawanie, odejmowanie, mnożenie oraz dzielenie. Kalkulator został rozszerzony o możliwość wprowadzania wielu argumentów dla dodawania i mnożenia oraz sprawdzanie, czy podane wartości są liczbami.

Program wykorzystuje bibliotekę `logging`, aby informować o operacjach wykonywanych przez użytkownika.

## Funkcje programu

- **Dodawanie**: Użytkownik może podać dwie lub więcej liczb do dodania.
- **Odejmowanie**: Użytkownik może podać dwie liczby, aby odjąć jedną od drugiej.
- **Mnożenie**: Użytkownik może podać dwie lub więcej liczb do pomnożenia.
- **Dzielenie**: Użytkownik podaje dwie liczby i program wykonuje dzielenie. Dzielnik nie może być równy 0 – w przeciwnym razie program informuje o błędzie.
- **Sprawdzanie poprawności danych**: Program sprawdza, czy podane dane są liczbami i ponownie prosi o poprawne wartości, jeśli użytkownik wprowadzi nieprawidłowe dane.

## Wymagania

- Python 3.x
- Biblioteka `logging` (wbudowana w Pythona, nie trzeba instalować)

## Jak uruchomić program

1. Skopiuj kod programu do pliku o nazwie `calculator2.py`.
2. Uruchom program w terminalu:
   ```bash
   python calculator.py
3.Program poprosi Cię o wybranie rodzaju operacji. Możesz wybrać spośród:

    1 - Dodawanie
    2 - Odejmowanie
    3 - Mnożenie
    4 - Dzielenie
4. Następnie wprowadź liczby, na których chcesz wykonać operację:

    Dla dodawania i mnożenia możesz podać wiele liczb oddzielonych spacjami.
    Dla odejmowania i dzielenia podaj dwie liczby.
5. Wynik działania zostanie wyświetlony na ekranie, a operacja zostanie zalogowana przez logging.