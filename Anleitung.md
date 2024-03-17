# Anleitung

## Gliederung:
### 1. Anleitung Menu Steuerung  
### 2. Anleitung um eigene Programme ins Menu einzufügen (Bsp DHT11 Programm)
### 3. Anleitung Intgration OLED

---

# 1. Anleitung Menu Steuerung  

## 1.1 Raspberry Pi Pico mit Stromquelle verbinden
Der Raspberry Pi Pico wird an eine Stromquelle mit einem Micro-USB Kabel verbunden, dass kann ein PowerBank sein oder auch ein Pc Outlet                  

## 1.2 Mit dem Drehpotentiometer Programm auswählen
Um die Auswahl zu ändern, verwenden Sie bitte das Drehpotentiometer, um durch die Liste oder das Menü zu navigieren. Der Rotary Encoder ermöglicht es Ihnen, durch die Liste zu blättern. Drehen Sie ihn im Uhrzeigersinn, um nach unten zu navigieren, und gegen den Uhrzeigersinn, um die Auswahl nach oben zu ändern.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/61042c13-0abd-4a33-968d-5a10c7bdb27e)


## 1.3 Auswahl des PythonProgramms
Durch das eindrücken des Rotery Encoders, wird das ausgewählte PythonProgramm z.Bsp.:'Temp&Lft.py' ausgeführt. 

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/bc909d34-2d3c-4eb6-84a5-d6efe6d22890)
![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/411476dc-f5dc-4478-af1d-27636dcca7c3)


## 1.4 Verlassen des PythonProgramms
Um das laufende Programm zu verlassen, müssen Sie den Griff des Rotary Encoders erneut drücken, wie beim Starten.


---


# 2. Anleitung um eigene Programme ins Menu einzufügen (Bsp DHT11 Programm)

Das wichtigste Zuerst das Menu Programm: [main.py](https://github.com/Schledi777/Projekt_Educationboard/blob/0e447e8d7ff2c907a0dd9716c9d91fd424211b08/Programme/main.py) sollte auf dem Pi schon installiert sein.

## 2.1 Programm Testen

Zuerst müssen Sie das Programm im Compiler kompilieren und alle Knöpfe sowie Sensoren/Aktuatoren auf ihre Funktionalität überprüfen. In unserem Fall hat das Programm für den DHT11-Sensor funktioniert, und wir erhalten eine Ausgabe auf dem OLED-Display.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e0e80df9-71fe-4305-bc10-b21786a1ecb9)


## 2.2 Return to Menu Baustein einfügen
Nun den Code vom Programm: [**'Return_to_Menu_Button.py'**](https://github.com/Schledi777/Projekt_Educationboard/blob/f0250ac8361fecf064085da8ad1dc9779a7f3361/Programme/Baustein_%26_Test_Prg/Return_to_Menu_Button.py
) einfügen dabei kann ein belibiger Button gewählt werden, im BausteinCode ist der definierte Button vom Rotery Encoder. 

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e09c8307-8410-4275-b465-ed2b0e1fe973)


In dieser Abbildung ist zu erkennen, dass in Zeile 3 **'Pin'** die Bibliothek **'machine'** importiert wird und in Zeile 7 die Bibliothek **'sys'** hinzugefügt wird. In Zeile 11 wird der Knopf definiert, mit dem wir zum Menü zurückkehren, mit dem Befehl: **'button_pin = Pin(9, Pin.IN, Pin.PULL_UP)'**. Von Zeile 18 bis 32 definieren wir eine Funktion namens **'button_pressed'**, die das laufende Programm unterbricht und das Menüprogramm **'main.py'** startet.

Nach dem Kompilieren sollte das Programm erneut getestet werden, und dabei sollten entstandene Fehler korrigiert werden, wie zum Beispiel das Hinzufügen der vergessenen Bibliothek **'sys'**. Wenn alles funktioniert, wird in unserem Fall das Menüprogramm gestartet, wenn der Knopf bzw. Button des Rotary Encoders gedrückt wird.


