
# Alle gültigen Operationen sind in dieser Liste hinterlegt.
# FIXME 3: Eigene Operationen hinzufügen
ops = ["+"]

def calc(string):
    """Eine Rechnung im RPN-Format evaluieren.

    Eine sehr einfache Rechnung:
    >>> calc("1")
    1
    
    Eine einfache Rechnung:
    >>> calc("1 1 +")             # 1 + 1
    2
    
    Eine etwas kompliziertere Rechnung:
    >>> calc("2 4 + 8 1 - * ")    # (2 + 4) * (8 - 1)
    42
    """

    # FIXME 1: Einen leere Liste für den Stapel erstellen. Gib ihr den Namen `stapel` oder `stack`.

    for element in string.split():
        if element in ops:
            if element == "+":
                # FIXME 2: Plus-Operation ausführen:
                # Zwei Zahlen vom Stapel nehmen (.pop()), zusammenrechnen, wieder am zurück auf den
                # Stapel legen (.append(...)).
                ...

            # FIXME 3: Weitere Operationen erfassen (Minus, ...).

            else:
                raise NotImplementedError("Operation nicht implementiert")
        else:
            # FIXME 1: Das aktuelle Element war keine Operation, darum nehmen wir an, es sei eine Zahl.
            # Element in eine Zahl umwandeln, und zuoberst auf den Stapel legen.
            ...


    # FIXME 1: Gib die oberste Zahl vom Stapel zurück.
    return ...



if __name__ == "__main__":
    import doctest
    doctest.testmod()
