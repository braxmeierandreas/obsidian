# Anleitung

## **Inhaltsverzeichnis**

**1.** **Was ist ein digitales Zertifikat und wozu benötige ich es?** .................................... 2

**2.** **Was benötige ich im Einzelnen?** ........................................................................... 2

**3.** **Wie erhalte ich ein Zertifikat?** .............................................................................. 2

**4.** **Wie importiere ich mein persönliches Zertifikat?** ................................................ 3

4.1 Mozilla Firefox ...................................................................................................................... 3

4.2 Internet Explorer .................................................................................................................. 6

4.3 Google Chrome ..................................................................................................................... 8

**5.** **Exportieren des öffentlichen Teils des Zertifikats** ................................................ 9

**Mozilla Firefox (Version 70.X oder aktueller)** ................................................................................ 9

**6.** **Zertifikat hochladen** .......................................................................................... 10

**7.** **Zertifikat erneuern** ............................................................................................ 11

**8.** **Liste von Zertifikatsausstellern, deren Client-Zertifikate bereits erfolgreich**
**getestet wurden** ........................................................................................................ 12

**9.** **Anhang: Allgemeine Liste von Ausstellern der Zertifikate** ................................. 13


**1.** **Was ist ein digitales Zertifikat und wozu benötige ich es?**


Ein Zertifikat ist eine Art elektronischer „Ausweis“. Verschlüsselungssysteme nutzen dieses Zertifikat zum
Nachweis der Identität. Es enthält zwei Teile, Ihren Private Key und den zugehörigen Public Key. Das
Zertifikat wird bei Anwendungen mit hohem Schutzbedarf zur 2-Faktor-Authentifizierung
(Usercode/Passwort und Zertifikat) genutzt, um sich als berechtigte Person zu authentifizieren. Gemäß dem
Reifegradmodell des Onlinezugangsgesetzes (OZG) muss eine Authentifizierung mit einem dem jeweils
erforderlichen Vertrauensniveau angepassten Mittel möglich sein. Für die Registrierung/Erstidentifizierung
wird für alle Vertrauensniveaus ein elektronischer Identitätsnachweis gefordert. Daher ist es für die Nutzung
des DiGA-/DiPA-Antragsportals erforderlich, einmalig eine Identifizierung mit einem Zertifikat
durchzuführen. Nach Ablauf des Zertifikats ist zudem eine erneute Identifizierung erforderlich.


Nutzende, die kein Zertifikat besitzen, sich also nicht „ausweisen“ können, erhalten keinen Zugriff auf den
Bereich der Antragsstellung und Bearbeitung.


Das Zertifikat für den Zugang zu dem DiGA-/DiPA-Antragsportals können Sie bei einer Zertifizierungsstelle
(Certificate Authortiy – CA) oder bei einem Distributor erwerben. Es kann auch für andere Zwecke genutzt
werden.


Bei dem nötigen Zertifikat handelt es sich um ein S/MIME-Zertifikat mit der Zertifikatserweiterung „Client
Authentication“. Das Zertifikat muss einen Organisationsnamen enthalten, d. h. der Zertifizierungsstufe
„Organization-Validated“ oder „Sponsor-Validated“ entsprechen. Eine Liste mit möglichen Ausstellern
finden Sie im Anhang.


**2.** **Was benötige ich im Einzelnen?**


Um ein Zertifikat zu erhalten und es für den Zugang zum DiGA-/DiPA-Antragsportals zu nutzen, sind die
folgenden drei Schritte notwendig:

  - Beantragen Sie ein Zertifikat bei einer Zertifizierungsstelle oder einem Distributor. Es muss für
