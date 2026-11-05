# workshop_main.py

from fee_module import calculate_fee, workshops, Participant


def main():
    participants = []

    print("=" * 60)
    print("PARTICIPANT WORKSHOP FEE MANAGEMENT SYSTEM")
    print("=" * 60)

    while True:
        try:
            participant_name = input(
                "\nEnter participant name: "
            ).strip()

            if not participant_name:
                raise ValueError("Participant name cannot be empty.")

            print("\nAvailable Workshops")
            print("-" * 60)

            for choice, workshop in workshops.items():
                print(
                    f"{choice} - {workshop['workshop_name']}\n"
                    f"    {workshop['training_days']} days "
                    f"(RM {workshop['fee_per_day']:.2f} per day)"
                )

            workshop_choice = int(
                input("\nEnter workshop choice (1/2/3): ")
            )

            if workshop_choice not in workshops:
                raise ValueError(
                    "Invalid workshop choice. Please select 1, 2, or 3."
                )

            selected_workshop = workshops[workshop_choice]

            workshop_name = selected_workshop["workshop_name"]
            training_days = selected_workshop["training_days"]
            fee_per_day = selected_workshop["fee_per_day"]

            # Call the function imported from fee_module.py
            total_fee = calculate_fee(
                training_days,
                fee_per_day
            )

            # Create a Participant object
            participant = Participant(
                participant_name=participant_name,
                workshop_choice=workshop_choice,
                workshop_name=workshop_name,
                training_days=training_days,
                fee_per_day=fee_per_day,
                total_fee=total_fee
            )

            # Store the participant object in a list
            participants.append(participant)

            print("\nParticipant successfully registered!")
            participant.display_info()

        except ValueError as error:
            print(f"\nError: {error}")
            continue

        while True:
            another = input(
                "\nAdd another participant? (y/n): "
            ).strip().lower()

            if another in ("y", "n"):
                break

            print("Please enter y or n.")

        if another == "n":
            break

    print("\n" + "=" * 60)
    print("ALL PARTICIPANT RECORDS")
    print("=" * 60)

    for number, participant in enumerate(participants, start=1):
        print(f"\nRecord {number}")
        participant.display_info()

    print(f"\nTotal Participants: {len(participants)}")
    print("Thank you for using the system.")


if __name__ == "__main__":
    main()