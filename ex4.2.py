
from math import pi, cos, sin, tan
from numpy import deg2rad

Theta_deg = float(input('Insira o valor do angulo:\n'))
Theta_rad = deg2rad(Theta_deg)

print('Seno = ', sin(Theta_rad))
print('Cosseno = ', cos(Theta_rad))
print('Tangente = ', tan(Theta_rad))