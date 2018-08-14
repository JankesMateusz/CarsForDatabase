car_list = ["ACURA", "AMERICAN IRONHORSE","APRILIA", "ARCTIC CAT", "AUTOCAR LLC.", "AVANTI",
            "BENTLEY", "BIG DOG", "BLUE BIRD", "BOMBARDIER", "BUELL", "BUICK", "CANNONDALE",
            "CHEVROLET", "CHRYSLER", "COBRA", "COUNTRY COACH MOTORHOME", "DODGE", "DUCATI",
            "E-TON", "EL DORADO", "FERRARI", "FREIGHTLINER", "GILLIG", "GMC", "HARLEY DAVIDSON",
            "HINO", "HM", "HUMMER", "HUSABERG", "HUSQVARNA", "HYOSUNG", "INTERNATIONAL",
            "ISUZU", "JOHN DEERE", "KASEA", "KAWASAKI", "KENWORTH", "KTM", "KUBOTA",
            "KYMCO", "LAMBORGHINI", "LINCOLN", "MACK", "MASERATI", "MAYBACH", "MERCURY",
            "MORGAN", "MOTO GUZZI", "MOTOR COACH INDUSTRIES", "MV AGUSTA", "NEW FLYER",
            "ORION BUS", "OSHKOSH MOTOR TRUCK CO.", "PANOZ", "PETERBILT", "POLARIS", "PONTIAC",
            "PORSCHE", "ROLLS ROYCE", "SALEEN", "SATURN", "SCION", "SEA-DOO", "SKI-DOO",
            "STERLING", "STERLING TRUCK", "SUZUKI", "TM", "TRIUMPH", "UD", "VENTO", "VESPA",
            "VICTORY", "WESTERN RV", "WORKHORSE", "YAMAHA"]

with open("cars.txt", "r") as oldfile, open("new_cars.txt", "w") as newfile:
    for line in oldfile:
        if not any(car in line for car in car_list):
            newfile.write(line)

