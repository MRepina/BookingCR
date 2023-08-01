# Meeting Scheduler App

The Meeting Scheduler App is a simple Python application that allows users to schedule and manage appointments and meetings. The app provides a user-friendly interface to view and book time slots for different dates.

## Features

- Schedule appointments for a single day or a whole week.
- View the schedule for a selected date and check for conflicting bookings.
- Book available time slots by providing your name, meeting name, start time, and end time.

## Prerequisites

- Python 3.x
- `customtkinter` library (included in the project directory)

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Run the following command to install the required dependencies:

   pip install tkcalendar

## How to Use

1. Open a terminal or command prompt in the project directory.
2. Run the `app.py` script:

   python app.py


3. The Meeting Scheduler App window will appear with three options: "Schedule for a day," "Schedule for a week," and "Booking."
4. Click on the appropriate button to perform the desired action.

### Schedule for a Day

- Choose a date from the calendar widget.
- Click on the "Show Schedule" button to view the schedule for the selected date.
- The schedule will be displayed in the scrollable frame.

### Schedule for a Week

- Choose a start date and an end date from the calendar widgets.
- Click on the "Show Schedule" button to view the schedules for all dates within the selected week.
- The schedules for each date will be displayed in the scrollable frame.

### Booking

- Choose a date from the calendar widget.
- Enter your name and the meeting name in the respective entry fields.
- Provide the start time and end time in the format "HH:MM."
- Click on the "Submit" button to book the time slot.
- If the time slot is available and there are no conflicting bookings, the booking will be created successfully.

## Notes

- The available booking time range is from 07:00 to 20:00.
- The app does not support saving data to a database. All bookings will be cleared when the app is closed.

## Contributing

Contributions to this project are welcome. If you find any bugs or want to suggest new features, please open an issue or submit a pull request.


Happy scheduling!


# BookingCR
