# 1) Write a python class to convert an integer into a roman numeral and vice-versa

class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        roman_numeral = ''
        if self.number >= 1000:
            roman_numeral += 'M' * (self.number // 1000)
            self.number = self.number % 1000
        if self.number >= 900:
            roman_numeral += 'CM'
            self.number = self.number % 900
        if self.number >= 500:
            roman_numeral += 'D'
            self.number = self.number % 500
        if self.number >= 400:
            roman_numeral += 'CD'
            self.number = self.number % 400
        if self.number >= 100:
            roman_numeral += 'C' * (self.number // 100)
            self.number = self.number % 100
        if self.number >= 90:
            roman_numeral += 'XC'
            self.number = self.number % 90
        if self.number >= 50:
            roman_numeral += 'L'
            self.number = self.number % 50
        if self.number >= 40:
            roman_numeral += 'XL'
            self.number = self.number % 40
        if self.number >= 10:
            roman_numeral += 'X' * (self.number // 10)
            self.number = self.number % 10
        if self.number >= 9:
            roman_numeral += 'IX'
            self.number = self.number % 9
        if self.number >= 5:
            roman_numeral += 'V'
            self.number = self.number % 5
        if self.number >= 4:
            roman_numeral += 'IV'
            self.number = self.number % 4
        if self.number >= 1:
            roman_numeral += 'I' * self.number
        return roman_numeral


number_to_roman = IntegerToRoman(int(input('Enter a number: ')))
print(number_to_roman.to_roman())
