#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if roman_string and type(roman_string) is str:
        if roman_string != "":
            num_rom = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
            for pres, prev in zip(roman_string, roman_string[1:]):
                if pres not in num_rom.keys():
                    return 0
                elif num_rom[pres] >= num_rom[prev]:
                    res += num_rom[pres]
                else:
                    res -= num_rom[pres]
            res += num_rom[roman_string[-1]]
    return res
