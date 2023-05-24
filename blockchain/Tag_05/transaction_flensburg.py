# Füherschein-ID, Verstoß, Datum

# driving_license_id, violation_type, violation_date
# zusätzlich: Anzahl der bisherigen Verstöße, Führerschein entzogen?
# number_of_violations, is_driver_license_suspended (Aufgabe vom Smart Contract diese Daten anzupassen)

class Transaction:

    def __init__(self, driving_license_id, violation_type, violation_date):

        self.driving_license_id = driving_license_id
        self.violation_type = violation_type
        self.violation_date = violation_date

        # zusätzlich:
        self.number_of_violations = 1 # Default
        self.is_driver_license_suspended = False
