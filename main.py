# decimal number to roman numerals
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
        # won't work with 2.7. ends the output with a <space>
            print(rom[i], end = "")
            div -= 1
        i -= 1
 
# Driver code
if __name__ == "__main__":
    number = 2021
    printRoman(number)
