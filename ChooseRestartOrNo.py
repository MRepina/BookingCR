import datetime 

# Define the days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize the conference room schedule
conference_room = {
    "Monday": {},
    "Tuesday": {},
    "Wednesday": {},
    "Thursday": {},
    "Friday": {}
}

# Define the working hours for the conference room
start_time = datetime.time(8, 0)
end_time = datetime.time(20, 0)

# Define the function to display the schedule for a given day
def display_day_schedule(day):
    print(f"Schedule for {day}:")
    if conference_room[day]:
        for time, reservation in conference_room[day].items():
            meeting_time = f"{time[0].strftime('%H:%M')} - {time[1].strftime('%H:%M')}"
            name, meeting = reservation.split("(")[0].strip().split(" - ")
            print(f"{meeting_time}: {name} - {meeting}")
    else:
        print("The room is free.")


# Define the function to display the schedule for the current week
def display_week_schedule():
    """Display the schedule for the current week."""
    for day in days_of_week:
        display_day_schedule(day)
        print()

# Define the function to book the conference room for a specific time slot
def book_time():
    while True:
        today = datetime.date.today()
        day = input("\nEnter the day you want to book (Monday-Friday): ")
        if day not in conference_room:
            print("\nInvalid day entered.")
            reset = input("\nAnother try?(y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break
        
        days_ahead = days_of_week.index(day) - today.weekday()
        if days_ahead < 0:
            print("\nYou can't book a past day.")
            reset = input("\nAnother try ? (y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break
        date = today + datetime.timedelta(days=days_ahead)

        if day == days_of_week[today.weekday()] and datetime.datetime.now().time() > datetime.time(20, 0):
            print("\nThe conference room is closed for today.")
            print("\nWorking hours 07:00 - 20:00")
            reset = input("\nReset time ?(y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break
        
        start_time_str = input("\nEnter the time you want to start (HH:MM): ")
        try:
            start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
        except ValueError:
            print("\nInvalid time entered.")
            reset = input("\nReset time ?(y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break
        
        if day == days_of_week[today.weekday()] and start_time < datetime.datetime.now().time():
            print("\nYou can't book a time earlier than the current time.")
            reset = input("\nReset booking? (y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break

        start_datetime = datetime.datetime.combine(date, start_time)
        end_time_str = input("Enter the time you want to finish (HH:MM): ")
        try:
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        except ValueError:
            print("\nInvalid time entered.")
            reset = input("\nReset time ? (y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break
        end_datetime = datetime.datetime.combine(date, end_time)

        start_time_min = datetime.time(7, 0)
        end_time_max = datetime.time(20, 0)
        if start_datetime.time() < start_time_min or end_datetime.time() > end_time_max:
            print("\nThe conference room is closed during this time.")
            print("Working hours 07:00 - 20:00")
            reset = input("\nReset time ?(y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break

        if start_time.strftime("%H:%M") in conference_room[day]:
            print("\nThat time slot is already booked.")
            reset = input("\Reset time ?(y/n): ")
            if reset.lower() == "y":
                continue
            else:
                print("\nGoing back to the beginning...")
                break

        for timeslot, booking in conference_room[day].items():
            if start_datetime < timeslot[1] and end_datetime > timeslot[0]:
                print(f"\nConflict with existing booking: {booking}")
                reset = input("\nReset time ? (y/n): ")
                if reset.lower() == "y":
                    continue
                else:
                    print("\nGoing back to the beginning...")
                    break
                return
        name = input("Enter your name: ")
        title = input("Enter the title of the meeting: ")
        conference_room[day][(start_datetime, end_datetime)] = f"{title} - {name} ({start_time_str} - {end_time_str})"
        print("Reservation successful.")
        display_day_schedule(day)
        

        # Ask user if they want to make another reservation or exit
        while True:
            choice = input("\nDo you want to make another reservation? (y/n): ")
            if choice.lower() == "y":
                book_time()
                break
            elif choice.lower() == "n":
                print("...\nExiting program.")
                return
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")
        

# Define the main function to prompt the user for their choice
def main():
    while True:		
        choice = input("\nEnter your choice:\n1 - See the schedule for the day\n2 - See the schedule for the week\n3 - Book the conference room\n4 - Exit\n")
        if choice == "1":
            day = input("\nEnter the day you want to see the schedule for (Monday-Friday): ")
            if day not in conference_room:
                print("\nInvalid day entered.")                
                continue
            display_day_schedule(day)
        elif choice == "2":
            display_week_schedule()
        elif choice == "3":
            book_time()
        elif choice == "4":
            break
        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()
