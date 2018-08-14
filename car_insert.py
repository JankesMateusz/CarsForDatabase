
f = open("new_cars.txt", "r")
lines = f.readlines()
f.close()

f2 = open("data.txt", "w")
for i in lines:
    f2.write("insert into carinfo(year_of_production,brand, model) values(" + str(i).rstrip("\n") + ")\n")
f2.close()