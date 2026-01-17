
import tkinter as tk
# tkinter wordt gebruikt om de GUI te maken

from PIL import Image, ImageTk
# PIL (Pillow) wordt gebruikt om afbeeldingen in de GUI te laden en weer te geven

from profiles import ontmoeten_profiles, contacten_profiles
# Import van profielgegevens (lijsten met dictionaries)



class Scene3(tk.Frame):
    def __init__(self, parent, controller, pathway="ontmoeten"):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.pathway = pathway

        # Kies de juiste lijst afhankelijk van pathway
        if pathway == "ontmoeten":
            self.profiles = ontmoeten_profiles
        else:
            self.profiles = contacten_profiles

        self.index = 0  # start altijd bij het eerste profiel

        # ---------------- TOP SECTION ----------------
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=44, pady=32)

        # Titel bovenaan: "Ontmoeten" of "Contacten"
        self.title_label = tk.Label(
            main_frame,
            text="Ontmoeten" if pathway == "ontmoeten" else "Contacten",
            font=("Arial", 42, "bold"),
            fg="black",
            bg="white"
        )
        self.title_label.pack(anchor="w")

        # Horizontale separator
        separator = tk.Frame(main_frame, bg="#999999", height=2)
        separator.pack(fill=tk.X, pady=(8, 24))

        # Content frame: linker en rechter kolom
        content = tk.Frame(main_frame, bg="white")
        content.pack(fill=tk.BOTH, expand=True)

        # ---------------- LEFT COLUMN ----------------
        left_column = tk.Frame(content, bg="white")
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Profielnaam label
        self.name_label = tk.Label(left_column, text="", font=("Arial", 34, "bold"), fg="black", bg="white")
        self.name_label.pack(anchor="w", pady=(0,0))

        # Profielbeschrijving label
        self.desc_label = tk.Label(left_column, text="", font=("Arial", 26), fg="black", bg="white", justify="left")
        self.desc_label.pack(anchor="w")

        # ---------------- RIGHT COLUMN (NAVIGATIE PIJLEN) ----------------
        right_column = tk.Frame(content, bg="white")
        right_column.pack(side=tk.RIGHT, padx=(32,0), fill=tk.Y)

        # Pijl omhoog
        self.up_btn = tk.Canvas(right_column, width=128, height=64, bg="white", highlightthickness=0)
        self.up_btn.pack(pady=(60,8))  # pijlen hoger plaatsen
        self.up_btn.create_polygon(64,4,112,54,16,54, fill="#1E73B9", outline="")
        self.up_btn.bind("<Button-1>", lambda e: self.prev_profile())

        # Pijl omlaag
        self.down_btn = tk.Canvas(right_column, width=128, height=64, bg="white", highlightthickness=0)
        self.down_btn.pack(pady=(8,60))  # pijlen gecentreerd
        self.down_btn.create_polygon(64,60,112,10,16,10, fill="#1E73B9", outline="")
        self.down_btn.bind("<Button-1>", lambda e: self.next_profile())

        # ---------------- BLUE BACKGROUND ----------------
        bottom_height = 55
        self.blue_bg = tk.Canvas(self, width=800, height=bottom_height, bg="#327FBE", highlightthickness=0)
        self.blue_bg.place(x=0, y=480-bottom_height)

        # ---------------- BUTTONS ----------------
        button_height = 90
        y_buttons = int(480 - bottom_height/2 - button_height + 20)
        x_left = 0
        x_right = 800 - 320

        # GROENE BELKNOP
        bell_image = Image.open("images/bel_wit.png").resize((60,60), Image.LANCZOS)
        self.bell_photo = ImageTk.PhotoImage(bell_image)

        self.green = tk.Canvas(self, width=320, height=button_height, bg="white", highlightthickness=0)
        self.draw_round_top_right(self.green,0,0,320,button_height,20,fill="#327FBE",outline="#327FBE")
        self.draw_round(self.green,8,8,312,82,20,fill="#2E7D32",outline="#327FBE",width=4)

        # Tekst "Bellen"
        self.green.create_text(110,45,text="Bellen",font=("Arial",36,"bold"),fill="white")

        # Bel icoon
        self.green.create_image(220,45,image=self.bell_photo)
        self.green.place(x=x_left,y=y_buttons)
        self.green.bind("<Button-1>", lambda e: self.call_profile())

        # RODE BACK KNOP naar Scene1
        self.red = tk.Canvas(self, width=320, height=button_height, bg="white", highlightthickness=0)
        self.draw_round_top_left(self.red,0,0,320,button_height,20,fill="#327FBE",outline="#327FBE")
        self.draw_round(self.red,8,8,312,82,20,fill="#E53935",outline="#327FBE",width=4)
        self.red.create_text(160,45,text="Back",font=("Arial",36,"bold"),fill="white")
        self.red.place(x=x_right,y=y_buttons)
        self.red.bind("<Button-1>", lambda e: self.controller.show_frame("Scene1"))

        # Toon eerste profiel bij start
        self.show_profile()

    # ---------------- PROFIEL NAVIGATIE ----------------
    def show_profile(self):
        # Update naam en beschrijving van huidig profiel
        p = self.profiles[self.index]
        self.name_label.config(text=f"{p['name']} ({p['age']})")
        self.desc_label.config(text=p["description"])

    def next_profile(self):
        # Ga naar volgende profiel (indien mogelijk)
        if self.index < len(self.profiles) - 1:
            self.index += 1
            self.show_profile()

    def prev_profile(self):
        # Ga naar vorige profiel (indien mogelijk)
        if self.index > 0:
            self.index -= 1
            self.show_profile()

    # ---------------- PROFIEL BELKNOP ----------------
    def call_profile(self):
        """Ga naar Scene4 en geef de huidige profielnaam door"""
        profile_name = self.profiles[self.index]["name"]
        self.controller.show_test_scene(profile_name=profile_name)

    # ---------------- HULPFUNCTIE ----------------
    def get_current_profile_name(self):
        # Geef huidige profielnaam terug
        return self.profiles[self.index]["name"]

    # ---------------- ROUND HELPERS ----------------
    # Functies om afgeronde knoppen te tekenen
    def draw_round(self, canvas, x1, y1, x2, y2, r, **kwargs):
        points = [x1+r,y1,x2-r,y1,x2,y1,x2,y1+r,x2,y2-r,x2,y2,x2-r,y2,x1+r,y2,x1,y2,x1,y2-r,x1,y1+r,x1,y1]
        canvas.create_polygon(points, smooth=True, **kwargs)

    def draw_round_top_right(self, canvas, x1, y1, x2, y2, r, **kwargs):
        canvas.create_rectangle(x1,y1,x2-r,y1+r, **kwargs)
        canvas.create_arc(x2-2*r,y1,x2,y1+2*r, start=0, extent=90, style=tk.PIESLICE, **kwargs)
        canvas.create_rectangle(x1,y1+r,x2,y2, **kwargs)

    def draw_round_top_left(self, canvas, x1, y1, x2, y2, r, **kwargs):
        canvas.create_arc(x1,y1,x1+2*r,y1+2*r, start=90, extent=90, style=tk.PIESLICE, **kwargs)
        canvas.create_rectangle(x1+r,y1,x2,y1+r, **kwargs)
        canvas.create_rectangle(x1,y1+r,x2,y2, **kwargs)
