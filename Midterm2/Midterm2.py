# Elick Coval
# 00845725
# Elick_Coval@student.uml.edu
# 3/18/2020
# COMP 4600
# Midterm 2

# enables the dictionary with lists of dictionaries for scheduling
import collections as ct

# global lists and flags to persist through loops
doctors = []
patients = []
keepAsking = True
firstTime = True


# Setting up the data structure used for scheduling
def initializeSchedule():
    week = ct.defaultdict(list)
    clear = {'': ''}
    week['Monday'].append(clear)
    week['Tuesday'].append(clear)
    week['Wednesday'].append(clear)
    week['Thursday'].append(clear)
    week['Friday'].append(clear)
    return week


class Doctor:

    def __init__(self, name, spec):
        self.patients = initializeSchedule()  # start with an empty schedule
        self.name = name  # doctor's name
        self.specialty = spec # doctor's specialization

    # patient toString returns a string of pertinent information which is split apart and used
    def add_patient(self, patient):
        values = str(patient).split()
        if self.look_for_space(values[0]):
            self.patients[values[0]].insert(0, {values[1]: values[2]})

    def remove_patient(self, patient):
        values = str(patient).split()
        self.patients[values[0]].remove({values[1]: values[2]})

    # I couldn't figure out a way to omit the defaultdict in print statement
    def print_patients(self):
        for k, v in self.patients.items():
            print(k + ":")
            for x in v:
                print(''.join(x))

    # checks to make sure the max isn't allowed
    def look_for_space(self, chosenDay):
        if (len(self.patients[chosenDay])) <= 16:
            return True
        else:
            print("Sorry, " + self.name + " is all booked up on that day")
            return False

    def __str__(self):
        return str(self.name) + ", " + str(self.specialty)

    # to test disallowing a max of 16 patients per day
    def test(self, testDoctor):
        p1 = Patient("Friday", "Ying", "X-Ray")
        testDoctor.add_patient(p1)
        patients.append(p1)
        p2 = Patient("Friday", "Jaime", "Check-Up")
        testDoctor.add_patient(p2)
        patients.append(p2)
        p3 = Patient("Friday", "Brynn", "Coronavirus-Test")
        testDoctor.add_patient(p3)
        patients.append(p3)
        p4 = Patient("Friday", "Janiya", "Check-Up")
        testDoctor.add_patient(p4)
        patients.append(p4)
        p5 = Patient("Friday", "Krista", "Screening")
        testDoctor.add_patient(p5)
        patients.append(p5)
        p6 = Patient("Friday", "Kamora", "Coronavirus-Test")
        testDoctor.add_patient(p6)
        patients.append(p6)
        p7 = Patient("Friday", "Lainey", "Blood-Test")
        testDoctor.add_patient(p7)
        patients.append(p7)
        p8 = Patient("Friday", "Mario", "Coronavirus-Test")
        testDoctor.add_patient(p8)
        patients.append(p8)
        p9 = Patient("Friday", "Wei", "Blood-Test")
        testDoctor.add_patient(p9)
        patients.append(p9)
        p10 = Patient("Friday", "Todd", "Blood-Test")
        testDoctor.add_patient(p10)
        patients.append(p10)
        p11 = Patient("Friday", "Todd", "Check-Up")
        testDoctor.add_patient(p11)
        patients.append(p11)
        p12 = Patient("Friday", "Wang", "Broken-Leg")
        testDoctor.add_patient(p12)
        patients.append(p12)
        p13 = Patient("Friday", "Felipe", "Surgery")
        testDoctor.add_patient(p13)
        patients.append(p13)
        p14 = Patient("Friday", "Anabel", "Check-Up")
        testDoctor.add_patient(p14)
        patients.append(p14)
        p15 = Patient("Friday", "Yamilet", "Check-Up")
        testDoctor.add_patient(p15)
        patients.append(p15)
        p16 = Patient("Friday", "Milo", "Check-Up")
        testDoctor.add_patient(p16)
        patients.append(p16)


class Patient:

    def __init__(self, day, name, procedure):
        self.day = day
        self.name = name
        self.procedure = procedure

    def __str__(self):
        return str(self.day) + " " + str(self.name) + " " + str(self.procedure)


# driver code
while keepAsking:

    # for testing purposes
    if firstTime:
        d = Doctor("Bruce", "Surgeon")
        d2 = Doctor("Jian", "Cardiologist")
        doctors.append(d)
        doctors.append(d2)
        d.test(d)
        firstTime = False

    try:
        choice = int(input("\nWhat would you like to do?  \n 1. See list of available doctors \n 2. Add a doctor \n "
                            "3. Schedule a new patient \n 4. See a doctor's list of patients \n "
                            "5. Lookup a patient's procedure \n 0. Quit\n"))
        if choice == 1:
            for doctor in doctors:      # print all doctors
                print(doctor)

        if choice == 2:                 # allow any doctor name / specialty
            name = input("What is the doctor's name?\n")
            spec = input("What is the doctor's specialty?\n")
            doc = Doctor(name, spec)
            doctors.append(doc)

        if choice == 3:
            name = input("What is the first name of the patient?\n")

            while True:                 # keep asking until the user enters a day of the week
                try:
                    day = input("Which day would this be for?")
                    for doc in doctors:
                        if day in doc.patients:
                            raise Exception
                except Exception as e:
                    break

                print("Please enter a day of the week")

            proc = input("What is the reason for visit? (No Spaces)\n")

            # create patient and add to the patient list
            p = Patient(day, name, proc)
            patients.append(p)

            while True:                  # keep asking until they pick an available doctor
                try:
                    docChoice = input("Which doctor are you trying to schedule for?")
                    for doc in doctors:
                        if doc.name == docChoice:
                            doc.add_patient(p)
                            raise Exception
                except Exception as e:
                    break

                print("Sorry no doctor by that name, the available doctors are: ")
                for i in doctors:
                    print(i)

        if choice == 4:
            found = False
            docChoice = input("Which doctor's patient list are you looking for?")
            for doc in doctors:
                if doc.name == docChoice:
                    print(doc.patients)
                    doc.print_patients()
                    found = True
            if not found:
                print("Sorry that doctor was not found, the doctors are")
                for i in doctors:
                    print(i)

        if choice == 5:
            found = False
            patChoice = input("Which patient are you looking up?")
            for pat in patients:
                if pat.name == patChoice:
                    print(pat.name + " is scheduled for " + pat.procedure + " on " + pat.day)
                    found = True
            if not found:
                print("Sorry that patient was not found, please check for typos")

        if choice == 0:
            keepAsking = False

    except ValueError as e:
        print("Please enter an integer")
