from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person():
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status


class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)
    
    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor_name, spot):
        pass
    

    def add_parking_display_board(self, floor_name, display_board):
        pass

    
    def add_customer_info_panel(self, floor_name, info_panel):
        pass

    
    def add_entrance_panel(self, entrance_panel):
        pass
    

    def add_exit_panel(self, exit_panel):
        pass


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)
        
    def process_ticket(self, ticket_number):
        None


class ParkingSpot(object):
    def __init__(self, parking_spot_type:ParkingSpotType, number):
        self.__number = number
        self.__type = parking_spot_type
        self.__free = True
        self.__vehicle = None
    
    
    def get_type(self):
        return self.__type
    

    def get_number(self):
        return self__number
    
    
    def is_free(self):
        return self.__free
    

    def assign_vehicle(self, vehicle:VehicleType):
        self.__vehicle = vehicle
        self.__free = False
    

    def remove_vehicle(self, vehicle:VehicleType):
        self.__vehicle = None
        self.__free = True


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)



class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)



class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)



class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)



class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type:VehicleType, ticket=None):
        self.__license_number = license_number
        self.vehicle_type = vehicle_type
        self.__ticket = ticket
    
    def assign_ticket(self, ticket):
        self.__ticket = ticket
    


class ParkingFloor(object):
    def __init__(self, name:String):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__display_board = ParkingDisplayBoard()
    

    def add_parking_spot(self, spot:ParkingSpot):
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__handicapped_spots[spot.get_number()] = spot,
            ParkingSpotType.COMPACT: self.__compact_spots.put(spot.get_number(), spot),
            ParkingSpotType.LARGE: self.__large_spots.put(spot.get_number(), spot),
            ParkingSpotType.MOTORBIKE: self.__motorbike_spots.put(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC: self.__electric_spots.put(spot.get_number(), spot),
        }

        switcher.get(spot.get_type(), 'Wrong parking spot type')
    
    
    def assign_vehicle_to_spot(self, vehicle:Vehicle, spot:ParkingSpot):
        spot.assign_vehicle = vehicle
    

    def free_spot(self, spot):
        spot.remove_vehicle()
    


class ParkingLot(object):

    def __init__(self, name:String, address:Address):
        self.name = name
        self.address = address
        self.__name = name
        self.__address = address
        self.__parking_rate = ParkingRate()

        self.__compact_spot_count = 0
        self.__large_spot_count = 0
        self.__motorbike_spot_count = 0
        self.__electric_spot_count = 0
        self.__max_compact_count = 0
        self.__max_large_count = 0
        self.__max_motorbike_count = 0
        self.__max_electric_count = 0

        self.__entrance_panels = {}
        self.__exit_panels = {}
        self.__parking_floors = {}

        # all active parking tickets, identified by their ticket_number
        self.__active_tickets = {}

        self.__lock = threading.Lock()
    

    def get_new_parking_ticket(self, vehicle:Vehicle):
        if self.is_full(vehivle.get_type()):
            raise Exception('Parking full!')
        
        ticket = ParkingTicket()

        vehicle.assign_ticket(ticket)
        ticket.save_in_DB()
        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        return ticket

    
    def is_full(self, type:VehicleType):
        # trucks and vans can only be parked in LargeSpot
        if type == VehicleType.Truck or type == VehicleType.Van:
            return self.__large_spot_count >= self.__max_large_count
        
        # motorbikes can only be parked at motorbike spots
        if type == VehicleType.Motorbike:
            return self.__motorbike_spot_count >= self.__max_motorbike_count
        

        # cars can be parked at compact or large spots
        if type == VehicleType.Car:
            return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)
        

        # electric car can be parked at compact, large or electric spots
        return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (self.__max_compact_count + self.__max_large_count
                                                                                                  + self.__max_electric_count)


    def increment_spot_count(self, type):
        if type == VehicleType.Truck or type == VehicleType.Van:
            large_spot_count += 1
        elif type == VehicleType.Motorbike:
            motorbike_spot_count += 1
        elif type == VehicleType.Car:
            if self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1
        else:  # electric car
            if self.__electric_spot_count < self.__max_electric_count:
                electric_spot_count += 1
            elif self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1


    def is_full(self):
        for key in self.__parking_floors:
            if not self.__parking_floors.get(key).is_full():
                return False
            return True                                                                                                