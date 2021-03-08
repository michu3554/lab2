# Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
# a następnie odwróć całą listę. Po odwróceniu listy dodaj kilka pozycji
# (dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać
# 10 pozycji)

ulubione_filmy = ["Skazani na Shawshank" "Nietykalni" "Zielona mila" "Ojciec Chrzestny" "Forrest Gump" "Pulp fiction"]
print(ulubione_filmy)
ulubione_filmy.reverse()
print(ulubione_filmy)
ulubione_filmy.insert(5, "Joker")
ulubione_filmy.insert(6, "Pianista")
ulubione_filmy.insert(7, "Incepcja")
ulubione_filmy.insert(8, "Milczenie owiec")
print(ulubione_filmy)

# Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1. Pomyśl co może być kluczem

slownik_filmow = {'tytul': ulubione_filmy}

slownik_filmow.items()

print(slownik_filmow)
