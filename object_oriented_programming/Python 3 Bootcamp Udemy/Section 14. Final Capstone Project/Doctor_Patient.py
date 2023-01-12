'''
OOP Project to schedule dr. appointments. Program verifies if both patient and doctor are available any given date.

Variable naming:
Slot refers to Date
Entries refer to Appointments
'''

# Person class
# Shared attributes between Dr & Patient
class Person(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name + " " + self.last_name
		self.calendar = Calendar() # shared class for dr & patient

	def is_available(self, slot):
		return self.calendar.is_available(slot)

	def make_appointment(self, slot, record):
		return self.calendar.add_entry(slot, record)

	def get_public_record(self): # Linked to Dr Method
		return{
			'name': self.full_name,
			'booking_class': self.__class__.__name__
		}

# Patient and Dr
class Patient(Person):
	def __init__(self, first_name, last_name, ssn):
		super(Patient, self).__init__(first_name, last_name) # multi-class inheritance
		self.ssn = ssn
		self.patient_id = self.first_name[:1] + self.last_name + self.ssn	

class Doctor(Person):
	def __init__(self, first_name, last_name, speciality):
		super(Doctor, self).__init__(first_name, last_name) # multi-class inheritance
		self.speciality = speciality

	def get_public_record(self):
		record = super(Doctor, self).get_public_record()
		record['speciality'] = self.speciality
		return record

# Clalendar class
class Calendar(object):
	def __init__(self):
		self.entries = {}

	def is_available(self, slot):
		return slot not in self.entries

	def add_entry(self, slot, record):
		if not self.is_available(slot): # case not available date
			raise DoubleBookingException # create own exception
		self.entries[slot] = record

	def __str__(self):
		return str(self.entries)

class DoubleBookingException(Exception):
	pass

# Make appointments
def schedule(doctor, patient, slot):
    if not doctor.is_available(slot):
        print('Cannot schedule, doctor is not available:', doctor.get_public_record())
        return False
    
    if not patient.is_available(slot):
        print('Cannot schedule, patient is not available:', patient.get_public_record())
        return False

    doctor.make_appointment(slot, patient.get_public_record())
    patient.make_appointment(slot, doctor.get_public_record())
    print("Appointment Scheduled with Dr. " + doctor.full_name +  " for patient " + patient.full_name + "\n")

    return True

# Testing ...
SLOT_1 = '8:00AM'
SLOT_2 = '9:00AM'
D1 = Doctor("Natasha", "Leggero", "Dental")
D2 = Doctor("Joe", "Rogan","General")  
P1 = Patient("Wayne", "Rooney", "1234")
P2 = Patient("Sarah", "Bridge", "1214")

schedule(D1,P1,SLOT_1)
schedule(D1,P2,SLOT_2)

#P1.get_public_record()
#P2.calendar()
#D1.calendar()
#D2.calendar()