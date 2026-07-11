class car:
    num=0
    def __init__(self):
        car.num+=1
        print(f"no of instance {car.num}")

maruti=car()
bmw=car()
honda=car()