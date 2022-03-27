"""
Homework 2 | Question 1
Name       | Noga Zohar
ID         | 313263485
"""
# morse dictionary
MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

# translation function
def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """

    # open english text file
    with open(input_file) as lorem:
        english_lorem = lorem.read()

    # convert to uppercase
    english_lorem = english_lorem.upper()

    # translate to morse
    morse_map = english_lorem.maketrans(MORSE_CODE)
    morse_str = english_lorem.translate(morse_map)

    # split to different lines
    morse_lorem = morse_str.replace(' ','\n')

    # write to output file
    with open(output_file,'w') as output_lorem:
        output_lorem.write(morse_lorem)

# run function
if __name__ == '__main__':
    # Question 1
    english_to_morse()