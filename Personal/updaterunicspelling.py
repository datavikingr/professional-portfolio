#!python3
import json

##########################################
def switcheroo(victim, box):
    if victim in box:
        return box[victim]
    return victim

##########################################
# Fist Pass: Letter/rune Typos
##########################################
with open('dictionaries/yf_letterswap.json') as f:
    ls_dict = json.load(f)
with open('ON-YF.txt', 'r') as g:
    input_text = g.read()
modified_chars = [switcheroo(c, ls_dict) for c in input_text]
modified_s = ''.join(modified_chars)
with open('ON-YF.txt', 'w') as f:
    f.write(modified_s)
##########################################
# Second Pass: Proper spell check
##########################################
with open('dictionaries/yf_spellcheck.json') as dictionary:
    sc_dict = json.load(dictionary)
with open('ON-YF.txt', 'r') as source:
    lines = source.readlines()
modified_lines = []
for line in lines:
    words = line.split('᛫')
    modified_words = [switcheroo(word, sc_dict) for word in words]
    modified_line = '᛫'.join(modified_words)
    modified_lines.append(modified_line)
with open('ON-YF.txt', 'w') as f:
    f.writelines(modified_lines)
