from SimpleCV import Image,Color
car_in_lot = Image("parking-car.png")
car_not_in_lot = Image("parking-no-car.png")
car = car_in_lot.crop(470,200,200,200)
yellow_car = car.colorDistance(Color.YELLOW)

yellow_car.show()