## 2.3 Programm auf Raspberry Speichern
Wie in der [Dokumentation.md](https://github.com/Schledi777/Projekt_Educationboard/blob/0e447e8d7ff2c907a0dd9716c9d91fd424211b08/Dokumentation.md) erwähnt werden die Schritte 7. & 8. getätigt:

1. Um Programme auf den Pi zu speichern, sollten Sie das aktuelle Programm geöffnet haben. Dann gehen Sie zur Registerkarte **'Datei'** und wählen **'Speichern unter...'** aus. Es öffnet sich ein weiteres Menü, in dem Sie zwischen Computer und Raspberry Pi wählen können. Klicken Sie auf **'Raspberry Pi Pico'**, und es öffnet sich das Laufwerk des Pico's. Dort können Sie dann das Programm speichern.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/c90597f6-1f10-41f3-83e9-54ec1b6c77ba)
   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/f4fce567-db69-4507-a5c5-a597cba172cb)



2. Programm mit seinem Wunschnamen und der Endung'.py' benennen z.Bsp.: **Temp&Lft.py** und mit dem auswählen von 'OK' wird das Programm gespeichert

   ![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/3506fc69-14a1-4c40-a98a-c133b997ce44)


## 2.4 Programm im Menu Testen
Nun wird getestet ob das Programm auf dem Raspberry Pi Pico funktioniert, dabei wird mit dem Rotery Encoder das Programm **Temp&Lft.py** ausgewählt und mit dem eindrücken des Encoders gestartet.

   ![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/411476dc-f5dc-4478-af1d-27636dcca7c3)
   ![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e0e80df9-71fe-4305-bc10-b21786a1ecb9)

Wenn das Programm läuft wird wieder der Button/Knopf des Rotery Encoders eingedrückt und somit erscheint wieder das Menu.

   ![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/34ea6314-d324-46ab-baae-aa15a3199ca6)


---

# 3. Anleitung Intgration OLED zu einem Programm
Das EducationBoard verwendet einen **OLED Display I2C SSH1106 128 x 64 Pixel**.

## 3.1 Bibliothek für OLED hinzufügen
Sollte auf dem Pi Pico die Bibliothek sh1106.py NICHT unter dem Ordner lib im Pi zufinden sein, wird diese wie folgt hinzugefügt.
Zuerst wird die Bibliothek aus dem Ordner Lib aus dem Ordner Programme ['sh1106.py'](https://github.com/Schledi777/Projekt_Educationboard/blob/98594aedf2d1238a6d3b70266d346a011cbef856/Programme/Lib/sh1106.py) rauskopiert und im Raspberry Pi Pico im Ordner Lib mit dem Namen **'sh1106.py'** gespeichert werde.


## 3.2 Erklärung Syntax der Bibliothek
Der Beispiel Baustein ['OLED_Test_Baustein.py'](https://github.com/Schledi777/Projekt_Educationboard/blob/d16e9fedaf6b2823e0aaa90fe9d6515f0642ee1b/Programme/Baustein_%26_Test_Prg/OLED_Test_Baustein.py) wird zur Erklärung der Syntax genutzt.
Um den OLED nutzen zu können, muss man wie in Zeile 3 von der Bibliothek '**machine**' I2C und Pin importieren, in Zeile 4 wird aus der Bibliothek '**sh1106**' SH1106_I2C hinzugefügt und in Zeile 5 wird die Biliothek '**time**'.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/ed0f9c36-b3c6-46cc-8d80-4a84391f2662)

Als nächstes sollte aus Gründen der Übersichtlichkeit die Breite (128 Pixel) und Höhe (64 Pixel) als Variablen definiert werden. Dies wird in Zeile 7 für die Breite mit **'WIDTH = 128'** und in Zeile 8 für die Höhe mit **'HEIGHT = 64'** durchgeführt.

Danach werden die I2C-Eigenschaften wie folgt definiert: Die SCL/SCK- und SDA-Anschlüsse werden mit den entsprechenden Pins verbunden (SDA auf GPIO-Pin 6 und SCK auf GPIO-Pin 7). Diese Pins sind frei wählbar, müssen jedoch I2C-fähig sein und eine UART-Schnittstelle besitzen. Die Frequenz wird auf 400.000 Hz festgelegt. Dies wird mit dem Befehl **'i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)'** durchgeführt, um alle diese I2C-Eigenschaften zu definieren.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/a4377c25-61cc-4d1a-9a89-de23a9068af8)

