# CONVO 
De Mini Nurse is ontwikkeld vanuit het inzicht dat (dementie)patiënten vaak terechtkomen in een onbekende omgeving of situatie. Als geliefde kun je niet altijd aanwezig zijn op de momenten dat het écht nodig is. In geval van onrust of desoriëntatie kan de patiënt op een knop drukken, waarna jouw stem (vertrouwde stem van een geliefde) te horen is. 

## Vormontwerp
Het ontwerp van CONVO is gebaseerd op de tijdloze designprincipes van BRAUN. De volledig witte behuizing wordt verfijnd door zachte zilveren accenten, die de draaiknop, drukknoppen en de afgeronde randen van de body subtiel benadrukken. Deze rustige en herkenbare vormgeving zorgt ervoor dat CONVO vertrouwd aanvoelt en harmonieus past binnen verschillende woonomgevingen.

foto's van afgewerkte convo

### Ontwikkelproces van CONVO
Bij de creatie van het product werd gebruik gemaakt van de prusa MK4 3D-printer. Deze 3D-printe de knoppen, body en het onderstel. Volgende onderdelen werden allen uitgewerkt in de 3D-model software NX.
<br>Welke setting, kleuren en hoe de onderdelen af te werken leggen we kort uit.

#### De knoppen
foto's van de 5 knoppen
Alle knoppen werden geprint met:
- 0.15 mm QUALITY setting
- tree support
- 0.4 mm nozzle
- vulling van 15%

Knop 1,2 en 3 werden vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur wit. Na het printproces werden de knoppen afgewerkt met een zilverkleurige spuitlak.<br> Knop 4 werd vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur rood. <br> Knop 5 werd vervaardigd via 3D-printing met Polymaker Panchroma PLA Satin in de kleur groen.

#### De body
foto van de body deel 1 en 2
Beide stukken werden geprint met:
- 0.15 mm QUALITY setting
- tree support
- 0.4 mm nozzle
- vulling van 30%
- Polymaker Panchroma PLA Satin in de kleur wit

Na het printproces werden van beide onderdelen de edges afgewerkt met een zilverkleurige spuitlak. Hierna werd het logo "CONVO" geplaatst op de behuizing met behulp van een stikker en werd ook dit afgewerkt met een zilveren spuitlak.

#### Het onderstel
foto van het onderstel
Volgend onderdeel werd geprint met:
- 0.15 mm QUALITY setting
- raster support
- 0.4 mm nozzle
- vulling van 15%
- Polymaker Panchroma PLA Satin in de kleur wit

## Elektronica
### Benodigdheden
Het systeem bestaat uit:
- Raspberry pi model 4B
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
#### Raspberry pi en voeding
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




