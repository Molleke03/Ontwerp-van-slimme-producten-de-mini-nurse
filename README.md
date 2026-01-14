# Ontwerp-van-slimme-producten-de-mini-nurse
De Mini Nurse is ontwikkeld vanuit het inzicht dat (dementie)patiënten vaak terechtkomen in een onbekende omgeving of situatie. Als geliefde kun je niet altijd aanwezig zijn op de momenten dat het écht nodig is. In geval van onrust of desoriëntatie kan de patiënt op een knop drukken, waarna jouw stem (vertrouwde stem van een geliefde) te horen is. 

## Vormontwerp

## Elektronica
### Benodigdheden
Het systeem bestaat uit:
- Raspberry pi model 4b
- 5 inch HDMI display (800x480 pixels)
- Audio amplifier TPA2016D2
- 2x speaker 3W 8ohm
- Encoder module (potentiometer)
- 4x drukknop

- Kabel USB-C --> USB-A + adapter
- Kabel HDMI mini --> HDMI
- Kabel micro USB --> USB-A + adapter
- Kabel male 3.5mm jack stereo --> male 2x RCA aux (is vervolgens nog bewerkt)
- Arduino draadjes

### Aansluitingen
De Raspberry Pi fungeert als het kloppend hart van het ontwerp, want het is de centrale besturingseenheid die alle componenten met elkaar kan verbinden.
Het wordt gevoed via zijn eigen USB-voeding (USB-C), die op het net verbonden is. 

De Raspberry Pi is vervolgens met het 5-inch HDMI-display verbonden via een HDMI-kabel. Ook het display wordt gevoed met een aparte netadapter via de voedingsaansluiting van het display (USB micro). Op deze manier kan er een beeld gecreëerd worden.

Om geluid te krijgen uit de raspberry is een 3.5mm jack stereo ingezet die overgaat naar 2x RCA aux koppen. Wel zijn deze RCA aux knoppen geknipt geweest, zodat deze aangesloten kan worden aan de audio amplifier en bijgevolg de speakers. Door deze uitgangen te knippen kon er handmatig draadjes gesoldeert worden. Deze arduino draadjes worden geconnecteerd aan de pinnen R-, R+, L+ en L-.
Om deze audio amplifier correct te gebruiken, moeten er ook enkele pinnen verbonden zijn met de raspberry pi. Zo wordt zowel de VDD als I2C van de amplifier verbonden met de 5V power van de raspberry, wat zich bevindt op pin 2. De GND van de amplifier wordt zoals verwacht verbonden met de GND van de raspberry op pin 14. 
Aan de andere kant van de audio amplifier worden er 2 speakers geschakeld, waarbij + verbonden wordt met + en - verbonden met -.

Ook is er een potentiometer (encoder module) gebruikt om het volume te regelen in ons ontwerp. Ook hier moet dit component verbonden worden met de raspberry pi. De GND wordt opnieuw verbonden met de GND op pin 4 van de raspberry. Omdat de potentiometer enkel werkt op 3.3V wordt de + verbonden met de 3.3V power van de raspberry. Dit is pin 17. De SW is geconnecteerd aan GPIO25 (pin 22), de DT aan GPIO8 (pin 24) en de CLK aan GPIO7 (pin 26).

Tot slot zijn er 4 drukkknoppen nodig om het display te besturen en dus interactie te doen met het ontwerp. De verdeling van de knoppen gebeuren van links naar rechts, waarbij deze volgorde (back, confirm, naar boven, naar onder) de functies beschrijft van de knop. Iedere knop wordt verbonden met dezelfde GND op de raspberry, namelijk pin 6. De positieve kant wordt verbonden met een GPIO pin van de raspberry. 
- Back knop           --> GPIO23 (pin 16)
- Confirm knop        --> GPIO22 (pin 15)
- Naar boven knop     --> GPIO27 (pin 13)
- Naar onder knop     --> GPIO17 (pin 11)

Doordat sommige draden op dezelfde pin terechtkomen van de raspberry worden er hersluitbare lasklemmen gebruikt van het merk Kopp.

Alle aangesloten modules delen een gemeenschappelijke massa (GND) via de Raspberry Pi.


Onderstaande afbeelding heeft de gehele schema weer, hoe alles geschakeld moet zijn.
<img width="1983" height="1759" alt="Elektronica schema" src="https://github.com/user-attachments/assets/fe171d56-499d-4bfd-9e24-fea087e7abce" />




