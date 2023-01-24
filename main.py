from car import Car
from infrastructure_functions import write_to_log
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    try:
        load_dotenv()
        car = Car()
        car.start()
        car.gearup()
        car.gearup()
        print("Get the car's gear status after gear up twice",car.get_gear())
        print("Get the car's speed of the gear status of 2:",car.get_gear_speed())
        car.stop()
        print("Get the car's gear status after stop:",car.get_gear())
        print("Amount of money:",car.get_money())
        print("The car fuel before the drive",car.get_fuel())
        car.drive(20)
        print("The car fuel after the drive",car.get_fuel())
        car.drive(20)


    except OverflowError as e:
        write_to_log(e)
        print(e)
    except ValueError as e:
        write_to_log(e)
        print(e)
    except TypeError as e:
        write_to_log(e)
        print(e)
    except FileNotFoundError:
        write_to_log(os.getenv('FileNotFoundError'))
        print(os.getenv('FileNotFoundError'))
    except PermissionError:
        write_to_log(os.getenv('PermissionError'))
        print(os.getenv('permissionerror'))
    except Exception as e:
        write_to_log(e)
        print(e)


