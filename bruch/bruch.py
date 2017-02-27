"""

.. moduleauthor:: Patrick Kocsis <pkocsis@student.tgm.ac.at>

"""
from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """
    Bruch

    :param int zaehler: numerator
    :param int nenner: denominator
    :ivar int zaehler: numerator
    :ivar int nenner: denominator
    """

    def __iter__(self):
        """
        Ermöglicht die iterration der Bruch klasse

        :return: zaehler und nenner
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        """
        Der Konstruktor, hier kann ein Bruch erstelt werden

        :param zaehler: Ein (Bruch) oder (int)
        :param int nenner: nicht null
        :raises TypeError: incompatible types
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:' + type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:' + type(nenner).__name__)
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):
        """
        Überschreibt die float() Funktion

        :return: Der Bruch als Kommazahl dargestellt
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        Überschreibt die int() Funktion

        :return: Der float() Wert als int() grundet
        """
        return int(self.__float__())

    def __neg__(self):
        """
        Den Bruch negieren

        :return: negierter Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):
        """
        Erhalte die Rechte Seite des Bruches

        :raise TypeError: Wenn der Zähler kein int() oder float()
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self, zaehler):
        """
        Zuerst wird auf gleichen Nenner gebracht (mit Nenner multiplizieren)
        Zähler = z2 * self.nenner + n2 * self.zaehler


        :raise TypeError: Wenn zaehler kein Bruch ist
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' + Bruch()')
        nennerNeu = self.nenner * n2
        zaehlerNeu = z2 * self.nenner + n2 * self.zaehler
        return Bruch(zaehlerNeu, nennerNeu)

    def __complex__(self):
        """
        Überschreibt die complex(funktion)

        :return: complex(float(self))
        """
        return complex(self.__float__())

    def __rsub__(self, left):
        """
        Zähler = left * self.nenner - self.zaehler

        :raise TypeError: inkompatible typen
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' - Bruch()')

    def __sub__(self, zaehler):
        """
        Zähler anpassen -> self.__add__(zaehler * -1)

        :raise TypeError: inkompatible typen
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):
        """
        right version of mul

        :raise TypeError: inkompatible typen
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)

    def __mul__(self, zaehler):
        """
        Zwei Brüche multiplizieren

        :raise TypeError: inkompatible typen
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' * Bruch()')
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __pow__(self, p):
        """
        Mit einer Zahl den Bruch pontenzieren

        :raise TypeError: inkompatible typen
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('incompatible types:' + type(p).__name__ + ' should be an int')

    def __rtruediv__(self, left):
        """
        Division rechte seite

        :raise TypeError: inkompatible typen
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' / Bruch()')

    def __truediv__(self, zaehler):
        """
        Division

        :raise TypeError: incompatible types
        :param zaehler: Bruch oder int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' / Bruch()')
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __invert__(self):
        """
        Kehrwert

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):
        """
        Representation des Bruches für Entwickler

        :return str: the representation
        """
        # Vor der Ausgabe wird gekuerzt!
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        # Nenner stehts positiv
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    @staticmethod
    def __makeBruch(other):
        """
        Bruch statisch Erzeugen

        :raise TypeError: falscher Datentyp
        :param other: Bruch oder int
        :return: Bruch
        """
        '''create a Bruch from int or return the reference'''
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(other).__name__ + ' not an int nor a Bruch')

    def __eq__(self, other):
        """
        Zwei Brüche vergleichen

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner
    
    def __ne__(self, other):
        """
        not equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        return not self.__eq__(other)
    
    def __gt__(self, other):
        """
        greather than

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner
    
    def __lt__(self, other):
        """
        lower than

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner
    
    def __ge__(self, other):
        """
        greather or equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner
    
    def __le__(self, other):
        """
        lower or equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner
    
    def __abs__(self):
        """
        abs(Bruch)

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))
    
    def __iadd__(self, other):
        """
        intern add

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self
    
    def __isub__(self, other):
        """
        intern sub

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self
    
    def __imul__(self, other):
        """
        intern mul

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self * other
        return self

    def __idiv__(self, other):
        """
        intern division 2.x

        :param Bruch other: other Bruch
        :return: self
        """
        return self.__itruediv__(other)

    def __itruediv__(self, other):
        """
        intern division 3.x

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self

    @classmethod
    def gcd(cls, x, y):
        """
        Berechnung vom Größten gemeinsamen Teiler

        :param int x: erster Wert
        :param int y: zweiter Wert
        :return: Größter gemeinsamer Teiler
        """
        x, y = abs(x), abs(y)
        if x < y: x, y = y, x
        while y != 0:
            x, y = y, x % y
        return x
