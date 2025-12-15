from math import pi, cos, sin, tan

Theta_deg = float(input('Insira o valor do angulo:\n'))
Theta_rad = Theta_deg * pi / 180

print('Seno = ', sin(Theta_rad))
print('Cosseno = ', cos(Theta_rad))
print('Tangente = ', tan(Theta_rad))