class Car:

    def __init__(self):

       # self.doors = doors
        self.is_car = True

    def chek_engine_start(self):
        engine_started = False
        num = 0
        while True:
            cinput = input("Please enter value: ")
            num += 1

            if num > 5:
                print("You dont deserve a tesla!")
                break
            else:
                if cinput == "Start":
                    if engine_started == True:
                        print("Engine already started")
                    else:
                        print("Engine Started")
                        engine_started = True

                elif cinput == "Stop":
                    if engine_started == False:
                        print("Engine already Stopped!")

                    else:
                        print("Engine Stopped")
                        engine_started = False


class Tesla(Car):
    pass


class Toyota(Car):
    pass


tesla = Tesla()
tesla.chek_engine_start()

toyota = Toyota()
toyota.chek_engine_start()
