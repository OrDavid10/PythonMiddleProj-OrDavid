import os
from dotenv import load_dotenv

class Car:
    load_dotenv()
    price_per_liter = int(os.getenv('PRICE_PER_LITER'))
    def __init__(self):
        """
        :writer:Or
        :Date:22/01/2023
        :description: function that build an object car with its properties
        :param:none
        :return: none
        """
        self.engine_status = bool(os.getenv('ENGINE_STATUS'))
        self.fuel_capacity = int(os.getenv('FUEL_CAPACITY'))
        self.current_fuel= int(os.getenv('CURRENT_FUEL'))
        self.fuelco= int(os.getenv('FUELCO'))
        self.money= int(os.getenv('MONEY'))
        self.gear = int(os.getenv('GEAR'))
        self.gear_speed =int(os.getenv('GEAR_SPEED'))
    def start(self):
        """
        :writer:Or
        :Date:22/01/2023
        :description: function that starts the engine of the car
        :param:none
        :return: none
        """
        self.engine_status = True
    def stop(self):
        """
        :writer:Or
        :Date:22/01/2023
        :description: function that stop the car from driving the speed and the gear will
        reduces to 0
        :param:none
        :return: none
        """
        if self.engine_status==True:
            self.gear=0
            self.gear_speed=0
        else:
            raise ValueError(os.getenv('ValueError4'))
    def turn_off(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that turn the car off
       :param:none
       :return: none
       """
        self.engine_status=False
    def drive(self , km_to_drive):
        """
        :writer:Or
        :Date:22/01/2023
        :description: function that checks if the car can handle the drive and
         starts the driving
        :param km_to_drive:km to drive
        :return: none
        """
        if self.engine_status==True:
            if km_to_drive <1:
                raise ValueError(os.getenv('ValueError5'))
            elif km_to_drive > self.get_fuelco()*self.get_fuel():
                raise OverflowError(os.getenv('overflowerror3'))
            else:
                self.gearup()
                self.set_fuel(self.get_fuel()-km_to_drive/self.get_fuelco())
                self.stop()
        else:
            raise ValueError(os.getenv('ValueError4'))
    def gearup(self):
        """
        :writer:Or
        :Date:22/01/2023
        :description: function that gears up the current gear status by 1
        :param:none
        :return: none
        """
        if self.engine_status == True:
            if self.get_gear()==6:
                raise OverflowError(os.getenv('OverflowError2'))
            else:
                self.set_gear(self.get_gear()+1)
        else:
            raise ValueError(os.getenv('ValueError4'))
    def get_engine_status(self):
        """
          :writer:Or
          :Date:22/01/2023
          :description: function that returns the engine status
          :param:none
          :return: boolean
         """
        return self.engine_status
    def get_gear_speed(self):
      """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns the current gear speed
       :param:none
       :return: int
      """
      return self.get_gear()*30
    def get_gear(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns the gear state from 0-6
       :param:none
       :return: int
       """
        return self.gear
    def set_gear(self,gear_to_set):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that sets the gear of the car
       :param: gear to set
       :return: none
       """
        if gear_to_set>6 or gear_to_set<0:
            raise ValueError(os.getenv('ValueError1'))
        else:
            self.gear=gear_to_set
            self.gear_speed=gear_to_set*30
    def get_fuel(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns the current fuel
       :param:none
       :return: int
       """
        return self.current_fuel
    def set_fuel(self,fuel):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that sets the current fuel
       :param:none
       :return: none
       """
        if fuel >self.get_fuel_capacity() or fuel<0:
            raise ValueError(os.getenv('ValueError2'))
        else:
            self.current_fuel=fuel
    def get_fuelco(self):
        """
      :writer:Or
      :Date:22/01/2023
      :description: function that returns the fuelco
      :param:none
      :return: int
      """
        return self.fuelco
    def get_money(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns the current money
       :param:none
       :return: int
       """
        return self.money
    def set_money(self,money):
        if money<0:
            raise ValueError(os.getenv('ValueError3'))
        elif str(money).isnumeric() == False:
            raise TypeError(os.getenv('TypeError1'))
        else:
            self.money=money
    def get_fuel_capacity(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns the fuel capacity
       :param:none
       :return: int
       """
        return self.fuel_capacity
    def fill_up_gas(self):
        """
         :writer:Or
        :Date:22/01/2023
        :description: function that fills up the gas and updates it , and updates the money after the filling up
        :param:none
        :return: none
        """
        fuel_to_fill=self.get_fuel_capacity()-self.get_fuel()
        amount_to_pay=fuel_to_fill*self.price_per_liter
        if self.get_money()<amount_to_pay:
            raise OverflowError(os.getenv('OverflowError1'))
        else:
            self.set_fuel(self.get_fuel_capacity())
            self.money-=amount_to_pay
    def need_to_be_filled(self):
        """
       :writer:Or
       :Date:22/01/2023
       :description: function that returns True if needed to fillup gas
       and False otherwise
       :param:none
       :return: boolean
       """
        return self.get_fuel()<=2