# CONVO 
*Convo, a tool for connection and conversation* <br>
_____
Convo is een innovatief communicatieapparaat ontworpen voor ouderen die zich eenzaam voelen of moeite hebben met moderne technologie. Veel bestaande digitale oplossingen zijn te complex, waardoor net de mensen die het meest nood hebben aan sociaal contact worden uitgesloten.

Het product richt zich op ouderen die eenvoud en duidelijkheid nodig hebben. Het apparaat bestaat uit een helder display, vier grote fysieke knoppen en ingebouwde speakers. Met één druk op de knop kunnen gebruikers eenvoudig contact maken met een familielid of een andere persoon die openstaat voor een babbeltje.

## Vormontwerp
Het ontwerp van CONVO is gebaseerd op de tijdloze designprincipes van BRAUN. De volledig witte behuizing wordt verfijnd door zachte zilveren accenten, die de draaiknop, drukknoppen en de afgeronde randen van de body subtiel benadrukken. Deze rustige en herkenbare vormgeving zorgt ervoor dat CONVO vertrouwd aanvoelt en harmonieus past binnen verschillende woonomgevingen.

<img width="1920" height="1080" alt="github 2" src="https://github.com/user-attachments/assets/4552cc56-3de8-4f11-9cfa-3c79afd99a7a" />


### Ontwikkelproces van CONVO
Bij de creatie van het product werd gebruik gemaakt van de prusa MK4 3D-printer. Deze 3D-printe de knoppen, body, onderstel en de zijkanten. Volgende onderdelen werden allen uitgewerkt in de 3D-model software NX.

<img width="1298" height="684" alt="Schermafbeelding 2026-01-16 111215" src="https://github.com/user-attachments/assets/a6f5c804-302b-4509-a808-203c2ab8c65c" />
<br>Welke setting, kleuren en hoe de onderdelen af te werken leggen we kort uit.

#### De knoppen
<img width="1259" height="374" alt="knoppen github" src="https://github.com/user-attachments/assets/28eefafe-7d6e-4e0d-b752-ef2ddffc763c" />

Alle knoppen werden geprint met:
- 0.15 mm QUALITY setting
- tree support
- 0.4 mm nozzle
- vulling van 15%

Knop 1 werd vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur groen.<br>
Knop 2 werd vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur rood. <br>
Knop 3, 4 en 5 werden vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur wit. Na het printproces werden de knoppen afgewerkt met een zilverkleurige spuitlak.

#### De body
<img width="1259" height="374" alt="body" src="https://github.com/user-attachments/assets/7d014f0e-e93c-4f3b-8cf0-93d97338da73" />

Beide stukken werden geprint met:
- 0.15 mm QUALITY setting
- tree support
- 0.4 mm nozzle
- vulling van 30%
- Polymaker Panchroma PLA Satin in de kleur wit

Na het printproces werden van beide onderdelen de edges afgewerkt met een zilverkleurige spuitlak. Hierna werd het logo "CONVO" geplaatst op de behuizing met behulp van een stikker en werd ook dit afgewerkt met een zilveren spuitlak.

#### Het onderstel
<img width="1259" height="374" alt="onderstel" src="https://github.com/user-attachments/assets/1b288362-2004-4073-bbb8-b2ab894fd57e" />

Volgend onderdeel werd geprint met:
- 0.15 mm QUALITY setting
- raster support
- 0.4 mm nozzle
- vulling van 15%
- Polymaker Panchroma PLA Satin in de kleur wit

#### De zijkanten
<img width="1259" height="374" alt="zijkanten" src="https://github.com/user-attachments/assets/3c14e3a1-b086-4e12-a537-1a34ef7e40cc" />

Volgend onderdeel werd geprint met:
- 0.15 mm QUALITY setting
- 0.4 mm nozzle
- vulling van 15%
- Polymaker Panchroma PLA Satin in de kleur wit

## Elektronica
### Benodigdheden
Het systeem bestaat uit:
- Raspberry Pi model 4B
- 5 inch HDMI-display (800x480 pixels)
- Audio amplifier TPA2016D2
- 2x speaker (3W, 8Ω)
- Encoder module (rotary encoder/ potentiometer))
- 4x drukknop
- USB-C → USB-A kabel met adapter
- Mini-HDMI → HDMI kabel
- Micro-USB → USB-A kabel met adapter
- 3.5 mm jack stereo → 2x RCA aux kabel (bewerkt)
- Arduino jumpdraadjes

### Aansluitingen
#### Raspberry Pi en voeding
De Raspberry Pi fungeert als het kloppend hart van het ontwerp en vormt de centrale besturingseenheid waaraan alle componenten zijn gekoppeld. De Raspberry Pi wordt gevoed via een USB-C-voeding die rechtstreeks op het elektriciteitsnet is aangesloten.

#### Display
De Raspberry Pi is via een HDMI-kabel verbonden met het 5 inch HDMI-display. Het videosignaal wordt digitaal via HDMI doorgestuurd.
Het display heeft een aparte voeding, die wordt aangesloten via een micro-USB-connector en een netadapter. Hierdoor kan het display onafhankelijk van de Raspberry Pi pinnen toch functioneren en wordt het beeld correct weergegeven.

