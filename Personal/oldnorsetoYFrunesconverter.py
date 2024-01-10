#!python3
##########################################
#TODO: Selnium output is dirty; clean this
##########################################
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, string, subprocess, json
##########################################
def strip_string(input_text, string_to_strip):
    stripped_text = input_text.replace(string_to_strip, "")
    return stripped_text
##########################################
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
##########################################
def process_input_string(driver, runa_string_in):
    if runa_string_in.strip().isdigit():
        runo_string = runa_string_in
        print(runo_string)
    else:
        input_field = driver.find_element(By.ID, 'inntak')
        input_field.send_keys(runa_string_in)
        submit_button = driver.find_element(By.ID, 'fa_runir_takki')
        submit_button.click()
        time.sleep(.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        runo_string = soup.find('h4', {'class': 'runir-nidurstada'}).contents[0]
        input_field.clear()
        print(runo_string)
    time.sleep(0.5)
    with open('3-futhark_raw.txt', 'a') as output_file:
        output_file.write(runo_string + '\n')
##########################################
def modify_characters(char, ls_dict):
    if char in ls_dict:
        return ls_dict[char]
    return char
##########################################
def modify_word(word, sc_dict):
    if word in sc_dict:
        return sc_dict[word]
    return word
##########################################
def remove_empty_lines(line):
    return line.strip()
##########################################
# First Pass: Copyright notice stripping 
##########################################
string_to_strip = input("Enter the string to strip: ")
with open('oldnorse_input.txt', 'r') as input_file:
    input_text = input_file.read()
output_text = strip_string(input_text, string_to_strip)
with open('1-oldnorse_cprtstrip.txt', 'w') as output_file:
    output_file.write(output_text)
##########################################
# Second Pass: Punctuation
##########################################
with open('1-oldnorse_cprtstrip.txt', 'r') as input_file:
    punc_input = input_file.read()
punc_output = remove_punctuation(punc_input)
with open('2-oldnorse_nopunc.txt', 'w') as output_file:
    output_file.write(punc_output)
##########################################
# Third Pass: Cross-Reference
##########################################
driver = webdriver.Chrome()
driver.get('https://runic.is/')
driver.implicitly_wait(0.5)
with open('2-oldnorse_nopunc.txt') as input_file:
    oldnorse_array = input_file.readlines()
for runa_string_in in oldnorse_array:
    process_input_string(driver, runa_string_in)
driver.close()
driver.quit()
##########################################
# Fourth Pass: Letter/rune Typos
##########################################
with open('dictionaries/yf_letterswap.json') as f:
    ls_dict = json.load(f)
with open('3-futhark_raw.txt', 'r') as g:
    input_text = g.read()
modified_chars = [modify_characters(c, ls_dict) for c in input_text]
modified_s = ''.join(modified_chars)
with open('4-futhark_allrunes.txt', 'w') as f:
    f.write(modified_s)
##########################################
# Fifth Pass: Proper spell check
##########################################
with open('dictionaries/yf_spellcheck.json') as dictionary:
    sc_dict = json.load(dictionary)
with open('4-futhark_allrunes.txt', 'r') as source:
    lines = source.readlines()
modified_lines = []
for line in lines:
    words = line.split('᛫')
    modified_words = [modify_word(word, sc_dict) for word in words]
    modified_line = '᛫'.join(modified_words)
    modified_lines.append(modified_line)
with open('5-spchked_futhark.txt', 'w') as f:
    f.writelines(modified_lines)
##########################################
# Sixth Pass: Empty Lines
##########################################
with open('5-spchked_futhark.txt', 'r') as file:
    lines = file.readlines()
modified_lines = [line for line in lines if line.strip()]
with open('11-YF-FINAL.txt', 'w') as file:
    file.writelines(modified_lines)
##########################################
# Complete.
##########################################
print('Processing completed. You have your text in runic and formatted.')
