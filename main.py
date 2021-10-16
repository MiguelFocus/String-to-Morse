from sys import argv

morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

# Get user input from Comand Line
user_input = argv[1:]

# Convert list of inputs into list of letters
lowered_list = []
for word in user_input:
    lowered_list.append(word.lower())

list_user = [list(word) for word in lowered_list]

morse_letter_list = []


# Convert letters into morse
for word in list_user:
    try:
        for c in word:
            morse_letter_list.append(morse_code[c])
        if len(list_user) > 1:
            morse_letter_list.append('/')
    except KeyError:
        print('Wrong character, try again')

# Convert morse into words
morse_word = ' '.join(morse_letter_list)

print(morse_word)
