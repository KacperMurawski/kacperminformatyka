liczba1 = 0
liczba2 = 0
liczbar1 = input("podaj pierwsza liczbe rzymska:")
liczbar2 = input("podaj druga liczbe rzymska:")

if (liczbar1 == "M"):
    liczba1 = 1000
elif (liczbar1 == "D"):
    liczba1 = 500
elif (liczbar1 == "C"):
    liczba1 = 100
elif (liczbar1 == "L"):
    liczba1 = 50
elif (liczbar1 == "X"):
    liczba1 = 10
elif (liczbar1 == "V"):
    liczba1 = 5
elif (liczbar1 == "I"):
    liczba1 = 1

if (liczbar2 == "M"):
    liczba2= 1000
elif (liczbar2 == "D"):
    liczba2 = 500
elif (liczbar2 == "C"):
    liczba2 = 100
elif (liczbar2 == "L"):
    liczba2 = 50
elif (liczbar2 == "X"):
    liczba2 = 10
elif (liczbar2 == "V"):
    liczba2 = 5
elif (liczbar2 == "I"):
    liczba2 = 1

print(liczbar1 + liczbar2)
