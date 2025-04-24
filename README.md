# Parkingslicens CAS AAU
 Automatisering af parkering på CAS AAU

Der findes to versioner:

Multiple:
Denne henter et CSV dokument med telefonnumre og registreringsnumre og udfylder alle disse.
Opsæt et cronjob til at køre scriptet på et givent tidspunkt og det vil udfylde parkering for alle.
Husk at sætte det til kun hverdage.
Den laver en logfil med resultaterne af kørslen.

Single:
Udfyldes med telefonnummer og registringsnummer i scriptet.
Opsæt et cronjob til at køre scriptet på et givent tidspunkt og det vil udfylde parkering for kun det der står i scriptet.
Husk at sætte det til kun hverdage.


Installer requirements med 
pip install -r requirements.txt

Det er en nødvendighed at have følgende installeret på linux:
chromium-browser chromium-chromedriver

På PC burde det fungere så længe en chromium browser er installeret