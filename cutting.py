from SimpleCV import Image
car_in_lot = Image("parking-car.png")

car = car_in_lot.crop(470,200,200,200)

car.show()
