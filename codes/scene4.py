import tkinter as tk
# Import tkinter to create the graphical user interface

from PIL import Image, ImageTk
# Import Pillow tools to load and display images


class Scene4(tk.Frame):
    # This class represents the "Calling / Waiting" screen

    def __init__(self, parent, controller=None, profile_name=None):
        # This function runs automatically when Scene4 is created

        super().__init__(parent, bg='white')
        # Initialize the frame and set the background color to white

        self.controller = controller
        # Store a reference to the main application controller

        if profile_name is None:
            profile_name = "Peter Wilson"
            # Use a default name if no profile name is provided


        # =========================
        # MAIN CONTENT AREA
        # =========================

        main_frame = tk.Frame(self, bg="white")
        # Create a main frame to hold all central content

        main_frame.pack(fill=tk.BOTH, expand=True)
        # Make the frame fill the entire screen


        # =========================
        # TITLE TEXT
        # =========================

        title = tk.Label(
            main_frame,
            text="Wachten op antwoord!",
            font=("Arial", 44, "bold"),
            fg="black",
            bg="white"
        )
        # Create the main title label

        title.pack(pady=(120, 0))
        # Position the title vertically near the center of the screen


        # =========================
        # PROFILE NAME (DYNAMIC)
        # =========================

        self.name_label = tk.Label(
            main_frame,
            text=profile_name,
            font=("Arial", 32),
            fg="black",
            bg="white"
        )
        # Create a label that shows the selected profile name

        self.name_label.pack(pady=(0, 20))
        # Add space below the name


        # =========================
        # CALL ICON
        # =========================

        try:
            # Try to load the call icon image

            call_image = Image.open("images/bel_blauw.png")
            # Open the blue phone icon

            call_image = call_image.resize((120, 120))
            # Resize the image to fit the layout

            self.call_photo = ImageTk.PhotoImage(call_image)
            # Convert the image so tkinter can display it

            call_lbl = tk.Label(main_frame, image=self.call_photo, bg="white")
            # Create a label to show the phone icon

        except Exception:
            # If the image cannot be loaded

            call_lbl = tk.Label(
                main_frame,
                text="[telefoon-icoon]",
                font=("Arial", 18),
                fg="#1E73B9",
                bg="white"
            )
            # Show a text placeholder instead of the image

        call_lbl.pack(pady=0)
        # Display the call icon or placeholder


        # =========================
        # BLUE BOTTOM BAR
        # =========================

        bottom_bar = tk.Frame(self, bg='#0082C1', height=60)
        # Create a blue bar at the bottom of the screen

        bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)
        # Position the bar at the bottom and stretch it horizontally


    def update_profile_name(self, name):
        # Update the displayed profile name dynamically
        # This is used when Scene4 already exists

        self.name_label.config(text=name)
        # Change the text of the name label
