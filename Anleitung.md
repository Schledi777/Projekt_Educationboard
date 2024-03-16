# Anleitung Menu Steuerung  
## 1. Raspberry Pi Pico mit Stromquelle verbinden

Bild

## 2. Mit dem Drehpotentiometer Programm auswählen
Durch drehen des Drehpotentiometers die Liste bzw. das Menu zu navigieren, um die Auswahl zu ändern.
Verwenden des Rotary Encoders, um durch die Liste zu navigieren. Drehungen im Uhrzeigersinn um nach unten zu navigieren und gegen den Uhrzeiger um die Auswahl nach oben zu ändern.

Bild

## 3. Auswahl des PythonProgramms
Durch das eindrücken des Rotery Encoders, wird das ausgewählte PythonProgramm ausgeführt. 

Bild

## 4. Verlassen des PythonProgramms
Um das laufende Programm zu Verlassen muss der Griff des Rotery Encoder wieder eingedrückt werden, wie für's starten

# Anleitung um eigene Programme ins Menu einzufügen (Bsp DHT11 Programm)

Das wichtigste Zuerst das Menu Programm: [main.py]() sollte auf dem Pi schon installiert sein.

## 1. Programm Testen

Erstmal das Programm im Compailer compilieren und alle Knöpfe bzw. Sensoren/Aktuatoren auf funktionalität Testen. In unserem Fall hat das Programm für den DHT11 Sensor funktioniert und wir bekommen eine Ausgabe auf dem OLED.
![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e0e80df9-71fe-4305-bc10-b21786a1ecb9)


## 2. Return to Menu Baustein einfügen
Nun den Code vom Programm: [**'Return_to_Menu_Button.py'**](https://github.com/Schledi777/Projekt_Educationboard/blob/f0250ac8361fecf064085da8ad1dc9779a7f3361/Programme/Baustein_%26_Test_Prg/Return_to_Menu_Button.py
) einfügen dabei kann ein belibiger Button gewählt werden, im BausteinCode ist der definierte Button vom Rotery Encoder. 

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e09c8307-8410-4275-b465-ed2b0e1fe973)


Wie in dieser Abbildung zuerkennen haben wir in Zeile haben wir in Zeile 3 **Pin** aus der Bibliothek **machine** und in Zeile 7 die Biliothek **sys** hinzugefügt.
In Zeile 11 haben wir den Knopf definiert mit dem wir zurück in Menu kommen mit dem Befehl:**'button_pin = Pin(9, Pin.IN, Pin.PULL_UP)'**.
Von Zeile 18 bis 32 kommt definiern wir eine funktion names **button_pressed** die das laufende Programm unterbricht und das Menu Programm **'main.py'** startet.

Nach dem Compalieren sollte das Programm erneut getestet werden und entstande Fehler korrigieren, wie z.Bsp.: die vergessene Bibliothek sys hinzuzufügen. 
Wenn es funktioniert wird in unserem Fall das Menu Programm gestartet, wenn man den Knopf bzw. Button des Rotery Encoders eindrückt.


## 3. Programm auf Raspberry Speichern
Wie in der [Dokumentation.md]() erwähnt werden die Schritte 7. & 8. getätigt:

1. Um Programme auf den Pi zu Speichern aktuelles Programm offen haben, dann unter Registerkarte '**Datei**' und dort dann '**Speichern unter...**' auswählen. Dann öffnet sich ein weiteres Menu, in welchen man zwischen Computer und Raspberry entscheiden kann. Dort auf '*Raspberry PI Pico*' klicken und es öffnet sich das Laufwerk des Pico's.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/c90597f6-1f10-41f3-83e9-54ec1b6c77ba)
   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/f4fce567-db69-4507-a5c5-a597cba172cb)



2. Programm mit seinem Wunschnamen und der Endung'.py' benennen z.Bsp.: **Temp&Lft.py** und mit dem auswählen von 'OK' wird das Programm gespeichert

   BILD

## 4. Programm im Menu Testen


