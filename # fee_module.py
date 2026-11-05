# fee_module.py

# Question 1(a): Calculate the total workshop fee
def calculate_fee(training_days, fee_per_day):
    return training_days * fee_per_day


# Question 1(b): Store workshop details in a dictionary
workshops = {
    1: {
        "workshop_name": "Web Development Workshop",
        "training_days": 3,
        "fee_per_day": 120
    },
    2: {
        "workshop_name": "Mobile App Development Workshop",
        "training_days": 4,
        "fee_per_day": 150
    },
    3: {
        "workshop_name": "Data Analytics Workshop",
        "training_days": 5,
        "fee_per_day": 180
    }
}


# Question 1(c): Define the Participant class
class Participant:
    def __init__(
        self,
        participant_name,
        workshop_choice,
        workshop_name,
        training_days,
        fee_per_day,
        total_fee
    ):
        self.participant_name = participant_name
        self.workshop_choice = workshop_choice
        self.workshop_name = workshop_name
        self.training_days = training_days
        self.fee_per_day = fee_per_day
        self.total_fee = total_fee

    # Question 1(d): Display participant details and fee category
    def display_info(self):
        if self.total_fee > 600:
            category = "High Fee"
        else:
            category = "Normal Fee"

        print("-" * 55)
        print(f"Participant Name : {self.participant_name}")
        print(f"Workshop Choice  : {self.workshop_choice}")
        print(f"Workshop Name    : {self.workshop_name}")
        print(f"Training Days    : {self.training_days}")
        print(f"Fee per Day      : RM {self.fee_per_day:.2f}")
        print(f"Total Fee        : RM {self.total_fee:.2f}")
        print(f"Fee Category     : {category}")
        print("-" * 55)