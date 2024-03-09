# **Documentation zum Projekt Educationboard zur Lehrveranstaltung Embedded Systems**

## **1.Instalation Micropython auf Raspberry Pi Pico und Verbinen in der IDE**

### 1. Pico mit Computer Verbinden


Source:(https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/microcontrollers/micropython/drag-and-drop.adoc)

Mit einem DATENÜBERTRAGUNGSFÄHIGEN Micro-USB Kabel, während man den '**BOOTSEL button**' gedrückt hält, in einen USB-OUTLET seiner Wahl des PC's stöpseln.
Der '**BOOTSEL button**' kann nach dem Verbinden losgelassen werden. Nun müsste im Explorer unter '*Dieser PC*' bei '*Geräte und Laufwerke*' ein Laufwerk namens '**RPI-RP2**' vorhanden sein. 


### 2. Istallation von Mircro Python


Nun Link von Source folgen auf den **Raspberry Pi Pico** link klicken, wie in der folgenden Abildung.

![image](https://github.com/Schledi777/ebunoard/assets/130638123/e6dbd6cc-b67a-4749-8757-4c0188bad334)

Nachdem man auf den Link geklickt hat müsste stand 03.03.2024 eine Datei mit dem Namen: 'RPI_PICO-20240222-v1.22.2.uf2' heruntergeladen worden sein.
Nun die 'RPI_PICO-20240222-v1.22.2.uf2' - Datei in das Laufwerk '**RPI-RP2**' per drag and dorp reinziehen.
Wenn die Istallation erfolgreich war sollte nun das Laufwerk '**RPI-RP2**' nicht mehr zusehen sein.


### 3. Istallation IDE und Verbinden des Pi Pico's mit der IDE


#### 1. Thonny:

Herunterladen unter der IDE: https://thonny.org und dann Installieren.

Verbinden der IDE mit Pi Pico:
1. Raspberry Pi Pico in einen USB-OUTLET stecken
2. Thonny öffnen
3. In der Registerkarte oben links auf '**Ausführen**' klicken und dann auf '*Kofiguriere den Interperter...*'
   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/51ed80c2-cbc9-4096-a09a-7b5a4d67a074)

4. Wie im folgenden Bild die Art des Interpreters den '**MicroPython (Raspberry Pi Pico)**' auswählen und bei dem Port euren 'COM' - Anschluss. In meinem Fall ist es der '**COM3**' Anschluss über den ich die Codes und Biblioteken auf den Pico laden werde.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/4fe262bd-e212-4282-a591-b8ef2043bb0e)

5. Auf das Stopschild klicken um zu Connecten bzw. einen Softreboot starten oder das laufende Programm zu stoppen.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/8387de42-e4bb-436a-9c90-b63f8a294ce4)

6. Auf den grünen Run button klicken um das Pogramm über den Pi zu starten, wenn es einen Fehler gibt kommt eine Meldung in der Console.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/e59b8616-fa2c-4c8f-b61b-d08a6cb48c1d)

7. Um Programmen auf den Pi zu Speichern aktuelles Programm offen haben, dann unter Registerkarte '**Datei**' und dort dann '**Speichern unter...**' auswählen. Dann öffnet sich ein weiteres Menu, in welchen man zwischen Computer und Raspberry entscheiden kann. Dort auf '*Raspberry PI Pico*' klicken und es öffnet sich das Laufwerk des Pico's.

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/c90597f6-1f10-41f3-83e9-54ec1b6c77ba)
   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/f4fce567-db69-4507-a5c5-a597cba172cb)

9. Programm oder Bibliotek mit '.py' benennen und mit dem auswählen von 'OK' wird die Datei gespeichert

   ![image](https://github.com/Schledi777/ebunoard/assets/130638123/3cc35c2d-7460-4d19-adad-caaffc2c970e)


