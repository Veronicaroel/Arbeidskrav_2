#   Oppgave 3

import numpy as np

def grad_til_rad(v_grad):
    v_rad = v_grad*np.pi/180
    return v_rad

v_grad = float(input('Skriv inn gradtallet:' ))

v_rad = grad_til_rad(v_grad)


print(v_grad, "grader er lik", v_rad, "radianer")