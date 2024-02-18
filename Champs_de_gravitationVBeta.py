from math import * 
G= 6.67e(-11)
Ma= float(input("Ma = "))
Ra= float(input("Ra= "))
Vlib= sqrt((2*G*Ma)/(Ra))

h= float(input("h= "))
Vr = -((G*M)/r)


Ms = float(input("Masse du satellite : "))
Epg = -((G * Ma * Ms) / (Ra + h))



Eméca_non_divisée = (G*Ma*Ms) / (r)
Eméca_finale = (Eméca_non_divisée)/(-2)


print("Vlib = "+ str(Vlib))
print("Vr = "+ str(Vr))
print("Epg = "+ str(Epg))
print("Eméca_finale = "+ str(Eméca_finale))