#   Oppgave 2

import numpy as np

antall_elever = int(input("Skriv inn antall elever: "))

antall_pizza = int(np.ceil(antall_elever / 4))

print("Det må handles inn", antall_pizza, "pizza")