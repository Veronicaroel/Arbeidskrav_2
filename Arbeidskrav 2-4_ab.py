#   Oppgave 4
#   a)

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["Londaon", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

#   b)

land = input("Skriv inn et land: ")

info = data[land]
print(info[0], "er hovedstaden i", land, "og det er", info[1], "mill. innbyggere i", info[0])