#   Oppgave 6

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2-5

x = np.linspace(-10, 10, 200)

y = f(x)

plt.plot(x, y, color="blue")
plt.title("Oppgave 6")

plt.show()