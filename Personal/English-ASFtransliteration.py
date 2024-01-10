#!python3
import time, string, subprocess, json

def modify_characters(text, swap_dict):
    result = []
    i = 0
    while i < len(text): # Check for two-letter combo
        combo = text[i:i+2]
        if combo in swap_dict:
            result.append(swap_dict[combo])
            i += 2
        else: # If not a two-letter combo, process one character
            result.append(swap_dict.get(text[i], text[i]))
            i += 1
    return ''.join(result)

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_repeated_letters(word): # Keep the first occurrence of each letter and remove consecutive duplicates
    return ''.join(char if char != prev_char else '' for char, prev_char in zip(word, [''] + list(word)))

## Scrubbing punctuation
with open('english_input.txt', 'r') as input_file:
    punc_input = input_file.read()
punc_output = remove_punctuation(punc_input)
with open('6-english_nopunc.txt', 'w') as output_file:
    output_file.write(punc_output)

## Stripping whitespace
with open('6-english_nopunc.txt', 'r') as file:
    lines = file.readlines()
modified_lines = [line.strip() for line in lines]
with open('7-english_clean.txt', 'w') as file:
    file.writelines('\n'.join(modified_lines))

## Handling the ligature runes
with open('dictionaries/asfdoubleswap.json') as ligaturerunes: # Load ligature runes dictionary
    ls_dict = json.load(ligaturerunes)
with open('7-english_clean.txt', 'r') as source: # Read input text
    input_text = source.read()
modified_chars = [modify_characters(input_text, ls_dict)] # Modify characters, considering two-letter combos
with open('8-futhorc_doublerunes.txt', 'w') as f: # Write modified text to a file
    f.write(modified_chars[0])

## Remove remaining double letters
with open('8-futhorc_doublerunes.txt', 'r') as file:
    lines = file.readlines()
modified_lines = [' '.join(remove_repeated_letters(word) for word in line.split()) for line in lines] # Remove repeated letters in each word
with open('9-futhorc_doubleletters.txt', 'w') as file:
    file.write('\n'.join(modified_lines))

## Handling the single runes
with open('dictionaries/asfsingleswap.json') as ligaturerunes:
    ls_dict = json.load(ligaturerunes)
with open('9-futhorc_doubleletters.txt', 'r') as source:
    input_text = source.read()
modified_chars = [modify_characters(c, ls_dict) for c in input_text]
modified_s = ''.join(modified_chars)
with open('10-ASF-FINAL.txt', 'w') as f:
    f.write(modified_s)
