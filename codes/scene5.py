import tkinter as tk
# Importeer tkinter om vensters, frames en labels te maken

from PIL import Image, ImageTk
# Importeer Pillow om afbeeldingen te laden en in tkinter te tonen

import RPi.GPIO as GPIO
# Raspberry Pi GPIO-bibliotheek om fysieke pinnen te gebruiken

import time
# Om vertragingen en debouncing voor de encoder te regelen

import subprocess
# Om systeemvolume via terminalcommando's aan te passen

import pygame
# Voor audio-afspelen (loopend tijdens het bellen)


# ======================
# AUDIO-INSTELLINGEN
# ======================

AUDIO_PATH = "source path audio /geluid/gesprek.mp3"
# Pad naar het audiobestand dat wordt afgespeeld tijdens het bellen

MAX_VOLUME = 90
# Maximale toegestane volume-instelling (in procenten)

STEP = 5
# Hoeveel het volume omhoog of omlaag gaat per stap van de rotary encoder


# ======================
# GPIO PIN-INSTELLINGEN VOOR ROTARY ENCODER
# ======================

CLK = 7
# Clock-pin van de rotary encoder

DT = 8
# Data-pin van de rotary encoder

SW = 25
# Schakelaar-knop (drukknop) van de rotary encoder


class Scene5(tk.Frame):
# ======================
# Scene5: Bellen-scherm
# ======================

    def __init__(self, parent, controller=None, profile_name=None):
        # Automatisch uitgevoerd bij het aanmaken van Scene5

        super().__init__(parent, bg='white')
        # Frame initialiseren met witte achtergrond

        self.controller = controller
        # Referentie naar het hoofdprogramma opslaan

        self.profile_name = profile_name or "Peter Wilson"
        # Stel profielnaam in of gebruik standaardnaam


        # ======================
        # UI OPBOUWEN
        # ======================

        self.build_ui()
        # Creëer alle visuele elementen van de scene


        # ======================
        # ROTARY ENCODER CONFIGURATIE
        # ======================

        GPIO.setmode(GPIO.BCM)
        # Gebruik BCM-pin nummering

        GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # Stel pins in als input met pull-up weerstand

        self.clk_last = GPIO.input(CLK)
        # Bewaar de huidige staat van CLK voor vergelijking bij rotatie

        self.after(10, self.poll_encoder)
        # Start het continue controleren van de encoder


        # ======================
        # AUDIO STARTEN
        # ======================

        self.start_audio()
        # Speel het belgeluid direct af


    # ======================
    # USER INTERFACE (UI)
    # ======================

    def build_ui(self):
        # Bouw het scherm met labels, afbeeldingen en knoppen

        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Hoofdframe dat de volledige ruimte vult

        # ---- Titel ----
        tk.Label(main_frame,
                 text="U bent aan het bellen!",
                 font=("Arial",44,"bold"),
                 fg="black",
                 bg="white").pack(pady=(120,0))
        # Titel bovenaan het scherm

        # ---- Profielnaam ----
        self.name_label = tk.Label(main_frame,
                                   text=self.profile_name,
                                   font=("Arial",32),
                                   fg="black",
                                   bg="white")
        self.name_label.pack(pady=(0,20))
        # Toont dynamisch de naam van de persoon die gebeld wordt

        # ---- Telefoon afbeelding ----
        try:
            call_image = Image.open("images/bel_blauw.png").resize((120,120))
            self.call_photo = ImageTk.PhotoImage(call_image)
            call_lbl = tk.Label(main_frame, image=self.call_photo, bg="white")
        except Exception:
            # Als de afbeelding niet kan worden geladen
            call_lbl = tk.Label(main_frame,
                                text="[telefoon-icoon]",
                                font=("Arial",18),
                                fg="#1E73B9",
                                bg="white")
        call_lbl.pack(pady=0)
        # Toon het icoon of een tekstplaceholder

        # ---- Blauwe onderbalk ----
        bottom_height = 55
        self.bottom_bar = tk.Frame(self, bg="#0082C1", height=bottom_height)
        self.bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)
        # Onderbalk onderaan het scherm


        # ---- Knoppen onderaan ----
        button_height = 90
        y_buttons = 480 - bottom_height - button_height + 20
        x_left = 0
        x_right = 800 - 320

        # Groene knop: +Contact
        self.green = tk.Canvas(self, width=320, height=button_height, bg="white", highlightthickness=0)
        self.draw_round_top_right(self.green, 0, 0, 320, button_height, 20, fill="#327FBE", outline="#327FBE")
        self.draw_round(self.green, 8,8,312,82,20, fill="#2E7D32", outline="#327FBE", width=4)
        self.green.create_text(160,45, text="+Contact", font=("Arial",36,"bold"), fill="white")
        self.green.place(x=x_left, y=y_buttons)

        # Rode knop: Menu
        self.red = tk.Canvas(self, width=320, height=button_height, bg="white", highlightthickness=0)
        self.draw_round_top_left(self.red, 0,0,320,button_height,20, fill="#327FBE", outline="#327FBE")
        self.draw_round(self.red, 8,8,312,82,20, fill="#E53935", outline="#327FBE", width=4)
        self.red.create_text(160,45, text="Menu", font=("Arial",36,"bold"), fill="white")
        self.red.place(x=x_right, y=y_buttons)
        # Plaats beide knoppen aan de onderkant


    # ======================
    # AUDIO FUNCTIES
    # ======================

    def start_audio(self):
        # Start het belgeluid in een lus
        pygame.mixer.init()
        pygame.mixer.music.load(AUDIO_PATH)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

    def stop_audio(self):
        # Stop het belgeluid en maak resources vrij
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        GPIO.cleanup()


    # ======================
    # ROTARY ENCODER FUNCTIES
    # ======================

    def poll_encoder(self):
        # Blijf continu de encoder controleren
        clk = GPIO.input(CLK)
        dt = GPIO.input(DT)

        if clk != self.clk_last and clk == GPIO.LOW:
            # Detecteer draaiing
            if dt != clk:
                self.volume_up()
            else:
                self.volume_down()
            time.sleep(0.03)  # debounce

        self.clk_last = clk

        # Drukknop SW
        if GPIO.input(SW) == GPIO.LOW:
            self.toggle_mute()
            time.sleep(0.3)  # debounce

        self.after(10, self.poll_encoder)
        # Herhaal polling


    # ======================
    # VOLUME CONTROLE
    # ======================

    def get_volume(self):
        # Lees huidig systeemvolume in procenten
        out = subprocess.check_output(["pactl","get-sink-volume","@DEFAULT_SINK@" ]).decode()
        return int(out.split("/")[1].replace("%","").strip())

    def volume_up(self):
        # Verhoog volume als het onder MAX_VOLUME is
        if self.get_volume() < MAX_VOLUME:
            subprocess.call(["pactl","set-sink-volume","@DEFAULT_SINK@",f"+{STEP}%"])

    def volume_down(self):
        # Verlaag volume
        subprocess.call(["pactl","set-sink-volume","@DEFAULT_SINK@",f"-{STEP}%"])

    def toggle_mute(self):
        # Zet mute aan of uit
        subprocess.call(["pactl","set-sink-mute","@DEFAULT_SINK@","toggle"])


    # ======================
    # PROFIELNAAM DYNAMISCH UPDATEN
    # ======================

    def update_profile_name(self, name):
        # Update de naam op het scherm
        self.name_label.config(text=name)


    # ======================
    # HELPERS OM RONDE KNOPPEN TE TEKENEN
    # ======================

    def draw_round(self, canvas, x1, y1, x2, y2, r, **kwargs):
        # Tekent een afgeronde rechthoek
        points = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2, x2-r, y2,
                  x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1]
        canvas.create_polygon(points, smooth=True, **kwargs)

    def draw_round_top_right(self, canvas, x1, y1, x2, y2, r, **kwargs):
        # Tekent een rechthoek met afgeronde rechterbovenhoek
        canvas.create_rectangle(x1, y1, x2 - r, y1 + r, **kwargs)
        canvas.create_arc(x2 - 2*r, y1, x2, y1 + 2*r, start=0, extent=90, style=tk.PIESLICE, **kwargs)
        canvas.create_rectangle(x1, y1 + r, x2, y2, **kwargs)

    def draw_round_top_left(self, canvas, x1, y1, x2, y2, r, **kwargs):
        # Tekent een rechthoek met afgeronde linkerbovenhoek
        canvas.create_arc(x1, y1, x1 + 2*r, y1 + 2*r, start=90, extent=90, style=tk.PIESLICE, **kwargs)
        canvas.create_rectangle(x1 + r, y1, x2, y1 + r, **kwargs)
        canvas.create_rectangle(x1, y1 + r, x2, y2, **kwargs)
