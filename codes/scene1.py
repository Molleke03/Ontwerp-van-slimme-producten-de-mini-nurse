import tkinter as tk
# Import tkinter, which is used to create windows, frames, and text on the screen

from PIL import Image, ImageTk
# Import tools from Pillow (PIL) to load and display images in the interface


class Scene1(tk.Frame):
    # This class represents the first menu screen of the application


    def __init__(self, parent, controller):
        # This function runs automatically when Scene1 is created


        super().__init__(parent, bg='white')
        # Initialize the frame and set the background color to white

        self.controller = controller

        # This allows Scene1 to request screen changes


        # =========================
        # MAIN LAYOUT FRAME
        # =========================

        main_frame = tk.Frame(self, bg='white')
        # Create a main frame that will hold all visible content

        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=(20, 10))
        # Place the frame on the screen


        # =========================
        # HEADER
        # =========================

        header = tk.Label(
            main_frame,
            text="Menu",
            font=('Arial', 36, 'bold'),
            fg='black',
            bg='white'
        )
        # Create a large title label with the text "Menu"

        header.pack(anchor='w', pady=(0, 30))
        # Place the header at the left side ("w" means west/left)
        # Add space below the header


        # =========================
        # MENU CONTAINER
        # =========================

        menu_container = tk.Frame(main_frame, bg='white')
        # Create a frame that will contain the menu options

        menu_container.pack(anchor='w')
        # Place the menu container aligned to the left


        # =========================
        # CONTACTEN OPTION
        # =========================

        contacten_frame = tk.Frame(menu_container, bg='white')
        # Create a frame for the "Contacten" menu option

        contacten_frame.pack(anchor='w', pady=(0, 10))
        # Place it on the left with some space below

        try:
            # Try to load the image for the "Contacten" option

            heart_img = Image.open("images/hart_groen.png").resize((130, 104))
            # Open the green heart image and resize it to fit the layout

            self.heart_photo = ImageTk.PhotoImage(heart_img)
            # Convert the image so tkinter can display it

        except:
            # If the image cannot be loaded (file missing or error)

            self.heart_photo = None
            # Set the image to None so the program does not crash

        tk.Label(contacten_frame, image=self.heart_photo, bg='white').pack(
            side=tk.LEFT, padx=(0, 30)
        )
        # Display the heart image on the left side
        # Add space to the right of the image

        tk.Label(
            contacten_frame,
            text="Contacten",
            font=('Arial', 36, 'bold'),
            fg='#2E7D32',
            bg='white'
        ).pack(side=tk.LEFT)
        # Display the text "Contacten" next to the image
        # The green color indicates this option is currently active or selected


        # =========================
        # SEPARATOR LINE
        # =========================

        tk.Frame(
            menu_container,
            bg="#CCCCCC",
            height=2,
            width=600
        ).pack(pady=20, anchor='w')
        # Create a thin gray horizontal line
        # This visually separates the menu options


        # =========================
        # ONTMOETEN OPTION
        # =========================

        ontmoeten_frame = tk.Frame(menu_container, bg='white')
        # Create a frame for the "Ontmoeten" menu option

        ontmoeten_frame.pack(anchor='w')
        # Place the frame aligned to the left

        try:
            # Try to load the image for the "Ontmoeten" option

            meet_img = Image.open("images/+ grijs.png").resize((130, 104))
            # Open the gray plus image and resize it

            self.meet_photo = ImageTk.PhotoImage(meet_img)
            # Convert the image so tkinter can display it

        except:
            # If the image cannot be loaded

            self.meet_photo = None
            # Set the image to None to avoid errors

        tk.Label(ontmoeten_frame, image=self.meet_photo, bg='white').pack(
            side=tk.LEFT, padx=(0, 30)
        )
        # Display the gray plus image on the left side

        tk.Label(
            ontmoeten_frame,
            text="Ontmoeten",
            font=('Arial', 36, 'bold'),
            fg='#B4B4B4',
            bg='white'
        ).pack(side=tk.LEFT)
        # Display the text "Ontmoeten" next to the image
        # The gray color indicates this option is currently inactive
