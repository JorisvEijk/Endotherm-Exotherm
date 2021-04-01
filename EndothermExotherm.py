import math
import matplotlib.pyplot as plt

a_conc = 1
b_conc = 1.5
c_conc = 0

temp = 350
specific_heat = 4180
heat = specific_heat * temp

reaction_heat = 130000

pre_exponential = 4
activation_energy = 8000
R = 8.3144621

time = 0
time_max = 20
dt = 0.02

a_set = []
b_set = []
c_set = []
temp_set = []
tempC_set = []
time_set = []

a_set.append(a_conc)
b_set.append(b_conc)
c_set.append(c_conc)
temp_set.append(temp)
tempC_set.append(temp - 273.15)
time_set.append(time)

while time <= time_max:

    d_a = 0
    d_b = 0
    d_c = 0
    d_heat = 0

    k = pre_exponential * math.exp(-activation_energy / (R * temp))
    rate = k * a_conc * b_conc

    d_a -= rate * dt
    d_b -= rate * dt
    d_c += rate * dt
    d_heat -= rate * dt * reaction_heat

    a_conc += d_a
    b_conc += d_b
    c_conc += d_c
    heat += d_heat
    time += dt

    temp = heat / specific_heat

    a_set.append(a_conc)
    b_set.append(b_conc)
    c_set.append(c_conc)
    temp_set.append(temp)
    tempC_set.append(temp - 273.15)
    time_set.append(time)

plt.plot(time_set, a_set, 'r', time_set, b_set, 'b', time_set, c_set, 'g')
plt.grid(True)
plt.xlim(0, time_max)
plt.show()

plt.plot(time_set, tempC_set)
plt.grid(True)
plt.show()
