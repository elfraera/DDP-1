name = input("Nama Tactical Doll : ")
firepower = input("Firepower : ")
firepower_int = int(firepower)
rateoffire = input("Rate of Fire : ")
rateoffire_int = int(rateoffire)
accuracy = input("Accuracy : ")
accuracy_int = int(accuracy)
evasion = input("Evasion : ")
evasion_int = int(evasion)
damagepersecond = ((firepower_int * rateoffire_int)/60)
combateffectiveness = (30 * firepower_int) + (40 * ((rateoffire_int**2)/120)) + (15*(accuracy_int + evasion_int))
print("Damage per Second : ", str(round(damagepersecond,2)))
print("Combat Effectiveness : ", str(round(combateffectiveness)))

