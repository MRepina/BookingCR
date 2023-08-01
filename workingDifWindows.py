import customtkinter as tk
from tkcalendar import Calendar
from tkinter.constants import END
from tkinter import messagebox
from datetime import datetime, timedelta
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("900x530")

bookings = []

class Booking:
    def __init__(self, date, start_time, end_time, name, meeting_name):
        self.date = datetime.strptime(date, "%m/%d/%y")
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.name = name
        self.meeting_name = meeting_name

def get_reservations(selected_date):
    selected_date = datetime.strptime(selected_date, "%m/%d/%y").date()
    return [booking for booking in bookings if booking.date.date() == selected_date]

def login():
    # Remove the login widgets
    frame.destroy()

    # Create a new frame for the main screen
    main_frame = customtkinter.CTkScrollableFrame(master=root, width=200, height=200)
    main_frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    # Create the four buttons
    button1 = customtkinter.CTkButton(master=main_frame, text="Schedule for a day", command=show_day)
    button1.pack(pady=12, padx=10)

    button2 = customtkinter.CTkButton(master=main_frame, text="Schedule for a week", command=show_week)
    button2.pack(pady=12, padx=10)

    button3 = customtkinter.CTkButton(master=main_frame, text="Booking", command=book_time)
    button3.pack(pady=12, padx=10)

def show_schedule(book_frame, selected_date):
    reservations = get_reservations(selected_date)
    schedule_label = customtkinter.CTkLabel(master=book_frame)

    if reservations:
        schedule_text = ""
        for booking in reservations:
            schedule_text += f"\nStart Time: {booking.start_time.strftime('%H:%M')} - " \
                            f"End Time: {booking.end_time.strftime('%H:%M')} - " \
                            f"Name: {booking.name} - " \
                            f"Meeting Name: {booking.meeting_name}"
    else:
        schedule_text = "No bookings for this date."

    schedule_label.configure(text=f"Schedule for {selected_date}:\n{schedule_text}")
    schedule_label.pack(side="top", pady=10, anchor="center")

def show_day():
    book_window = tk.CTkToplevel(master=root)
    book_window.geometry("900x530")
    book_window.title("Book Time")

    book_frame = tk.CTkScrollableFrame(master=book_window, width=200, height=200)
    book_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Choose date
    date_label = tk.CTkLabel(master=book_frame, text="Choose Date:")
    date_label.pack(side="top", pady=10, anchor="center")
    date_picker = Calendar(master=book_frame, selectmode="day")
    date_picker.pack(side="top", pady=10, anchor="center")

    def show_schedule_wrapper():
        selected_date = date_picker.get_date()
        show_schedule(book_frame, selected_date)

    show_schedule_button = tk.CTkButton(master=book_frame, text="Show Schedule", command=show_schedule_wrapper)
    show_schedule_button.pack(pady=20)

    start_over_button = tk.CTkButton(master=book_frame, text="OK", command=book_window.destroy)
    start_over_button.pack(pady=20)

    book_window.mainloop()
    
def show_week():
    book_window = tk.CTkToplevel(master=root)
    book_window.geometry("900x530")
    book_window.title("Book Time")

    book_frame = tk.CTkScrollableFrame(master=book_window, width=200, height=200)
    book_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Container for start date and end date
    date_container = tk.CTkFrame(master=book_frame)
    date_container.pack(side="top", pady=10, anchor="center")

    # Choose start date
    start_date_label = tk.CTkLabel(master=date_container, text="Choose Start Date:")
    start_date_label.pack(side="left", padx=10)
    start_date_picker = Calendar(master=date_container, selectmode="day")
    start_date_picker.pack(side="left", padx=10)

    # Choose end date
    end_date_label = tk.CTkLabel(master=date_container, text="Choose End Date:")
    end_date_label.pack(side="left", padx=10)
    end_date_picker = Calendar(master=date_container, selectmode="day")
    end_date_picker.pack(side="left", padx=10)

    schedule_frame = tk.CTkFrame(master=book_frame)  # Create a new frame for displaying schedule
    schedule_frame.pack(side="top", pady=10, anchor="center")

    def show_schedule_wrapper():
        start_date = start_date_picker.get_date()
        end_date = end_date_picker.get_date()

        # Retrieve the dates for Monday to Friday within the selected week
        dates = get_weekday_dates(start_date, end_date)

        # Clear the schedule_frame before displaying the schedule
        for widget in schedule_frame.winfo_children():
            widget.destroy()

        # Display the schedule for each date
        for date in dates:
            show_schedule(schedule_frame, date)

    show_schedule_button = tk.CTkButton(master=book_frame, text="Show Schedule", command=show_schedule_wrapper)
    show_schedule_button.pack(pady=20)

    start_over_button = tk.CTkButton(master=book_frame, text="OK", command=book_window.destroy)
    start_over_button.pack(pady=20)

    book_window.mainloop()
    
