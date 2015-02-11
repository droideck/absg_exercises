#!/usr/bin/python
# Simulate the functionality of the deprecated banner command in a script.
#+Prints arguments as a large vertical banner to stdout, using an ASCII character (default '#').


class BannerDict(dict):
    def __init__(self):
        dict.__init__(self)
        self["D1"] = "        "; self["Z1"] = "        "
        self["D2"] = " #####  "; self["Z2"] = " ###### "
        self["D3"] = " #    # "; self["Z3"] = "     #  "
        self["D4"] = " #    # "; self["Z4"] = "    #   "
        self["D5"] = " #    # "; self["Z5"] = "   #    "
        self["D6"] = " #    # "; self["Z6"] = "  #     "
        self["D7"] = " #####  "; self["Z7"] = " ###### "
        self["D8"] = "        "; self["Z8"] = "        "
        self["R1"] = "        "; self["E1"] = "        "
        self["R2"] = " #####  "; self["E2"] = " ###### "
        self["R3"] = " #    # "; self["E3"] = " #      "
        self["R4"] = " #    # "; self["E4"] = " #####  "
        self["R5"] = " #####  "; self["E5"] = " #      "
        self["R6"] = " #   #  "; self["E6"] = " #      "
        self["R7"] = " #    # "; self["E7"] = " ###### "
        self["R8"] = "        "; self["E8"] = "        "
        self["O1"] = "        "; self["K1"] = "        "
        self["O2"] = "  ####  "; self["K2"] = " #    # "
        self["O3"] = " #    # "; self["K3"] = " #   #  "
        self["O4"] = " #    # "; self["K4"] = " ####   "
        self["O5"] = " #    # "; self["K5"] = " #  #   "
        self["O6"] = " #    # "; self["K6"] = " #   #  "
        self["O7"] = "  ####  "; self["K7"] = " #    # "
        self["O8"] = "        "; self["K8"] = "        "


def draw_word(word):
    bd = BannerDict()
    for i in range(1, 9):
        print "".join([bd[char.upper() + str(i)] for char in word])[:80]


if __name__ == "__main__":
    draw_word("ok")
    draw_word("drozdek")
