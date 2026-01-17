import tkinter as tk
# Import tkinter, which is used to create windows, text, and layouts on the screen

from datetime import datetime
# Import datetime so we can get the current date and time


class Scene0(tk.Frame):
    # This class represents one screen in the application

    def __init__(self, parent, controller):
        # This function runs automatically when Scene0 is created

        super().__init__(parent, bg='white')
        # Initialize the Frame and set the background color to white

        self.controller = controller
        # This allows Scene0 to ask the app to change screens if needed

        # =========================
        # CENTER CONTENT
        # =========================
        # Everything on this screen will be placed in the center

        center_frame = tk.Frame(self, bg='white')
        # Create a smaller frame inside Scene0
        # This frame will hold the clock and status text

        center_frame.place(relx=0.5, rely=0.5, anchor='center')
        # Place the frame exactly in the center of the screen
        # anchor='center' means the frame is centered on that point


        # =========================
        # TIME DISPLAY
        # =========================

        self.time_label = tk.Label(
            center_frame,
            text="",
            font=('Arial', 160, 'bold'),
            fg='black',
            bg='white'
        )
        # Create a large text label to show the current time
        # The text is empty for now and will be filled later

        self.time_label.pack()
        # Add the time label to the center frame


        # =========================
        # STATUS MESSAGE
        # =========================

        status_label = tk.Label(
            center_frame,
            text="Geen belverzoek ontvangen",
            font=('Arial', 24, 'bold'),
            fg='black',
            bg='white'
        )
        # Create a smaller text label
        # This text tells the user that no call request has been received

        status_label.pack()
        # Add the status label below the time label


        # =========================
        # START CLOCK UPDATES
        # =========================

        self.update_time()
        # Call the function that updates the clock every second


    def update_time(self):
        # This function updates the time shown on the screen

        self.time_label.config(
            text=datetime.now().strftime("%H:%M")
        )
        # Get the current time and format it as hours and minutes (HH:MM)
        # Update the time label with this new value

        self.after(1000, self.update_time)
        # Wait 1000 milliseconds (1 second)
        # Then call this function again to update the time
