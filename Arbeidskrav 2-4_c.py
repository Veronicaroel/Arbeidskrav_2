#   Oppgave 4
#   b)

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["Londaon", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

nytt_land = input("Skriv inn et nytt land: ")
hovedstad = input("Skriv inn hovedstaden i " + nytt_land + ": ")
innbyggere = float(input("Skriv inn antall innbyggere i " + hovedstad + ": "))
data[nytt_land] = [hovedstad, innbyggere]

print("Oppdatert dictionary: ")
print(data)