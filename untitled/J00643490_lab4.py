'''
Name: Alan Pysnack
JagID: J00643490
Date: 7/9/2020

'''


import argparse

parser = argparse.ArgumentParser(description='Encode or Decode a Caesar Cipher')
parser.add_argument('-i', '--input_file', type=str, metavar='', help='The name of the text file you wish to read')
parser.add_argument('-o', '--output_file', type=str, metavar='', help='The name of the output text file')
parser.add_argument('-e', '--encode', action='store_true')
parser.add_argument('-d', '--decode', action='store_true')
parser.add_argument('-r', '--rotation', type=int, metavar='', help='How much you want to shift e.g. "13" for ROT-13')
args = parser.parse_args()


def main():

    if args.input_file is None and args.output_file is None:
        # 1. Prompts the user to enter an English greeting to be translated into Swedish.
        input_list = input("Please enter the English greeting you would like translated to swedish: ").split()
        print(translate(input_list))

    else:
        # 2. Allows user to enter command line arguments to encode/decode caesar ciphers
        rot(args.input_file, args.output_file, args.encode, args.decode, args.rotation)
    

def translate(list_input):
    swedish = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    prompt = False

    return_string = ''

    for word in list_input:
        if word.lower() in swedish:
            return_string += swedish[word.lower()] + ' '
        else:
            return_string += word.lower() + '(?) '
            prompt = True
    if prompt:
        print("One or more of your words was not recognized.")

    return return_string


def rot(input_file, output_file, encode, decode, rotation):

    input_file = input_file.lower()
    output_file = output_file.lower()
    output_string = ''
    write_string = ''

    with open(input_file, 'r') as f:
        f.seek(0)
        f_contents = f.readlines()

        for line in f_contents:
            output_string += line.lower()


    if rotation is None:
        rotation = 13

    shift = rotation

    if encode and decode:
        print('Please only choose one, -e or -d.')

    if encode:
        for word in output_string:
            for letter in word:
                if letter.isalpha():
                    a = ord(letter) + shift
                    if a > 122:
                        a = (a - 123) + 97
                    write_string += chr(a) + ''

                else:
                    write_string += letter + ''

    elif decode:
        for word in output_string:
            for letter in word:
                if letter.isalpha():
                    a = ord(letter) - shift
                    if a < 97:
                        a = 123 - (97 - a)
                    write_string += chr(a) + ''

                else:
                    write_string += letter + ''

    else:
        print('Encode/Decode command not recognized')

    with open(output_file, 'w') as out_file:
        out_file.seek(0)
        out_file.write(write_string)


main()
