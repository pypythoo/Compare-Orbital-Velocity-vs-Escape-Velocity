#Compare Orbital Velocity vs Escape Velocity
import math
G= 6.67430e-11


#earth values
m_earth = 5.972e24
r_earth = 6.371e6

#defining function (reusabale)
def orbital_velocity(m, r):  
    return math.sqrt(m*G/r)
def escape_velocity(m ,r):
    return math.sqrt(2*m*G/r)

#function call
v_orbit= orbital_velocity(m_earth, r_earth)
e_orbit= escape_velocity(m_earth, r_earth)

#outputs
print("the orbital velocity is:", v_orbit, "m/s")
print("the escape velocity is:", e_orbit, "km/s")
print("escape velocity is",e_orbit/v_orbit,"times the velocity")