eine TLS-WWW-Client-Authentifizierung ausgestellt und SHA-2 signiert sein.
[(Extended-Key-Usage für Client-Authentifizierung, siehe http://www.ietf.org/rfc/rfc3280.txt,](http://www.ietf.org/rfc/rfc3280.txt)
Abschnitt 4.2.1.13).


  - Holen Sie das für Sie ausgestellte Zertifikat ab und importieren Sie es in Ihren Browser.


  - Sichern Sie Ihr Zertifikat


**3.** **Wie erhalte ich ein Zertifikat?**


Das Zertifikat beantragen Sie bei einer Zertifizierungsstelle oder einem Distributor. Angeben müssen Sie
dabei üblicherweise Ihren Namen, Ihre Adresse, Ihre E-Mail-Adresse, das Land aus dem Sie kommen, und
eventuell einen Firmennamen oder ein Bundesland. Wie genau der Antrag erfolgt, erfahren Sie beim
jeweiligen Anbieter. Den privaten Schlüssel (Private Key) sollten Sie gut aufbewahren. Zusätzlich müssen Sie
sich noch identifizieren (z. B. Postident). Der Aussteller stellt Formulare für die Beantragung und
Beschreibungen für das Eintragen des Zertifikats in den Browser zur Verfügung.


Die Beantragung und Abholung eines Zertifikats kann recht unterschiedlich sein. Der übliche Weg ist, die
Webseite des Anbieters zu besuchen und dort Ihre Daten einzugeben. Dabei erstellt der Browser auf Ihrem
Computer den Private Key und den Public Key.


Der Public Key wird an den Anbieter gesendet und dort signiert, während der Private Key in Ihrem Browser
verbleibt. In den meisten Fällen werden Sie anschließend per E-Mail aufgefordert, die Webseite erneut mit
dem gleichen Browser zu besuchen. Dabei wird der signierte Public Key mit dem Private Key
zusammengeführt und letztendlich das Zertifikat erstellt. Zugleich wird das Zertifikat auch in Ihrem
Browser installiert. In diesem Fall sollten Sie Ihr Zertifikat im Anschluss unbedingt sichern.


Eine weitere Variante wird in Kapitel 4 beschrieben. Dabei erhalten Sie das fertige Zertifikat entweder vom
Aussteller oder von einer Kollegin oder einem Kollegen Ihrer IT, die oder der es für Sie beantragt hat.


**4.** **Wie importiere ich mein persönliches Zertifikat?**


Wenn Sie Ihr Zertifikat erhalten haben, muss es in den Browser importiert werden, bevor Sie es verwenden
können. Durch den Import wird das Zertifikat im richtigen Zertifikatsspeicher platziert.


Im Folgenden wird das Importieren beispielhaft für den Browser Mozilla Firefox, dann für den Internet
Explorer und abschließend für Google Chrome durchgeführt:

4.1 Mozilla Firefox


Wählen Sie zuerst im Menü am rechten oberen Bildrand den Punkt „Einstellungen“ aus.


**Abbildung 1: Einstellungen Erweitert**


Wählen Sie nun „Datenschutz & Sicherheit“ aus und scrollen Sie hinunter bis der Menüpunkt „Zertifikate“
erscheint.


**Abbildung 2: Übersicht Zertifikate**


Wählen Sie „Zertifikate anzeigen“: Es öffnet sich ein weiteres Fenster, in dem Sie den Reiter „Ihre
Zertifikate“ wählen. Sie sehen nun eine Übersicht der bereits installierten Zertifikate (im Beispiel sind
keine Zertifikate vorhanden).


**Abbildung 3: Zertifikatsverwaltung**


Nach Klick auf „Importieren“ erscheint eine Datenauswahlbox.


**Abbildung 4: Importieren des Zertifikats**


Wählen Sie Ihr Zertifikat aus und klicken Sie auf „Öffnen“. Sie werden nun aufgefordert, das Passwort für
die Schlüsseldatei einzugeben.


**Abbildung 5: Passwort des Zertifikats**


Nach erfolgreichem Import des Zertifikats ist es unter „Ihre Zertifikate“ eingetragen.


**Abbildung 6: Übersicht mit hochgeladenem Zertifikat**


4.2 Internet Explorer


Hier wählen Sie im Menu „Extras“ den Punkt „Internetoptionen“.


**Abbildung 7: Öffnen der Internetoptionen**


Dann wählen Sie den Reiter Inhalte aus und klicken auf den Knopf „Zertifikate“.


**Abbildung 8: Aufruf Zertifikate**


Sie sehen unter „Eigene Zertifikate“ eine Übersicht der bereits installierten Zertifikate. Nach Klick auf
„Importieren“ erscheint der Zertifikatsimport-Assistent. Bei der ersten Ansicht klicken Sie auf „Weiter“. In
der folgenden Ansicht wählen Sie das Zertifikat aus, bestätigen mit „Weiter“ und geben Ihr Passwort ein.


Nun erscheint die Auswahl des Zertifikatspeichers. Die Einstellungen sollten den unten angezeigten
Einstellungen entsprechen.


**Abbildung 9: Auswahl des Zertifikatspeichers**


Klicken Sie nun auf „Weiter“ und bestätigen Sie die folgende Ansicht mit „Fertig stellen“.


Ihr Zertifikat sollte nun unter der Ansicht „Eigene Zertifikate“ angezeigt werden.


4.3 Google Chrome


Wählen Sie unter „Google Chrome anpassen und einstellen“ den Punkt „Einstellungen“ aus.


**Abbildung 10: Einstellungen öffnen**


Wählen Sie nun „Datenschutz und Sicherheit“ aus und klicken Sie auf „Mehr“.


Es öffnen sich nun weitere Auswahlmöglichkeiten. Hier klicken Sie bitte auf den untersten Punkt
„Zertifikate verwalten“.


**Abbildung 11: Zertifikate verwalten auswählen**


Sie sehen unter „Eigene Zertifikate“ eine Übersicht der bereits installierten Zertifikate. Nach Klick auf
„Importieren“ erscheint der Zertifikatsimport-Assistent. Bei der ersten Ansicht klicken Sie auf „Weiter“. In
der folgenden Ansicht wählen Sie das Zertifikat aus, bestätigen mit „Weiter“ und geben Ihr Passwort ein.


Nun erscheint die Auswahl des Zertifikatspeichers. Die Einstellungen sollten den unten angezeigten
Einstellungen entsprechen.


**Abbildung 12: Auswahl des Zertifikatspeichers**


Klicken Sie nun auf „Weiter“ und bestätigen Sie die folgende Ansicht mit „Fertig stellen“.


Ihr Zertifikat sollte nun unter der Ansicht „Eigene Zertifikate“ angezeigt werden.


**5.** **Exportieren des öffentlichen Teils des Zertifikats**


**Mozilla Firefox (Version 70.X oder aktueller)**


Um den öffentlichen Teil des Zertifikats für die Registrierung beim BfArM hochzuladen, extrahieren Sie
diesen Teil Ihres Zertifikats. Hierzu öffnen Sie, wie in Abschnitt 4 beschrieben, den Zertifikatmanager,
markieren unter „Meine Zertifikate“ das gewünschte Zertifikat und klicken dann auf „Ansehen…“.


**Abbildung 13: Exportieren des Zertifikats**


Scrollen Sie dann hinunter bis Sie „Speichern“ sehen und klicken Sie auf „PEM (Zertifikat)“.


Speichern Sie das Zertifikat lokal und sehen in Ihrem Download-Ordner (falls nicht anders angegeben)
nach, ob das Zertifikat heruntergeladen wurde.


Wiederholen Sie diesen Schritt durch Klick auf „PEM (Zertifikatskette)“.


**Abbildung 14: Extrahieren des öffentlichen Teils**


**6.** **Zertifikat hochladen**


Nach der Erstregistrierung sowie nach dem Einloggen in das DiGA-/DiPA-Antragsportal gelangen Sie auf
den Reiter „Mein Konto“. Hier können Sie unter „Client-Zertifikat“ den öffentlichen Schlüssel Ihres
Zertifikats als CRT-, DER- oder PEM-Datei hochladen, in dem Sie auf die Schaltfläche „Datei hochladen“
klicken. Laden Sie anschließend auch die Zertifikatskette unter „CA-Zertifikat“ hoch.


Hinweis: Das CA-Zertifikat / die Zertifikatskette kann normalerweise auch direkt beim Zertifikatsanbieter
heruntergeladen oder von diesem angefordert werden. Dieses ist unabhängig vom tatsächlichen Zertifikat
des Nutzenden.


Mit Klick auf die Schaltfläche „Client-Authentifizierung durchführen“ kann die Client-Authentifizierung
dann vorgenommen werden (siehe Abbildung 22).


**Abbildung 22: Durchführung der Client-Authentifizierung**


In dem erscheinenden Fenster muss hierfür das eigene Zertifikat ausgewählt werden. Dabei wird das
Zertifikat verifiziert und sichergestellt, dass im Browser der passende private Schlüssel zum Zertifikat
installiert ist. Wenn die Authentifizierung erfolgreich war, werden unter „Zertifikats-Status“ alle Angaben
mit „Ja“ beantwortet (siehe Abbildung 23).


**Abbildung 23: Durchführung der Client-Authentifizierung**


**7.** **Zertifikat erneuern**


Nach Ablauf des Zertifikats muss ein neues Zertifikat im Antragportal hochgeladen werden. Hierbei sind
grundsätzlich die zuvor beschriebenen Schritte erneut zu befolgen. Damit keine Komplikationen mit dem
„alten“ Zertifikat entstehen, sollten im Webbrowser unter „Zertifikatverwaltung“ die „AuthentisierungsEntscheidungen“ vor Einrichtung des neuen Zertifikats gelöscht werden (siehe Abbildung 24 am Beispiel
des Browsers Firefox).


**Abbildung 24: Authentisierungs-Entscheidungen**


**8.** **Liste von Zertifikatsausstellern, deren Client-Zertifikate bereits erfolgreich**

**getestet wurden**


Im Folgenden sind zur Unterstützung Zertifikatsaussteller aufgelistet, deren Client-Zertifikate bereits
erfolgreich im Antragsportal verwendet werden. Die Auflistung ist allerdings keinesfalls als Verweis oder
Empfehlung zum Kauf der Produkte eines bestimmten Unternehmens zu verstehen.


Asseco Data Systems S.A.: Certum SMIME RSA CA


Deutsche Telekom Security GmbH: Telekom Security BusinessID SMIME CA 2023


DigiCert Inc: DigiCert Assured ID Client CA G2


DigiCert, Inc.: DigiCert Assured G2 SMIME RSA4096 SHA384 2024 CA1


FNMT-RCM: AC Representación


GEANT Vereniging: GEANT Personal CA 4


GlobalSign nv-sa: GlobalSign GCC R6 SMIME CA 2023


Sectigo Limited: Sectigo RSA Client Authentication and Secure Email CA


SSL Corp: SSL.com Client Certificate Intermediate CA RSA R2


SwissSign AG: SwissSign RSA SMIME SV ICA 2024 - 1


SwissSign AG: SwissSign RSA TLS OV ICA 2022 - 1


Verein zur Foerderung eines Deutschen Forschungsnetzes e. V.: DFN-Verein Global Issuing CA


**9.** **Anhang: Allgemeine Liste von Ausstellern der Zertifikate**


Im Folgenden sind einige Zertifizierungsstellen aufgelistet, die generell digitale X.509-User-Zertifikate
ausstellen (Stand März 2020). Die Reihenfolge der aufgeführten Liste ist keinesfalls als Verweis oder
Empfehlung zum Kauf der Produkte eines bestimmten Unternehmens zu verstehen.


GlobalSign nv-sa, BE


SwissSign AG, CH


DigiCert Inc, US


COMODO CA Limited, GB


AC Camerfirma SA CIF A82743287, EU


Buypass AS-983163327, NO


QuoVadis Limited, BM


Starfield Technologies, Inc., US


Thawte, ZA


thawte, Inc., US


T-Systems Enterprise Services GmbH, DE


VeriSign, Inc., US


The USERTRUST Network, US


GeoTrust Inc., US


AffirmTrust, US


AddTrust AB, SE


Actalis S.p.A./03358520967, IT


CyberTrust Root, Baltimore, IE


Entrust, Inc., US


SECOM Trust.net, JP


SECOM Trust Systems CO.,LTD., JP


Internet Security Research Group, US


IdenTrust, US


GoDaddy.com, Inc., US


The Go Daddy Group, Inc., US


Sonera, FI


Thawte Consulting cc, ZA


XRamp Security Services Inc, US


SecureTrust Corporation, US"


LuxTrust s.a., LU


KEYNECTIS, FR


AC Camerfirma S.A., EU


Unizeto Sp. z o.o., PL


Unizeto Technologies S.A., PL


Chunghwa Telecom Co., Ltd., TW


Hinweis: Nicht alle Anbieter stellen X.509-Zertifikate mit der Erweiterung „Extended Key Usage: Client
Authentication" aus. Das Zertifikat muss zudem einen Organisationsnamen enthalten, d. h. der
Zertifizierungsstufe „Organization-Validated“ oder „Sponsor-Validated“ entsprechen.


Datenschutzrechtliche Hinweise zur Verarbeitung Ihrer personenbezogenen Daten und zu Ihren Rechten
finden Sie unter: [Datenschutz](https://www.bfarm.de/DE/Service/Datenschutz/_node.html)


