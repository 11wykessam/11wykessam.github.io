#return length of strings of all number names 1 to 1000
digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",\
          "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numberToString (number) :
    characters = str(number)
    if number > 0 :
        if number < 20 :
            return digits[number]
        elif number < 100 :
            return tens[int(characters[0])] + "" + digits[int(characters[1])]
        elif number < 1000:
            if number % 100 == 0 :
                return digits[int(characters[0])] + "hundred"
            else :
                return digits[int(characters[0])] + "hundredand" + numberToString(int(characters[1] + "" + characters[2]))
        elif number == 1000 :
            return "onethousand"
        else :
            return ""
    else:
        return ""

finalString = ""
for n in range(1, 1001) :
    finalString += numberToString(n)

print(len(finalString))