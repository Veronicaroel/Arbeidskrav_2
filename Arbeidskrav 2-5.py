import math

def beregn_figuren(a, b):
    # Areal
    radius = a / 2
    areal_halvsirkel = (math.pi * radius**2) / 2
    areal_trekant = (a * b) / 2
    areal = areal_halvsirkel + areal_trekant

    # Omkrets
    hypotenus = math.sqrt(a**2 + b**2)
    omkrets = (math.pi * radius) + b + hypotenus

    return areal, omkrets


a = float(input("Lengde a: "))
b = float(input("Lengde b: "))

areal, omkrets = beregn_figuren(a, b)

print("Arealet er: ", areal)
print("Ytre omkretsen er: ", omkrets)