def get_weekday_dates(start_date, end_date):
    # Convert start and end dates to datetime objects
    start_date_dt = datetime.strptime(start_date, "%m/%d/%y")
    end_date_dt = datetime.strptime(end_date, "%m/%d/%y")

    # Calculate the start and end dates for Monday to Friday within the selected week
    monday = start_date_dt
    # Calculate the last day (Friday) of the displayed week dynamically
    friday = start_date_dt + timedelta(days=(4 - start_date_dt.weekday()))

    # Generate the list of dates from Monday to Friday
    dates = []
    current_date = monday
    while current_date <= friday:
        dates.append(current_date.strftime("%m/%d/%y"))
        current_date += timedelta(days=1)

    return dates

def book_time():
    def book_time_wrapper():
        selected_date = date_picker.get_date()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()
        name = name_entry.get()
        meeting_name = meeting_entry.get()

        # Validate the input values
        if not (selected_date and start_time and end_time and name and meeting_name):
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        try:
            # Convert start and end time to datetime objects
            start_time_dt = datetime.strptime(start_time, "%H:%M")
            end_time_dt = datetime.strptime(end_time, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
            return

        # Set the available booking time range
        available_start_time = datetime.strptime("07:00", "%H:%M")
        available_end_time = datetime.strptime("20:00", "%H:%M")

        # Check if the selected start time and end time are within the available range
        if start_time_dt < available_start_time or end_time_dt > available_end_time:
            messagebox.showerror("Error", "Available time for booking 07:00 - 20:00")
            return

        # Check for conflicting bookings
        reservations = get_reservations(selected_date)
        for booking in reservations:
            if start_time_dt < booking.end_time and end_time_dt > booking.start_time:
                messagebox.showerror("Error", "There is a conflicting booking for the selected time.")
                return

        # Create a new booking instance
        booking = Booking(selected_date, start_time, end_time, name, meeting_name)
        bookings.append(booking)

        # Clear the entry fields
        start_time_entry.delete(0, END)
        end_time_entry.delete(0, END)
        name_entry.delete(0, END)
        meeting_entry.delete(0, END)

        messagebox.showinfo("Success", "Booking created successfully!")

    book_window = tk.CTkToplevel(master=root)
    book_window.geometry("900x530")
    book_window.title("Book Time")

    book_frame = tk.CTkScrollableFrame(master=book_window, width=200, height=200)
    book_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Choose date
    date_label = tk.CTkLabel(master=book_frame, text="Choose Date:")
    date_label.pack(side="top", pady=10, anchor="center")
    date_picker = Calendar(master=book_frame, selectmode="day")
    date_picker.pack(side="top", pady=10, anchor="center")

    # Choose time, name, and meeting name
    time_frame = tk.CTkFrame(master=book_frame)
    time_frame.pack(side="top", pady=10, fill="both", expand=True)

    time_label = tk.CTkLabel(master=time_frame, text="Choose Time:")
    time_label.pack(side="top", pady=10)

    left_frame = tk.CTkFrame(master=time_frame)
    left_frame.pack(side="left", padx=20, pady=10, fill="both", expand=True)

    start_label = tk.CTkLabel(master=left_frame, text="Start Time:")
    start_label.pack(pady=10)

    start_time_entry = tk.CTkEntry(master=left_frame, placeholder_text="HH:MM")
    start_time_entry.pack()

    end_label = tk.CTkLabel(master=left_frame, text="End Time:")
    end_label.pack(pady=10)

    end_time_entry = tk.CTkEntry(master=left_frame, placeholder_text="HH:MM")
    end_time_entry.pack()

    right_frame = tk.CTkFrame(master=time_frame)
    right_frame.pack(side="right", padx=20, pady=10, fill="both", expand=True)

    name_label = tk.CTkLabel(master=right_frame, text="Name:")
    name_label.pack(pady=10)

    name_entry = tk.CTkEntry(master=right_frame, placeholder_text="Enter your name")
    name_entry.pack()

    meeting_label = tk.CTkLabel(master=right_frame, text="Meeting Name:")
    meeting_label.pack(pady=10)

    meeting_entry = tk.CTkEntry(master=right_frame, placeholder_text="Enter meeting name")
    meeting_entry.pack()

    submit_button = tk.CTkButton(master=book_frame, text="Submit", command=book_time_wrapper)
    submit_button.pack(pady=20)

    start_over_button = tk.CTkButton(master=book_frame, text="OK", command=book_window.destroy)
    start_over_button.pack(pady=20)

    book_window.mainloop()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20)

login_button = customtkinter.CTkButton(master=frame, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()
