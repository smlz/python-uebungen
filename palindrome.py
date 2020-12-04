def palindrome(word):
    """Checks if a word is a palindrome.

    >>> palindrome("")
    True
    >>> palindrome("a")
    True
    >>> palindrome("anna")
    True
    >>> palindrome("hans")
    False
    >>> palindrome("alberta")
    False
    >>> palindrome("wasitacatisaw")
    True
    """
    # FIXME: Triviale Fälle: Worte mit keinem oder einem Buchstaben sind immer Palindrom.
    # Wir können also hier an dieser Stelle die definitive Antwort geben.


    
    # FIXME: Wenn die äussersten beiden Buchstaben nicht übereinstimmen, ist das Wort ganz
    # sicher kein Palindrom.
    # Wir können also hier an dieser Stelle die definitive Antwort geben.

    # Tipp: Erster Buchstabe word[0], letzter Buchstabe word[-1]

    # FIXME: Das Wort ist weder garantiert ein Palindrom (weil kurz), noch garantiert kein Palindrom
    # (weil Enden nicht übereinstimmen). Was ist mit der Mitte des Wortes?

    # Tipp: Mitte ausschneiden word[1:-1]

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)