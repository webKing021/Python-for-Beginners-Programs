#127. Menu driven program for participants

participants = []


def add_participant():
    name = input("Enter name: ")
    event = input("Enter event: ")
    gender = input("Enter gender (M/F): ")
    participants.append({"name": name, "event": event, "gender": gender})


def display_records():
    if not participants:
        print("No records.")
    else:
        for p in participants:
            print("Name:", p["name"], "Event:", p["event"], "Gender:", p["gender"])


def count_participants():
    print("Total participants:", len(participants))


def count_by_event():
    ev = input("Enter event name: ")
    c = 0
    for p in participants:
        if p["event"].lower() == ev.lower():
            c += 1
    print("Participants in", ev, ":", c)


def count_by_gender():
    g = input("Enter gender to count (M/F): ")
    c = 0
    for p in participants:
        if p["gender"].upper() == g.upper():
            c += 1
    print("Participants with gender", g, ":", c)


while True:
    print("\nMenu")
    print("1. Add record of participant")
    print("2. Display records")
    print("3. Count participants")
    print("4. Count participants on the basis of event")
    print("5. Count participants on the basis of gender")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_participant()
    elif choice == "2":
        display_records()
    elif choice == "3":
        count_participants()
    elif choice == "4":
        count_by_event()
    elif choice == "5":
        count_by_gender()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
