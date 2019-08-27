import car_stack as ct

soi = ct.CarStack([],4)
soi.depart(6)
for i in range(1,6):
    soi.arrive(i)

soi.printSoi()
soi.depart(7)

soi.depart(1)
soi.printSoi()
