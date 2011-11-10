"""
American or Railroad Telegraphic Code by Robert Hawk
"""
import sys, time
##try:
##    import speech
##except:
##    print "Speech Module Unavailable.\n"
from winsound import PlaySound
from msvcrt import getche

"""
bitwise or of winsound.SND_FILENAME and winsound.SND_NOWAIT
"""
Flags = 139264

"""
0 = internal space, 1 = dit (e.g. E), 2 = dah (e.g. T),
3 = long dah (i.e. L), 4 = longer dah (i.e. 0)
"""
Vail = {
    '0':[4,],
    '1':[1,2,2,1],
    '2':[1,1,2,1,1],
    '3':[1,1,1,2,1],
    '4':[1,1,1,1,2],
    '5':[2,2,2],
    '6':[1,1,1,1,1,1],
    '7':[2,2,1,1],
    '8':[2,1,1,1,1],
    '9':[2,1,1,2],
    'A':[1,2],
    'B':[2,1,1,1],
    'C':[1,1,0,1],
    'D':[2,1,1],
    'E':[1,],
    'F':[1,2,1],
    'G':[2,2,1],
    'H':[1,1,1,1],
    'I':[1,1],
    'J':[2,1,2,1],
    'K':[2,1,2],
    'L':[3,],
    'M':[2,2],
    'N':[2,1],
    'O':[1,0,1],
    'P':[1,1,1,1,1],
    'Q':[1,1,2,1],
    'R':[1,0,1,1],
    'S':[1,1,1],
    'T':[2,],
    'U':[1,1,2],
    'V':[1,1,1,2],
    'W':[1,2,2],
    'X':[1,2,1,1],
    'Y':[1,1,0,1,1],
    'Z':[1,1,1,0,1],
    '!':[2,2,2,1],
    '$':[1,1,1,1,2,1,1],
    '&':[1,0,1,1,1],
    "'":[1,2,2,2,2,1],
    '<':[2,1,2,2,1],
    '>':[2,1,2,2,1,2],
    '(':[1,1,1,1,1,2,1],
    ')':[1,1,1,1,1,1,1,0,1,1],
    ',':[1,2,1,2],
    '.':[1,1,2,2,1,1],
    '/':[2,1,1,2,1],
    '?':[2,1,1,2,1],
    '@':[1,2,2,1,2,1]
    };

def byLandline(switch):
    """1 = Telegraph, 0 = Spark Gap Radio"""
    global clik
    global clak
    global elll
    global zero

    """
    The following were downloaded with Weaver, a text to code program.
    available from http://www.nu-ware.com/
    """
    if switch:
        clik = "C:/Python26/Morse/TelegraphSounderDit.wav"
        clak = "C:/Python26/Morse/TelegraphSounderDah.wav"
        elll = "C:/Python26/Morse/TelegraphSounderL.wav"
        zero = "C:/Python26/Morse/TelegraphSounderZero.wav"
    else:
        clik = "C:/Python26/Morse/RotarySparkDit.wav"
        clak = "C:/Python26/Morse/RotarySparkDah.wav"
        elll = "C:/Python26/Morse/RotarySparkL.wav"
        zero = "C:/Python26/Morse/RotarySparkZero.wav"
    return switch

switch = byLandline(1)

def set_code_constants(wpm):
    """Morse words per minute Dependent variables"""
    global dit
    global dah
    global ell
    global zer
    global dit_sec
    global dah_sec
    global ell_sec
    global zer_sec
    global char_sec
    global word_sec
    global sentence_sec
    
    dit = 1200 / wpm
    dah = 2 * dit
    ell = 4 * dit
    zer = 6 * dit
    dit_sec = dit / 1000.0       # seconds
    dah_sec = 2.0 * dit_sec      # seconds
    ell_sec = 4.0 * dit_sec      # seconds
    zer_sec = 6.0 * dit_sec      # seconds
    char_sec = 2.0 * dit_sec           # seconds
    word_sec = 3.0 * dit_sec     # seconds
    sentence_sec = 6.0 * dit_sec # seconds
    return wpm

# Change initial words per minute here <--------------
wpm = set_code_constants(20)

def Send(args):
    """text, sound, time = args"""
    print args[0],
    if args[1]:
        PlaySound(args[1], Flags)
    time.sleep(args[2])

def Telegraph(text):
    text = text.upper()
    text = text.split()
    for word in text:
        print word
        for letter in word:
            if letter in Vail:
                for number in Vail[letter]:
                    Send({
                        0:['\b\bt-', None, dit_sec],
                        1:['\bdi-', clik, dit_sec],
                        2:['\bDA-', clak, dah_sec],
                        3:['\bDAA-', elll, ell_sec],
                        4:['\bDAAA-', zero, zer_sec]}
                         [number])
                if letter == ".":
                    time.sleep(sentence_sec)
                else:
                    time.sleep(char_sec)
            if number == 1:
                print "\b\bt ",
            else:
                print "\b\bH ",
        print
        time.sleep(word_sec)

def Gettysburg():
    print "Gettysburg Address at %.0f" % wpm, "words per minute."
    Telegraph("""four score and seven years, ago our fathers brought forth 
on this continent, a new nation conceived in liberty, and dedicated to
the proposition that all men are created equal. now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived 
and so dedicated, can long endure. we are met on a great battlefield of 
that war. we have come to dedicate a portion of that field as a final 
resting place for those who here gave their lives, that that nation 
might live. it is altogether fitting and proper that we should do this. 
but in a larger sense, we can not dedicate, we can not consecrate, we can 
not hallow this ground. the brave men living and dead, who struggled 
here have consecrated it far above our poor power to add or detract. 
the world will little note, nor long remember what we say here. but it 
can never forget what they did here. it is for us the living rather to 
be dedicated here to the unfinished work which they who fought here 
have thus far so nobly advanced. it is rather for us to be here 
dedicated to the great task remaining before us. that from these 
honored dead we take increased devotion to that cause for which they 
gave the last full measure of devotion. that we here highly resolve 
that these dead shall not have died in vain. that this nation, under god, 
shall have a new birth of freedom. and that government of the people, by 
the people, for the people, shall not perish from the earth.""")
    print "\n"

def alphabet():
    for letter in sorted(Vail.iterkeys()):
        try:
            speech.say(letter)
        except:
            pass
        Telegraph(letter)
    print

def change_wpm(wpm):
    text = raw_input('\bNew Value for Words per Minute (5..60): ')
    wpm = int(text)
    if (wpm < 5):
        wpm = 5
    if (wpm > 60):
        wpm = 60
    return set_code_constants(wpm)

def wireless(switch):
    if switch:
        switch = byLandline(0)
    else:
        switch = byLandline(1)
    return switch

def text2morse():
    while 1:
        print "\nText to Code at %.0f" % wpm,"words per minute.",
        text = raw_input('(Enter to Exit):\n')
        if text == "":
            break
        Telegraph(text)

def start():
    print "Words per Minute is %.0f" % wpm
    print '\nPress 1 to change Words per Minute'
    print 'Press 2 for Gettysburg Address'
    print 'Press 3 for Alphabet'
    print 'Press 4 Toggle Telegraph / Spark Gap Radio'
    print 'Press 5 for Text to Morse'
    print 'Enter to Exit\n'

while 1:
    start()
    key = getche()
    print "\b\b",
    if key in ['1','2','3','4','5']:
        exec({
            '1':'wpm = change_wpm(wpm)',
            '2':'Gettysburg()',
            '3':'alphabet()',
            '4':'switch = wireless(switch)',
            '5':'text2morse()'}[key], globals(), locals())
    else:
        break