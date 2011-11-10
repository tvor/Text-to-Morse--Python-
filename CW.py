"""
International Telegraphic Code by Robert Hawk
"""
import time, sys
##try:
##    import speech
##except:
##    print "Speech Module Unavailable.\n"
from winsound import Beep
from msvcrt import getche

"""
Text to International Telegraphic Code
"""
CW = {
    '!':[2,2,1,2,1,2],
    '"':[1,2,1,1,2,1],
    '$':[2,1,1,2,1,1,1],
    '&':[1,2,1,1,1],
    "'":[1,2,2,2,2,1],
    '(':[2,1,2,2,1,2],
    ')':[2,1,2,2,1,2],
    '+':[1,2,1,2,1],
    ',':[2,2,1,1,2,2],
    '-':[2,1,1,1,1,2],
    '.':[2,1,2,1,2,1],
    '/':[1,2,1,1,2],
    '0':[2,2,2,2,2],
    '1':[1,2,2,2,2],
    '2':[1,1,2,2,2],
    '3':[1,1,1,2,2],
    '4':[1,1,1,1,2],
    '5':[1,1,1,1,1],
    '6':[2,1,1,1,1],
    '7':[2,2,1,1,1],
    '8':[2,2,2,1,1],
    '9':[2,2,2,2,1],
    ':':[1,1,1,2,2,2],
    ';':[2,1,2,1,2,1],
    '=':[2,1,1,1,2], 
    '?':[1,1,2,2,1,1], 
    '@':[2,1,2,1,1,1],
    'A':[1,2], 
    'B':[2,1,1,1], 
    'C':[2,1,2,1],
    'D':[2,1,1],
    'E':[1,],
    'F':[1,1,2,1],
    'G':[2,2,1],
    'H':[1,1,1,1],
    'I':[1,1], 
    'J':[1,2,2,2],
    'K':[2,1,2],
    'L':[1,2,1,1],
    'M':[2,2],
    'N':[2,1],
    'O':[2,2,2],
    'P':[1,2,2,1],
    'Q':[2,2,1,2],
    'R':[1,2,1], 
    'S':[1,1,1], 
    'T':[2,],
    'U':[1,1,2],
    'V':[1,1,1,2],
    'W':[1,2,2],
    'X':[2,1,1,2],
    'Y':[2,1,2,2],
    'Z':[2,2,1,1],
    '_':[2,1,2,2,1,1],
    '`':[1,2,2,2,2,1]
    };

"""Procedural Signals for International Telegraphic Code"""

Prosign = {
    'AA':[[1,2,1,2], 'End of Line'],
    'AAA':[[1,2,1,2,1,2], 'Full Stop'],
    'AR':[[1,2,1,2,1], 'End of Message'],
    'AS':[[1,2,1,1,1], 'Please Stand By'], 
    'BK':[[2,1,1,1,2,1,2], 'Break, Back to You'],
    'BT':[[2,1,1,1,2], 'Stop, End of Sentence'],
    'CL':[[2,1,2,1,1,2,1,1], 'Closing Down'],
    'CT':[[2,1,2,1,2], 'Start, Commence Transmission'],
    'IMI':[[1,1,2,2,1,1], 'Repeat, Say Again'],
    'KN':[[2,1,2,2,1], 'OK, Named Station'],
    'SK':[[1,1,1,2,1,2], 'Stop Keying, End of Contact'],
    'SN':[[1,1,1,2,1], 'Understood'],
    'SOS':[[1,1,1,2,2,2,1,1,1], 'Emergency, Come Quickly'], 
    'VA':[[1,1,1,2,1,2], 'End of contact'],
    'VE':[[1,1,1,2,1], 'Understood']
    };

def set_code_constants(wpm):
    """Morse word per minute Dependent constants"""
    global dit
    global dah
    global dit_sec
    global dah_sec
    global char_sec
    global word_sec
    global sentence_sec
    
    dit = 1200 / wpm       # milliseconds
    dah = 3 * dit           # milliseconds
    dit_sec = dit / 1000.0    # seconds
    dah_sec = 3.0 * dit_sec    # seconds
    char_sec = 2.0 * dit_sec   # seconds
    word_sec = 3.0 * dit_sec   # seconds
    sentence_sec = 6.0 * dit_sec # seconds
    return wpm