Der Befehl in Zeile 12: '**display = SH1106_I2C(WIDTH, HEIGHT, i2c)**' erstellt ein Display-Objekt, das die angegebene Breite und Höhe hat und über die angegebene I2C-Verbindung kommuniziert.
Um die Display Anzeige um 180° zu drehen wird der Befehl aus Zeile 14 '**display.rotate(True)**' verwendet, wenn diese Funktion nicht gebraucht wird '*True*' durch '*False*' ersetzten.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/bf9d51a6-ee5c-4a3f-b7a6-a1b0a0ffd693)


Texte können mit dem Befehl '**display.text("*BeispielText*",x,y)**' hinzugefügt werden, x gibt an um wie viel Pixel die Textausgabe nach rechts verschoben wird und y um wie viele Pixel nach unten.
In diesem Beispiel haben wir 4 verschiede Texte(HTWK, TEST, TEST2, TEST3) mit verschiedenen Zeilen und Spalten angaben. 
Zum Anzeigen der Texte, wird wie in Zeile 22 der Befehl: '**display.show()**' genutzt. 

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/6f1199ba-b1db-4d52-9fa5-2b1326814d2e)
![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/17f0b795-5cdc-475b-8315-25820384f9ba)

Um die Texte dauerhaft zu aktualisieren, wird eine Dauerschleife mit '**while True:**' definiert Zeile 16. 
Danach soll nach jedem Durchlauf das Display 'sauber' bzw. Zurückgesetzt werden, dies geschieht durch den Befehl in Zeile 17: '**display.fill(0)**', da ansosten bei Text-Änderungen der Bildschirm 'verschmiert'.
Mit '**time.sleep(3)**' Zeile 23 wird angegeben nach wie vielen Sekunden, in unserem Fall 3 Sekunden, die Schleife wiederholt wird.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/1286dc94-b7fc-46b2-8463-3288bffd24a6)


## 3.3 Bsp. Implementierung für ein DHT11 Programm 
Dieses Beipiel orientiert sich am Programm: ['Temp&Lft.py'](https://github.com/Schledi777/Projekt_Educationboard/blob/65be3c3f6415bf3bf3732bba2f7c09c1fb358676/Programme/Temp%26Lft.py).
Im folgenden Bild an den RotenPunktMakierungen zuzuerkennen ist, wurden die im Punkt 3.2 genannten Bibliotheken in dieses Porgramm integiert.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/47278c8c-8ac6-4824-bdbd-78810b9a9a60)

Nun müssen die I2C-Eigenschaften des Displays definiert werden und es wird sich erneut an 3.2 orientiert wie an den RotenPunkt Makierungen im folgeneden Bild zuerkennen. 

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/4432970f-7975-4f20-a89e-f4c12e3f5a62)

Im folgenden Bild wird eine EndlosSchleife definiert, die den aktuellen Wert der Temperatur und Luftfeuchte ausgibt.
- Dabei löscht der Befehl: '***display.fill(0)***' den Bildschirm und bereitet neue Inhalte vor.

- Der Befehl: '***display.text("HTWK Leipzig",20,0)***' Schreibt den Text "HTWK Leipzig" als Titel, beginnend bei den Koordinaten (20, 0) auf dem Bildschirm.

- In Zeile 42 zeigt der Befehl: '***display.text("Temperatur: "+str(temp)+"C",0,28)***', den Temperaturwert ( der in der Variablen temp gespeichert ist) gefolgt von "C" für Celsius an. Der Text ist an den Koordinaten (0, 28) auf dem Bildschirm positioniert, da ein String verwendet wird muss die 'Abtrennung' der Wörter mit eine '**+**' erfolgen und **nicht** mit einem '**,**'.
- In Zeile 43 zeigt der Befehl:'***display.text("Luftfeuchte: "+str(hum)+"%",0,42)***'den Luftfeuchtigkeitswert (der in der Variablen hum gespeichert ist) gefolgt von "%" für Prozent an. Der Text ist an den Koordinaten (0, 42) auf dem Bildschirm positioniert.

- Danach pausiert '***time.sleep(1)***' die Ausführung des Programms für 1 Sekunde, um eine Verzögerung vor der Aktualisierung des Bildschirms zu erzeugen.

- '***display.show()***' zeigt den Text auf dem Display an.

![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/eb89dd13-17eb-45c1-a97b-e1d4f9dcf81b)
![image](https://github.com/Schledi777/Projekt_Educationboard/assets/130638123/e0e80df9-71fe-4305-bc10-b21786a1ecb9)
