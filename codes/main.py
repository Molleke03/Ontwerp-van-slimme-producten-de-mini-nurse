# ============================================================
# MAIN APPLICATION
# ============================================================
# This program is a button-controlled graphical application
# designed to run on a Raspberry Pi.
#
# It shows different screens (called "scenes") on a display
# and allows the user to navigate between them using
# physical buttons connected to GPIO pins.
# ============================================================


# ================================
# IMPORTS
# ================================

import tkinter as tk
# tkinter is used to create the graphical user interface (GUI)

import queue
# queue is used to safely store button press events

import time
# time is used to track inactivity and button press timing

from gpiozero import Button
# gpiozero allows interaction with physical GPIO buttons


# ================================
# IMPORT SCENES
# ================================
# Each Scene represents a different screen in the application

from scene0 import Scene0  # Idle / start screen
from scene1 import Scene1  # Menu: Contacten active
from scene2 import Scene2  # Menu: Ontmoeten active
from scene3 import Scene3  # Profile selection
from scene4 import Scene4  # Waiting screen
from scene5 import Scene5  # Final / confirmation screen


# ================================
# GPIO PIN NUMBERS
# ================================
# These values correspond to physical GPIO pins on the Raspberry Pi

BUTTON1_PIN = 17        # Navigation button (down / next)
BUTTON2_PIN = 27        # Navigation button (up / previous)
BUTTON_CONFIRM = 22    # Confirm selection
BUTTON_BACK = 23       # Go back


# ================================
# EVENT QUEUE
# ================================
# This queue stores button press events as (pin, timestamp)
# Events are processed one by one in the main loop

event_queue = queue.Queue()


# ================================
# BUTTON SETUP
# ================================
# This function creates a GPIO button and connects it
# to the event queue when pressed

def setup_button(pin):
    button = Button(
        pin,
        pull_up=True,
        bounce_time=0.2
    )
    # pull_up=True ensures stable electrical behavior
    # bounce_time prevents multiple false triggers

    button.when_pressed = lambda: event_queue.put((pin, time.time()))
    # When pressed, store the pin number and press time in the queue

    return button


# Create button objects
button1 = setup_button(BUTTON1_PIN)
button2 = setup_button(BUTTON2_PIN)
button_confirm = setup_button(BUTTON_CONFIRM)
button_back = setup_button(BUTTON_BACK)


# ================================
# MAIN APPLICATION CLASS
# ================================
# This class represents the entire application window