# Set initial words per minute here <--------------
wpm = set_code_constants(25)

# Set initial frequency here        <--------------
freq = 640

def Dot():
    print '\bdi-',
    Beep(freq, dit)
    time.sleep(dit_sec)

def Dash():
    print '\bDA-',
    Beep(freq, dah)
    time.sleep(dah_sec)

def Send(code):
    """ """
    for number in code:
        exec({
            0:'',
            1:'Dot()',
            2:'Dash()',
            3:'',
            4:''}
             [number])
        time.sleep(dit_sec)
    if number == 1:
        print "\b\bt ",
    else:
        print "\b\bH ",
    time.sleep(word_sec)    

def Radio(text):
    text = text.upper()
    words = text.split()
    for word in words:
        if word in Prosign:
            code, word = Prosign[word]
            print word
            Send(code) 
        else:
            print word
            for letter in word:
                if letter in CW:
                    Send(CW[letter])
                if letter == ".":
                    time.sleep(sentence_sec)
                else:
                    time.sleep(char_sec)
        print'\n'
        time.sleep(word_sec)
## End TEXT to MORSE

def Titanic():
    print "Titanic distress call at %.0f" % wpm, "words per minute."
    Radio("""CQD CQD CQD DE MGY MGY MGY I require immediate assistance 
Position 41.46 N 50.14 W MKC MKC MKC CQD CQD CQD MGY MGY MGY SOS SOS SOS 
SOS SOS SOS DE MGY MGY MGY MKC MKC MKC DE MGY MGY MGY CQD SOS de MGY We 
have struck iceberg Sinking fast Come to our assistance Position Lat 41.46 
N Long 50.14 W  MGY CQD SOS SOS CQD CQD DE MGY WE ARE SINKING FAST 
PASSENGERS ARE BEING PUT INTO BOATS MGY""")
    print "\n"

def signs():
    for word in sorted(Prosign.iterkeys()):
        print word
        try:
            for letter in word:
                speech.say(letter)
        except:
            pass
        Radio(word)
        time.sleep(char_sec)

def alphabet():
    for letter in sorted(CW.iterkeys()):
        try:
            speech.say(letter)
        except:
            pass
        Radio(letter)
        time.sleep(char_sec)
    print

def change_wpm(wpm):
    text = raw_input("New Value for Words per Minute <1..60>: ")
    if text == '':
        text = str(wpm)
    wpm = int(text)
    if (wpm < 1):
        wpm = 1
    if (wpm > 60):
        wpm = 60
    return set_code_constants(wpm)

def change_freq(freq):
    text = raw_input('New Value for Frequency <300..3000>: ')
    if text == '':
        text = str(freq)
    freq = int(text)
    if (freq < 300):
        freq = 300
    if (freq > 3000):
        freq = 3000
    return freq

def text2morse():
    while 1:
        print "\nText to Code at %.0f" % wpm, "words per minute.",
        text = raw_input('(Enter to Exit):\n')
        if text == "":
            break
        Radio(text)

def start():
    print "Words per Minute is %.0f" % wpm,
    print "Frequency is %.0f" % freq
    print '\nPress 1 to change Words per Minute'
    print 'Press 2 to change Frequency'
    print 'Press 3 for Titanic Distress Call'
    print 'Press 4 for Procedural signals'
    print 'Press 5 for Alphabet'
    print 'Press 6 for Text to Morse'
    print 'Enter to Exit\n'

while 1:
    start()
    key = getche()
    print "\b\b",
    if key in ['1','2','3','4','5','6']:
        exec({
            '1':'wpm = change_wpm(wpm)',
            '2':'frew = change_freq(freq)',
            '3':'Titanic()',
            '4':'signs()',
            '5':'alphabet()',
            '6':'text2morse()'}[key], globals(), locals())
        print
    else:
      break
