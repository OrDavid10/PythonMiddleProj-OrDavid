import pytest
from Car.car import Car
from Car.infrastructure_functions import write_to_log

@pytest.fixture()
def car():
    car = Car()
    return car
@pytest.mark.engine_start
def test_engine_start(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks a car's engine starter
   :return: pass/failed
   """
    car.start()
    try:
        assert car.get_engine_status() == True
        write_to_log(f'Passed (test_engine_start): with Parameters : Expected: {car.get_engine_status()} , Actual: {True}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_engine_start): Expected: {car.get_engine_status()}, Actual:  {assErr}')
def test_set_fuel(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks a setting of the car's fuel
   :return: pass/failed
   """
    try:
        car.set_fuel(40)
        assert car.get_fuel() == 40
        write_to_log(f'Passed (test_set_fuel): with Parameters : Expected: {car.get_fuel()} , Actual: {40}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_set_fuel): Expected: {car.get_fuel()}, Actual:  {assErr}')
def test_turn_off(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks the car turning off
   :return: pass/failed
   """
    try:
        car.start()
        car.turn_off()
        assert car.get_engine_status()== False
        write_to_log(f'Passed (test_turn_off): with Parameters : Expected: {car.get_engine_status()}, Actual: {False}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_turn_off): Expected: {car.get_engine_status()}, Actual:  {assErr}')
def test_fuel(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks a car's fuel
   :return: pass/failed
   """
    try:
        assert car.get_fuel()== 50
        write_to_log(f'Passed (test_fuel): with Parameters : Expected: {car.get_fuel()}, Actual: {50}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_fuel): Expected: {car.get_fuel()}, Actual:  {assErr}')
def test_gear_up(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks the car's gear up
   :return: pass/failed
   """
    try:
        car.start()
        car.gearup()
        car.gearup()
        assert car.get_gear()== 2
        write_to_log(f'Passed (test_gear_up): with Parameters : Expected: {car.get_gear()}, Actual: {2}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_gear_up): Expected: {car.get_gear()}, Actual:  {assErr}')
def test_gear_up_exception_throw(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks the car's gear up exception throwing
   :return: pass/failed
   """
    try:
        car.turn_off()
        with pytest.raises(ValueError):
            car.gearup()
        write_to_log(f'Passed (test_gear_up_exception_throw): with Error Raised : Expected: ValueError, Actual: ValueError')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_gear_up_exception_throw):  Expected: ValueError , Actual:  {assErr}')
def test_get_gear_speed(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks the car's speed
   :return: pass/failed
   """
    try:
        car.set_gear(3)
        assert car.get_gear_speed() == 90
        write_to_log(f'Passed (test_get_gear_speed): with Parameters : Expected: {car.get_gear_speed()}, Actual: {90}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_get_gear_speed):  Expected: {car.get_gear_speed()}, Actual:  {assErr}')
def test_drive_exception_OverflowError(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the drive function throwing an OverflowError
   :return: pass/failed
   """
    try:
        car.start()
        with pytest.raises(OverflowError):
            car.drive(2000000000)
        write_to_log(f'Passed (test_drive_exception_OverflowError): with Error Raised : Expected: OverflowError, Actual: OverflowError')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_drive_exception_OverflowError): Expected: OverflowError , Actual: {assErr}')
@pytest.mark.parametrize("km",[20])
def test_drive_by_fuel(car,km):
    """
   :name:Or
   :date: 22/01/2023
   :param km:kilometer for the drive
   function that checks the drive function by its fuel after execution
   :return: pass/failed
   """
    try:
        car.start()
        car.drive(km)
        assert car.get_fuel()== 49
        write_to_log(f'Passed (test_drive_by_fuel): with Parameters : Expected: {car.get_fuel()}, Actual: {49}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_drive_by_fuel):  Expected: {car.get_fuel()}, Actual:  {assErr}')
def test_drive_by_gear(car):
    """
   :name:Or
   :date: 22/01/2023
   :param:none
   function that checks the drive function by its gear after execution
   :return: pass/failed
   """
    try:
        car.start()
        car.drive(20)
        assert car.get_gear()== 0
        write_to_log(f'Passed (test_drive_by_gear): with Parameters : Expected: {car.get_gear()}, Actual: {0}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_drive_by_gear):  Expected: {car.get_gear()}, Actual:  {assErr}')
def test_drive_exception_ValueError(car):
        """
       :name:Or
       :date:22/01/2023
       :param:none
       function that checks that the drive function throwing a ValueError
       :return: pass/failed
       """
        try:
            car.turn_off()
            with pytest.raises(ValueError):
                car.drive(20)
            write_to_log(
                f'Passed (test_drive_exception_ValueError): with Error Raised : Expected: ValueError, Actual: ValueError')
        except AssertionError as assErr:
            write_to_log(f'Failed (test_drive_exception_ValueError): Expected: ValueError , Actual: {assErr}')
def test_set_money(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the money sets properly
   :return: pass/failed
   """
    try:
        car.set_money(1000)
        assert car.get_money()==1000
        write_to_log(
            f'Passed (test_set_money): with Parameters : Expected: {car.get_money()}, Actual: {1000}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_set_money): Expected: {car.get_money()}, Actual:  {assErr}')
def test_set_money_exception_ValueError(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the sets money throwing value error
   :return: pass/failed
   """
    try:
        with pytest.raises(ValueError):
            car.set_money(-1)
        write_to_log(
            f'Passed (test_set_money_exception_ValueError): with Error Raised : Expected: ValueError, Actual: ValueError')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_set_money_exception_ValueError): Expected: ValueError, Actual:  {assErr}')
def test_set_money_exception_TypeError(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the sets money throwing type error
   :return: pass/failed
   """
    try:
        with pytest.raises(TypeError):
            car.set_money('fw4r3')
        write_to_log(
            f'Passed (test_set_money_exception_TypeError): with Error Raised : Expected: TypeError, Actual: TypeError')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_set_money_exception_TypeError): Expected: TypeError, Actual:  {assErr}')
def test_fill_up_gas_by_fuel(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the fill up gas function fill the fuel capacity properly
   :return: pass/failed
   """
    try:
        car.start()
        car.drive(200)
        car.fill_up_gas()
        assert car.get_fuel()==50
        write_to_log(
            f'Passed (test_fill_up_gas_by_fuel): with Parameters : Expected: {car.get_fuel()}, Actual: {50}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_fill_up_gas_by_fuel): Expected: {car.get_fuel()}, Actual:  {assErr}')
def test_fill_up_gas_by_money(car):
    """
   :name:Or
   :date:22/01/2023
   :param:none
   function that checks that the fill up gas function reduces the money properly
   :return: pass/failed
   """
    try:
        car.start()
        car.drive(200)
        car.fill_up_gas()
        assert car.get_money()==400
        write_to_log(
            f'Passed (test_fill_up_gas_by_money): with Parameters : Expected: {car.get_money()}, Actual: {400}')
    except AssertionError as assErr:
        write_to_log(f'Failed (test_fill_up_gas_by_money): Expected: {car.get_money()}, Actual:  {assErr}')

















