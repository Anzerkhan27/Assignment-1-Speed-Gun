#!/usr/bin/env python3

"""
 processing a data stream and creating statistic of interest.
    TODO:
    1, Ask for reading input from the camera
    2, check fro valid inputs of data, including stopping at a que
    3, processing the input to produce statistics.

"""

__author__ = "Mohammad Anzer"
__email__ = "U1969730@unimail.hu.uk.ac"
__version__ = "2019-25-10"

heavy_goods = []
light_goods = []
private_cars = []
camera_readings = []
speed_limit = []
number_of_vehicles = []
terminate = "end"
try:
    while 1:
        readings = input("NEXT READING: ").lower().strip()
        if readings == terminate:
            break
        else:
            if len(readings) <= 3 and readings != '':
                try:
                    if readings[0] in ("h", "l", "c") and int(readings[1:]) in range(1, 100):
                        if readings[0] == "h":
                            heavy_goods.append(readings)
                        elif readings[0] == "l":
                            light_goods.append(readings)
                        else:
                            private_cars.append(readings)
                        camera_readings.append(int(readings[1:]))
                        number_of_vehicles.append(int(readings[1:]))
                    else:
                        print("invalid data")
                except:
                    print("invalid input")
            else:
                print("invalid input")
    for x in camera_readings:
        if x > 50:
            speed_limit.append(x)


    def kph(a):
        return round(a * 1.609, 2)


    def percentage(x):
        return round(x / len(camera_readings) * 100, 2)


    print("")
    print('Number of vehicles seen: {}.'.format(len(number_of_vehicles)))
    print("Number of heavy goods:   {}. ({}%)".format((len(heavy_goods)), percentage(len(heavy_goods))))
    print("Number of lighter goods: {}. ({}%)".format((len(light_goods)), percentage(len(light_goods))))
    print("Number of private cars:  {}. ({}%)H4C32".format((len(private_cars)), percentage(len(private_cars))))
    print("")
    print("Highest speed seen: {} MPH.   ({}KPH). ".format((max(camera_readings)), (kph(max(camera_readings)))))
    print("Lowest speed seen:  {} MPH.   ({}KPH). ".format((min(camera_readings)), (kph(min(camera_readings)))))
    print("Average speed:      {} MPH.   ({}KPH).  ".format(
        round(float(sum(camera_readings) / len(number_of_vehicles)), 2),
        (kph(float(sum(camera_readings) / len(number_of_vehicles))))))
    print("")
    print("speed limit violations: {} ({}%)".format(len(speed_limit), percentage(len(speed_limit))))
except:
    print("No readings today")
