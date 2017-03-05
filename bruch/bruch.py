# coding=UTF-8
class Bruch(object):
    """
    @:param given zaehler
    @:param given nenner
    @:var attribute zaehler
    @:var attribute nenner
    """

    def __init__(self, zaehler=0, nenner=1):
        """
        constructor which fills the "Bruch" with Zaehler and Nenner or a other given Bruch
        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :param nenner: int - not zero
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

    # ------------------------------Allgemein:
    def __float__(self):
        """
        Overwrites from Object
        returns the Result of a division as a Float
        :return: float result
        """
        return self.zaehler / self.nenner
    def __int__(self):
        """
        Overwrites from Object
        Returns the Result of a division as an Integer
        :return: integer Result
        """
        return int(self.__float__())
    def __complex__(self):
        """
        Overwrites from Object
        Returns the result of a division as a complex number
        :return: result as a complex number
        """
        return complex(self.__float__())
    def __invert__(self):
        """
        Overwrites from Object
        Returns the given Bruch with invertet arguments
        :return: inverted Bruch
        """
        return Bruch(self.nenner, self.zaehler)
    def __neg__(self):
        """
        Overwrites from Object
        negates the Bruch (*-1)
        :return: negated Bruch
        """
        return Bruch(-self.zaehler, self.nenner)
    def __abs__(self):
        """
        Overwrites from Object
        Returns the abs of a Bruch
        :return: abs
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))
    def __pow__(self, p):
        """
        Overwrites from Object
        Returns the Bruch to a given Power
        :param p: the Bruch is multiplied to that power
        :return:  the result
        """
        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('incompatible types:' + type(p).__name__ + ' should be an int')

 # ---------------------------------Vergleichsoperatoren:
    def __eq__(self, other):
        """
        Overwrites from Object
        Checks if two Bruch are equal to each other
        :param other: the Bruch to compare with
        :return: true if equal/ false if not
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner
# ----------------------------------------------------------------------
    def __ne__(self, other):
        """
        returns if two Bruch are not equal to each other
        :param other: the Bruch to compare with
        :return: true if not equal/false if not
        """
        return not self.__eq__(other)
# ----------------------------------------------------------------------
    def __gt__(self, other):
        """
        Checks if a Bruch is greater then another Bruch
        :param other: the other Bruch
        :return: true if greater/false if not
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner
# ----------------------------------------------------------------------
    def __lt__(self, other):
        """
        Checks if a Bruch is lower than another
        :param other: the other Bruch
        :return: true if lower/false if not
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner
# ----------------------------------------------------------------------
    def __ge__(self, other):
        """
        Compares if a Bruch is greater or equal to another Bruch
        :param other: the other Bruch
        :return: True if greater or equal / false if not
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner
# ----------------------------------------------------------------------
    def __le__(self, other):
        """
        Compares if a Bruch is lower or equal to another Bruch
        :param other: the other Bruch
        :return: True if lower or equal/ false if not
        """
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

#---------------------------Addition:
    def __add__(self,zaehler):
        """
        adds two Bruch's to each other
        :param zaehler: a int or another Bruch (if int a Bruch will be formed arg/1)
        :return: the new Bruch
        """
        if isinstance(zaehler, Bruch):
            for_z,for_n=zaehler
        elif type(zaehler) is int:
            for_z,for_n=zaehler,1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' + Bruch()')
        newNenner=self.nenner*for_n
        newZaehler=for_z*self.nenner+for_n*self.zaehler
        return Bruch(newZaehler,newNenner)
    def __radd__(self, zaehler):
        """
        Right Side addtion
        :param zaehler: int or Bruch
        :return: new Bruch
        """
        return self.__add__(zaehler)
    def __iadd__(self, other):
        """
        intern addtion
        :param other: Bruch or Int
        :return: new Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self

#--------------------------------Subtratktion
    def __sub__(self,zaehler):
        """
        Returns the result of a subtraktion of two Bruch's
        :param zaehler: the second bruch or int
        :return: result
        """
        return self.__add__(zaehler*-1)
    def __isub__(self, other):
        """
        internal subtraktion
        :param other: Bruch or Int
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self
    def __rsub__(self, left):
        if type(left) is int:
            for_z = left
            nennerNeu = self.nenner
            zaehlerNeu = for_z * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' - Bruch()')


#----------------------------------Multiplikation
    def __mul__(self, zaehler):
        """
        multiplies two Bruch's with each other
        :param zaehler: the second Bruch or int
        :return: Result
        """
        if isinstance(zaehler, Bruch):
            for_z, for_n = zaehler
        elif type(zaehler) is int:
            for_z, for_n = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' * Bruch()')
        for_z *= self.zaehler
        for_n *= self.nenner
        return Bruch(for_z, for_n)

    def __rmul__(self, zaehler):
        """
        Right Side multiplikation
        :param zaehler:
        :return:
        """
        return self.__mul__(zaehler)

    def __imul__(self, other):
        """
        intern multiplikation
        :param other: Bruch or int
        :return: Bruch
        """
        other = Bruch.__makeBruch(other)
        self = self * other
        return self

#-------------------------------Division
    def __truediv__(self, zaehler):
        """
        divides two Bruchs with each other
        :param zaehler: Bruch or Int
        :return: Result
        """
        if isinstance(zaehler, Bruch):
            for_z, for_n = zaehler
        elif type(zaehler) is int:
            for_z, for_n = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' / Bruch()')
        if for_z == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(for_n, for_z))
    def __itruediv__(self, other):
        """
        intern division
        :param other: Bruch or int
        :return: Result
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self
    def __rtruediv__(self, left):
        """
        right side division
        :param left: left side
        :return:
        """
        if type(left) is int:
            for_z = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(for_z, self.zaehler)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' / Bruch()')



    def __repr__(self):
        """
        Represents the instance
        :return: representation
        """
        shorten = Bruch.greatestCommonDivisor(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)
    def __makeBruch(other):
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(other).__name__ + ' not an int nor a Bruch')

    @classmethod
    def greatestCommonDivisor(cls,x,y):
        """
        greatestCommonDivisor
        :param int x: first value
        :param int y: second value
        :return: greatest common divisor
        """
        x,y=abs(x),abs(y) # positive Werte!!
        if x<y: x,y=y,x
        #Berechnung
        while y != 0:
            x,y = y,x%y
        return x

    def __iter__(self):
        """
        Class is iterable
        """
        return (self.zaehler, self.nenner).__iter__()