#### Audio
Voor de geluidsuitvoer wordt gebruikgemaakt van de 3.5 mm stereo jack-uitgang van de Raspberry Pi. Deze uitgang is verbonden met een 3.5 mm jack naar 2 × RCA aux kabel.
De RCA-connectoren zijn afgeknipt zodat de afzonderlijke signaaldraden handmatig konden worden gesoldeerd.

De gesoldeerde Arduino-draadjes zijn aangesloten op de audio amplifier TPA2016D2 via de volgende aansluitingen:
- R+ en R- voor het rechter audiokanaal
- L+ en L- voor het linker audiokanaal

Om de audio amplifier correct te laten functioneren, zijn bijkomende verbindingen met de Raspberry Pi gemaakt:
- VDD en I2C van de amplifier zijn verbonden met de 5 V voeding van de Raspberry Pi (pin 2)
- GND van de amplifier is verbonden met GND van de Raspberry Pi (pin 14)

Aan de uitgangszijde van de audio amplifier zijn twee luidsprekers aangesloten. Hierbij wordt telkens de positieve pool (R+ en L+) met de positieve uitgang verbonden en de negatieve pool (R- en L-) met de negatieve uitgang.

#### Encoder module (potentiometer)
Voor het regelen van het volume wordt een encoder module gebruikt. Deze is als volgt aangesloten op de Raspberry Pi:
- GND → GND van de Raspberry Pi (pin 4)
- VCC (+) → 3.3 V van de Raspberry Pi (pin 17)
(de encoder werkt uitsluitend op 3.3 V)
- SW → GPIO25 (pin 22)
- DT → GPIO8 (pin 24)
- CLK → GPIO7 (pin 26)

Door het draaien van de encoder kan het volume aangepast worden.

#### Drukknoppen
Tot slot zijn er vier drukknoppen voorzien voor de bediening van het display en de gebruikersinterface. De knoppen zijn van links naar rechts toegewezen aan de volgende functies:
- Back
- Confirm
- Naar boven
- Naar onder

Elke drukknop is aangesloten volgens hetzelfde principe:
- Eén pin → GND van de Raspberry Pi (pin 6)
- Eén pin → GPIO-pin

De GPIO-toewijzing is als volgt:
- Back knop → GPIO23 (pin 16)
- Confirm knop → GPIO22 (pin 15)
- Naar boven knop → GPIO27 (pin 13)
- Naar onder knop → GPIO17 (pin 11)



Omdat meerdere draden op dezelfde pin van de Raspberry Pi uitkomen, worden hersluitbare lasklemmen van het merk Kopp gebruikt om de verbindingen overzichtelijk en veilig te houden.


Onderstaande afbeelding heeft het gehele schema weer om alles wat te verduidelijken.
<img width="1983" height="1759" alt="Elektronica schema" src="https://github.com/user-attachments/assets/fe171d56-499d-4bfd-9e24-fea087e7abce" />


## Code

### Uitvoeren
1. Start de Raspberry Pi en log in.
2. Plaats alle codebestanden, afbeeldingen en het geluidsfragment volgens de mapstructuur hieronder op de Raspberry Pi.
3. Pas de locatie van het geluidsfragment in `scene5.py` aan aan de hand van de locatie op de Raspberry Pi.
4. Open **Thonny Python IDE**.
5. Installeer vereiste **libraries** (zie onderstaande sectie).
6. Open het Python-bestand `main.py` via **File → Open**.
7. Sluit eventuele hardware aan op de GPIO-pinnen.
8. Klik op **Run (F5)** om het script uit te voeren.

---

### Mapstructuur

<ul class="tree">
  <li>📁 Python_finaal
    <ul>
      <li>📄 main.py </li>
        <li>📄 profiles.py </li>
      <li>📄 scene0.py </li>
        <li>📄 scene1.py </li>
        <li>📄 scene2.py </li>
        <li>📄 scene3.py </li>
        <li>📄 scene4.py </li>
        <li>📄 scene5.py </li>
      <li>📁 images
        <ul>
          <li>🖼️ megafoon.png</li>
          <li>🖼️ bel_blauw.png</li>
          <li>🖼️ bel_wit.png</li>
          <li>🖼️ + grijs.png</li>
          <li>🖼️ + groen.png</li>
          <li>🖼️ hart_grijs.png</li>
          <li>🖼️ hart_groen.png</li>
        </ul>
      </li>
      <li>📁 geluid
        <ul>
          <li>📄 gesprek.mp3</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>


### libraries
### Standaard op Raspberry Pi OS
- tkinter
- queue
- time
- datetime
- subprocess
- RPi.GPIO
- gpiozero

### Externe libraries
- Pillow
- pygame

Installatie (indien nodig):
```bash
pip3 install pillow pygame
sudo apt install python3-gpiozero python3-rpi.gpio
```


### uitleg code
De uitleg van de opbouwing van de code is te vinden in elk code bestand.

### Flowchart
De logica van de code volgt onderstaande flowchart:

<img width="1983"  alt="Flowchart" src="https://github.com/user-attachments/assets/88182090-89c3-4339-b0ac-eb6d112e6510" />

