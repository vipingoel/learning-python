import json

from json import JSONEncoder
  
class Student:
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = [roll_no]
        self.address = address

class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

class EncodeStudent(JSONEncoder):
        def default(self, o):
            return o.__dict__

address = Address("Bulandshahr", "Adarsh Nagar", "203001")
student = Student("Raju", 53, address)
std_json = json.dumps(student, cls=EncodeStudent)
print(std_json)
std = json.loads(std_json)

print(std)