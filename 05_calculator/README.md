# Auftrag RPN-Rechner

Mit diesem Auftrag kreieren wir ein Programm, welches Rechnungen löst. Die Rechnungen geben wir als Strings ein, und erhalten am Schluss (hoffentlich) eine Zahl.

Die Rechnungen schreiben wir dabei nicht wie gewohnt auf, sondern im RPN-Format. Anstatt dass das Operationszeichen zwischen die beiden Operanden (Zahlen) gesetzt wird, schreiben wir es _nach_ den Operanden.

Beispiele:
* Aus `1 + 1` wird `1 1 +`
* Aus `2 * 3` wird `2 3 *`
* Aus `8 / 2` wird `8 2 /`
* Aus `1 + 2 - 3` wird `1 2 + 3 -`
* Aus `(2 + 3) * 5` wird `2 3 + 5 *`
* Aus `2 + 3 * 5` wird `2 3 5 * +`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(_Achtung_: Punkt vor Strich)

Das RPN-Format hat zwar den Nachteil, dass es im ersten Moment nicht sehr leserlich ist, aber auch einige wichtige Vorteile:
1. Es braucht keine Klammern.
2. Es brauch keine Regeln wie _Punkt-vor-Strich_, da die Operationen streng von links nach rechts ausgeführt werden.
3. Das Format lässt sich (wie wir sehen werden) relativ einfach in einem Programm verarbeiten.


## Vorbereitungsaufgaben

1. Schreib deine Lieblingszahl auf.
2. Kreiere eine einfache Rechnung mit deiner Lieblingszahl als Resultat.
3. Wandle die Rechnung in das RPN-Format um.
4. Kreiere eine möglichst komplizierte Rechnung mit deiner Lieblingszahl als Resultat.
5. Wandle auch diese Rechnung ins RPN-Format um.

## RPN-Algorithmus

Wie lässt sich jetzt das Resultat von so einer Rechnung berechnen?

__Vorbereitung__: Halte ein Stift und ein Blatt Papier bereit.

__Algorithmus:__
 - Gehe deine Rechnung Schritt-für-Schritt von links nach rechts durch:
    * Du triffst auf eine Zahl: Notiere sie auf deinem Blatt
    * Du triffst auf ein Operationszeichen:
      * Merke dir die letzten beiden Zahlen, welche du auf dein Blatt geschrieben hast.
      * Streiche die beiden Zahlen durch.
      * Schreibe das Resultat der Rechnug mit den gemerkten Zahlen auf das Blatt.

__Ende:__ Wenn du am Ende deiner Rechnung angelangt bist, sollte nur noch eine Zahl auf deinem Blatt stehen: Das Resultat der Rechnung!

__Aufgabe:__ Überprüfe den Algorithmus mit Stift und Papier mit deinen beiden Rechnungen.

## Umsetzung

1. Lade die Datei `calculator.py` herunte, öffene sie, und führe sie aus. Du solltest eine Fehlermeldung sehen:

```
...
**********************************************************************
1 items had failures:
   3 of   3 in __main__.calc
***Test Failed*** 3 failures.
```

2. Lies den Code der Funktion `calc` einmal ganz durch. Insbesondere die Kommentare welche mit `FIXME` beginnen.

3. Füge bei den Kommentaren `FIXME 1` deinen Code ein. Wenn du jetzt das Programm ausführst, sollten nur noch zwei Fehler auftauchen. Du kannst jetzt triviale Rechnungen ausführen:

```python
>>> calc("42")
42
```
4. Füge bei `FIXME 2` den Code ein, um eine Addition durchzuführen. Jetzt sollte nur noch _ein_ Fehler beim Ausführen angezeigt werden. Du kannst ab sofort addieren:
```python
>>> calc("1 1 +")
2
>>> calc("1 2 + 3 + 4 +")
10
```

5. Erweitere die `calc`-Funktion, so dass sie auch Subtraktionen und Multiplikationen korrekt berechnen kann (`FIXME 3`). Achtung: Zeile 4 nicht vergessen. Jetzt sollten beim Ausführen keine Fehlermeldungen mehr erscheinen.
```python
>>> calc("4 1 - 3 *")
9
```

6. Lies deinen Code. Siehst du mehrmals ähnlichen oder sogar identischen Code? Gibt es eine Möglichkeit, diese Wiederholungen zu vermeiden. Vereinfache deinen Code falls möglich.

7. Erweitere die `calc`-Funktion so, dass sie deine Rechnungen berechnen kann.

8. Schreiben den Code um mit einer möglichen Benutzerin deines Programmes zu interagieren. So könnt eine Aufruf zum Beispiel aussehen:

    > Guten Tag zum Rechner. Bitte gib mir eine Rechnung (X um zu beenden).
    > \> __1 1 +__
    > 2
    > \> __2 3 *__
    > 6
    > \> __4 1 - 3 *__
    > 9
    > \> x
    > Auf wiedersehen!
