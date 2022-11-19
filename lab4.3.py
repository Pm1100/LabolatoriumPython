        import random

        punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
        print(punkty)
        print(f"Najwięcej zdobytych punktów: {max(punkty)}, najmniej zdobytych punktów: {min(punkty)}")
        liczba = float(input("Podaj liczbę punktów : "))
        print(punkty.index(liczba))

        if liczba in punkty:

        else:
            print("Liczba nie występuje w liście PUNKTY")
        suma = sum(punkty)
        srednia = round(suma / len(punkty),2)
        print(f"Średnia punktów: {srednia}")
lista1=[]

for p in punkty:
    if p >srednia:
            lista1.append(p)
print(lista1)
lista2 = [p for p in punkty if p < srednia]
print(lista2,len(lista2))
