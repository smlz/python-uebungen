# Auftrag Altersberechnung

Schreibe ein Program welches das Alter (in Jahren) einer Person abfragt, und daraus die folgenden Werte berechnet und ausgibt:

 - Das (ungefähre) Alter in Tagen
 - Das (ungefähre) Alter in Stunden
 - _freiwillig_: Das ungefähre Alter in Minuten
 - _freiwillig_: Das ungefähre Alter in Sekunden

Erstellt dazu zuerst eine neue Datei mit dem Namen `alter.py`.

### Beispiel für einen Programmaufruf

Wenn das Programm aufgerufen wird, könnte das beispielsweise so aussehen (Benutzereingaben sind fett geschrieben): 

---
Hallo und Wilkommen zum Altersberechungstool!

Wie alt bist du? **18**

Also wenn ich das richtig verstehe, ist dein Alter in Tagen zirka:

6570

und in Studen wären das:

157680

Vielen Dank und auf Wiedersehen

---

Falls du Schwierigkeiten haben solltes, findest du in der Datei [`vorlage_alter.py`](vorlage_alter.py) eine Vorlage, welche eine grobe Struktur des Programms skizziert.

## Freiwilliger Zusatzauftrag

Das Ganze ist noch recht ungenau, da wir das genaue Geburtsdatum und auch welcher Tag heute ist, einfach ignorieren.

Das Geburtsdatum können wir abfrage, zum Beispiel so:

---
Hallo und Wilkommen zum Altersberechungstool!

In welchem Jahr bist du geboren? **2002**

In welchem Monat bist du geboren (in Zahlen)? **5**

An welchem Tag im Monat bist du geboren? **7**

Also wenn ich das richtig verstehe, ist dein Alter in Tagen zirka:

...

---

Beim heutigen Datum hilft uns Python:
```python
from datetime import date

heute = date.today()

print(heute.year)
print(heute.month)
print(heute.day)
```

_Tipp_: Berechne zuerst die Anzahl Tage im aktuellen Kalenderjahr und die Anzahl Tage im Geburtsjahr, und danach erst die Anzahl Tage für die Jahre dazwischen. Addiere am Schluss die drei Werte für die berechneten Tage zusammen.

Ignoriere dabei, dass Schaltjahre einen Tag mehr haben, und rechne zur Vereinfachung für die Monate immer mit 30 Tagen. Das Resultat ist zwar immer noch nicht perfekt, aber kommt der Realität schon bedeutend näher.

Wir sehen, Datumsberechnungen sind erstaunlich kompliziert. Und auch selbst wenn man die richtige Anzahl Tage pro Monat sowie auch die Schaltjahre korrekt berücksichtigt, ist das Resultat immer noch nicht zu hundert Prozent korrekt: [Stichwort Schaltsekunde](https://en.wikipedia.org/Leap_seconds).