class App(tk.Tk):

    # Time in seconds before returning to the start screen
    TIMEOUT_SECONDS = 60

    def __init__(self):
        super().__init__()

        # ----------------
        # WINDOW SETTINGS
        # ----------------

        self.title("Gecombineerde Scenes")
        # Set the window title

        self.configure(bg="white")
        # Set background color

        # Enable fullscreen mode
        self.fullscreen = True
        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)

        # Hide mouse cursor (touch / button only interface)
        self.config(cursor="none")

        # Keyboard shortcuts (for development/testing)
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.exit_fullscreen)

        # Configure root grid so content resizes correctly
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # ----------------
        # SCENE CONTAINER
        # ----------------
        # This frame holds all scenes
        # Only one scene is visible at a time

        self.container = tk.Frame(self, bg="white")
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


        # ----------------
        # STATIC SCENES
        # ----------------
        # These scenes are created once and reused

        self.frames = {}
        for Scene in (Scene0, Scene1, Scene2):
            frame = Scene(self.container, self)
            self.frames[Scene] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        # ----------------
        # DYNAMIC SCENES
        # ----------------
        # These scenes are created only when needed

        self.scene3 = None
        self.scene4 = None
        self.scene5 = None

        self.current_scene = None

        # Start application on Scene0
        self.show_frame(Scene0)

        # Track last user interaction
        self.last_activity_time = time.time()

        # Start polling the event queue
        self.poll_queue()


    # ================================
    # FULLSCREEN HANDLERS
    # ================================

    def toggle_fullscreen(self, event=None):
        # Toggle fullscreen mode on or off
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)

    def exit_fullscreen(self, event=None):
        # Exit fullscreen mode
        self.fullscreen = False
        self.attributes("-fullscreen", False)


    # ================================
    # SCENE SWITCHING
    # ================================

    def show_frame(self, scene):
        # Bring a scene to the front

        frame = scene if isinstance(scene, tk.Frame) else self.frames[scene]
        frame.tkraise()

        self.current_scene = frame
        self.last_activity_time = time.time()


    # ================================
    # EVENT QUEUE POLLING
    # ================================
    # This function runs repeatedly and handles button presses

    def poll_queue(self):
        try:
            while True:
                button, timestamp = event_queue.get_nowait()
                self.last_activity_time = timestamp

                # From start screen, any button opens the menu
                if isinstance(self.current_scene, Scene0):
                    self.show_frame(Scene1)
                    continue

                # Handle button based on GPIO pin
                if button == BUTTON1_PIN:
                    self.handle_button1()
                elif button == BUTTON2_PIN:
                    self.handle_button2()
                elif button == BUTTON_CONFIRM:
                    self.handle_confirm()
                elif button == BUTTON_BACK:
                    self.handle_back()

        except queue.Empty:
            # No events waiting
            pass


        # ----------------
        # INACTIVITY TIMEOUT
        # ----------------
        # Return to Scene0 after inactivity
        # except when Scene5 is active

        if (
            time.time() - self.last_activity_time > self.TIMEOUT_SECONDS
            and not isinstance(self.current_scene, (Scene0, Scene5))
        ):
            self.show_frame(Scene0)

        # Repeat polling every 50 milliseconds
        self.after(50, self.poll_queue)


    # ================================
    # BUTTON HANDLERS
    # ================================

    def handle_button1(self):
        # Navigate forward

        if isinstance(self.current_scene, Scene3):
            self.scene3.next_profile()
            # Move to next profile

        elif isinstance(self.current_scene, Scene1):
            self.show_frame(Scene2)
            # Switch menu selection


    def handle_button2(self):
        # Navigate backward

        if isinstance(self.current_scene, Scene3):
            self.scene3.prev_profile()
            # Move to previous profile

        elif isinstance(self.current_scene, Scene2):
            self.show_frame(Scene1)
            # Switch menu selection back


    def handle_confirm(self):
        # Confirm current selection

        if isinstance(self.current_scene, Scene1):
            self.show_scene3("contacten")

        elif isinstance(self.current_scene, Scene2):
            self.show_scene3("ontmoeten")

        elif isinstance(self.current_scene, Scene3):
            self.show_scene4(self.scene3.get_current_profile_name())


    def handle_back(self):
        # Go back to previous menu

        if isinstance(self.current_scene, Scene5):
            self.scene5.stop_audio()
            self.show_frame(Scene1)

        elif isinstance(self.current_scene, Scene3):
            self.show_frame(Scene1)


    # ================================
    # DYNAMIC SCENE CREATION
    # ================================

    def show_scene3(self, pathway):
        # Create and show Scene3

        self.scene3 = Scene3(self.container, self, pathway)
        self.scene3.grid(row=0, column=0, sticky="nsew")
        self.show_frame(self.scene3)


    def show_scene4(self, name):
        # Create or update Scene4

        if not self.scene4:
            self.scene4 = Scene4(self.container, self, name)
            self.scene4.grid(row=0, column=0, sticky="nsew")
        else:
            self.scene4.update_profile_name(name)

        self.show_frame(self.scene4)

        # Automatically continue to Scene5 after 10 seconds
        self.after(10000, lambda: self.show_scene5(name))


    def show_scene5(self, name):
        # Create or update Scene5

        if not self.scene5:
            self.scene5 = Scene5(self.container, self, name)
            self.scene5.grid(row=0, column=0, sticky="nsew")
        else:
            self.scene5.update_profile_name(name)
            self.scene5.start_audio()

        self.show_frame(self.scene5)


# ================================
# APPLICATION ENTRY POINT
# ================================

if __name__ == "__main__":
    App().mainloop()
