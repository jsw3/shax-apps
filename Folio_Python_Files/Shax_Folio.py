import nltk, re, shelve, time

'''
written by Joe Wallace, October 2017
use 'help(type(self)) for list of methods
'''

# creates a play text object from First Folio
class Play():
    
    def __init__(self, filename='FirstFolio.txt', title=None):
        '''initializer produces list of titles, full text of play and, if it has
        regular act breaks, individual acts accessible as list of acts 
        (but see comments in the code below)'''
        self.filename = filename
        self.title = title
        self.file = open(self.filename, encoding='utf-8')
        self.complete = self.file.read()
        self.titles = re.findall(r'FINIS.*[\n]*(.*)', self.complete) #titles
        self.titles.remove('')

        self.real_title = None

        if self.title:
            for title in self.titles:
                if self.title.lower() in title.lower():
                    self.real_title = title

        if self.real_title:
            # generates a list with titles of the plays
            _pattern = re.compile(r'%s.*?FINIS' % self.real_title, re.S)
            self.text = _pattern.findall(self.complete)
            # the code below takes care of the duplication of findings
            # if the title in the TOC is the same as the title in the body
            if 'To the memory of my beloved' in self.text[0]:
                self.text = [self.text[1]]
            elif len(self.text) == 2:
                self.text = [self.text[0]]
            self.text = ' '.join(self.text)
        else:
            self.text = self.complete

        if self.title:
            # returns a list of acts and their contents. 
            _numbers = ['Actus [pP]rimus', 'Actus [sS]ecund[aus]', 'Actus [tT]ertius',
                   'Actus [qQ]uartus', 'Actus [qQ]uintus']
            # I added an extra test for LLL, which has irregular act designations, as an example
            # note: other plays also have irregularities like this and I have not
            # done tests for them all. please be aware of these printing irregularities
            if self.real_title == "Loues Labour's lost":
                _numbers[4] = 'Actus Quartus'
            _all = []
            for i in range(5):
                if i < 4:
                    _pattern = re.compile(r'(%(first)s.*)%(second)s'
                                      % {'first': _numbers[i], 'second': _numbers[i+1]}, re.S)
                    _act = _pattern.findall(self.text)
                    _act = ' '.join(_act)
                    _all.append(_act)
                else:
                    _pattern = re.compile(r'Actus [qQ]uintus.*', re.S)
                    if self.real_title == "Loues Labour's lost":
                        _pattern = re.compile(r'Actus Quartus[\.]\n\nEnter the Pedant.*FINIS', re.S)
                    _act = _pattern.findall(self.text)
                    _act = ' '.join(_act)
                    _all.append(_act)
            self.acts = _all
            self.act1 = self.acts[0]
            self.act2 = self.acts[1]
            self.act3 = self.acts[2]
            self.act4 = self.acts[3]
            self.act5 = self.acts[4]
            self.acts = ' '.join(self.acts)

    def isFolio(self):
        return True
    
    # captures all tokens via NLTK word_tokenize method
    def all_tokens(self, words):
        '''all tokens methods can take either
        a string or a list of strings'''
        if isinstance(words, list):
            words = ' '.join(words)
        tokens = nltk.word_tokenize(words)
        return tokens
    
    # captures hyphenated words but not possessives
    def word_tokens(self, words):
        '''all tokens methods can take either
        a string or a list of strings'''
        if isinstance(words, list):
            words = ' '.join(words)
        pattern = re.compile(r'[a-zA-Z-]+') 
        tokens = pattern.findall(words)
        return tokens
    
    # captures both hyphenated words and possessives
    def possessive_tokens(self, words):
        '''all tokens methods can take either
        a string or a list of strings'''
        if isinstance(words, list):
            words = ' '.join(words)
        _pattern = re.compile(r'[a-zA-Z-\']+')
        _tokens = _pattern.findall(words)
        return _tokens
    
    # removes common words, defined below; the regex includes possessives
    def uncommon_tokens(self, words):
        '''all tokens methods can take either
        a string or a list of strings'''
        _tokens = []
        _common = ['s', 'in', 'the', 'a', 'of', 'before', 'near',
                   'same', 'part', 'state', 'another', 'an',
                   'and', 'with', 'enter', 'within', 'him', 'her',
                   'as', 'their', 'he', 'she', "'s"]
        if isinstance(words, list):
            words = ' '.join(words)
        _pattern = re.compile(r'[a-zA-Z-\']+')
        _w = _pattern.findall(words)
        _tokens = [w for w in _w if w.lower() not in _common]
        return _tokens
    
    # tests words against a few texts, such as Camden, Plutarch, and Holinshed
    # this will not be perfect but will give an approximation
    def fictional_words(self, words):
        tokens = self.uncommon_tokens(words)
        tokens = list(set(tokens))
        words = shelve.open('wordsDB')
        g = nltk.corpus.gazetteers.words()
        g = [w.lower() for w in g]
        brit = shelve.open('britanniaDB')
        plut = shelve.open('plutarchDB')
        hol = shelve.open('holinshedDB')
        total = []
        for word in tokens:
            if (word.split("'")[0].lower() in words
                or word.lower() in g
                or word.lower() in brit
                or word.lower() in plut
                or word.lower() in hol):
                total.append((word, 'NF'))
            else:
                total.append((word, 'F'))
        return total
    
    # tests words against dictionary, gazetteer, and Camden's Brittannia
    # like fictional words above, not perfect but gives you some indication    
    def fictional_settings(self, text):
        words = shelve.open('wordsDB')
        gazetteer = nltk.corpus.gazetteers.words()
        gazetteer = [w.lower() for w in gazetteer]
        britannia = shelve.open('britanniaDB')
        tokens = self.uncommon_tokens(text)
        tokens = [w for w in set(tokens)]
        total = []
        for word in tokens:
            if (word.split("'")[0].lower() in words
                or word.lower() in gazetteer
                or word.lower() in britannia):
                total.append((word, 'NF'))
            else:
                total.append((word, 'F'))
        return total
    
    # returns percentage of every individual word in the play, against total number of words used;
    # indicates diversity of the vocabulary
    def lexical_diversity(self, tokens):
        return str(round(len(set(tokens))/len(tokens)*100, 2)) +' {0}'.format('%')
    
    # returns a dictionary of words and number of times each one is used
    # set 'strict' to 'true' to include possessives
    def context_count(self, tokens, strict=False):
        text = self.play.text
        d = {}
        if strict:
            _pattern = re.compile(r'[a-zA-Z-\']+')
        else:
            _pattern = re.compile(r'[a-zA-Z-]+')
        words = _pattern.findall(text)
        for word in words:
            if word in tokens:
                d[word.lower()] = d.get(word, 0) + 1
        return d
    
    # pass this method a list of tokens; the method adds the token to a list every time it encounters
    # it in a text. then it uses the NLTK FreqDist method to convert that list into a frequency distribution
    # and then plot that distribution
    def context_plot(self, tokens, strict=False):
        text = self.play.text
        t = []
        if strict:
            _pattern = re.compile(r'[a-zA-Z-\']+')
        else:
            _pattern = re.compile(r'[a-zA-Z-]+')
        words = _pattern.findall(text)
        t = [w.lower() for w in words if w in tokens]
        fdist = nltk.FreqDist(t)
        fdist.plot()
    
    # pass this method a list of tokens and it will do an NLTK dispersion plot, 
    # which means it will show where each term occurs in the text imagined as a linear progression
    def dispersion_plot(self, tokens):
        text = nltk.Text(tokens)
        text.dispersion_plot(list(set(tokens)))
        
    def plot(self, tokens, n=0, c=False):
        '''pass an integer as n to specify how many samples to plot.
        'c=True' to see a cumulative plot'''
        fdist = nltk.FreqDist(tokens)
        if n:
            fdist.plot(n, cumulative=c)
        else:
            fdist.plot(cumulative=c)
        
    # returns list of setting descriptions from CW            
    def get_settings(self):
        _s = CWPlay(title=self.title) # create CWPlay object
        self.settings = _s.settings
        return self.settings
    
    # shows progression of settings as they occur in play
    # needs to be passed a list of settings; use 'get_settings'
    def settings_flow(self, settings):
        _memo = {}
        for i in range(len(settings)):
            _key = settings[i]
            if _key not in _memo:
                print('to ' + _key)
                _memo[_key] = 1
            else:
                print('back to ' + _key)
                _memo[_key] += 1
    
    def get_characters(self, text):
        '''list of lists of strings --> list of strings
        or string --> list of strings. returns list of characters based on their entrances'''
        # just make sure this works
        _chars = []
        if isinstance(text, list):
            for t in text:
                # returns a character list for each act, or set of acts
                _pattern = re.compile(r'Enter .*\n.*|Enter .*')
                characters = _pattern.findall(text)
                characters = [c.strip() for c in characters]
                characters = [' '.join(c.splitlines()) for c in characters]
                characters = [c.lstrip('Enter') for c in characters]
                characters = [c.lstrip(' ') for c in characters]
                characters = ' '.join(characters)
                _chars.append(characters)
        else:
            # returns a character list for each act, or set of acts
            _pattern = re.compile(r'Enter .*\n.*|Enter .*')
            _chars = _pattern.findall(text)
            _chars = [c.strip() for c in characters]
            _chars = [' '.join(c.splitlines()) for c in characters]
            _chars = [c.lstrip('Enter') for c in characters]
            _chars = [c.lstrip(' ') for c in characters]
        return _chars
    
    def cfdist_tabulate(self, text, term):
        '''text should be a list of strings; 
        should be used with character list from get_characters method'''
        cfdist = nltk.ConditionalFreqDist([(s, term) for s in text
                                           if term.lower() in s.lower()])
        cfdist.tabulate()

    def entrances(self, character, text):
        '''text needs to be list of strings'''
        print(character.upper() + ':')
        print('')
        count = 0
        for entrance in text:
            if character.lower() in entrance.lower():
                count += 1
                print(entrance)
        print('')
        if count == 1:
            print(character.upper() + ' entered one time')
        else:
            print(character.upper() + ' entered ' + str(count) + ' times')
            
    # returns a list of characters
    def dramatis_personae(self, tokens):
        chars = [c for c in tokens if c[0].isupper()]
        chars = sorted(list(set(chars)))
        g = nltk.corpus.gazetteers.words()
        g = [w.lower() for w in g]
        chars = [w for w in chars if w.lower() not in g] # test tokens against gazetteer
        return chars
       
# creates a play text from CW
class CWPlay(Play):
    
    def __init__(self, filename='ShakespeareCW_clean.txt', title=None):
        '''the initializer creates the 'settings' attribute, 
        which is a list of strings containing the settings'''
        self.filename = filename
        self.title = title

        self.file = open(self.filename)
        self.complete = self.file.read()

        _pattern = re.compile(r'15\d\d\n*.*|16\d\d\n*.*')
        _t = _pattern.findall(self.complete)
        _t = ' '.join(_t)
        _pattern = re.compile(r'15\d\d\n*|16\d\d\n*')
        self.titles = _pattern.split(_t)
        self.titles = [s.strip() for s in self.titles if s!= '']
        
        self.real_title = None

        if self.title:
            for title in self.titles:
                if self.title.lower() in title.lower():
                    self.real_title = title

        if self.real_title:
            _pattern = re.compile(r'%s.*?\d{4}' % self.real_title, re.DOTALL)
            self.text = _pattern.findall(self.complete)
            self.text = ' '.join(self.text)
        else:
            self.text = self.complete # list of strings
            
        # add settings attribute
        _pattern = re.compile(r'SCENE.*\n*.*|Scene.*\n*.*') #extract scene descriptions
        _s = _pattern.findall(self.text)
        _s = ' '.join(_s)

        _pattern = re.compile(r'SCENE.*|Scene.*') # clean up scene descriptions
        _s = _pattern.split(_s)
        _s = [s.strip() for s in _s if s!='' and s!='\n' and s!='\n '
              and not s.strip().startswith('ACT')]
  
        self.settings = _s # this is a list of setting descriptions

    def isFolio(self):
        return False

def pause():
    i = 0
    while i < 3:
        print('.')
        time.sleep(1)
        i += 1

def cont():
    print('Press enter to continue')
    input()

# demonstration
def main():
    '''do some tests'''
    print('This is a demonstration of how the script works', end='\n\n')
    cont()
    hamlet = Play(title='hamlet') # hamlet is a Folio play object. text available as [self].text
    print('First create a play object named "hamlet"')
    pause()
    cont()
    print('Word_tokens returns all words in the text')
    pause()
    cont()
    word_tokens = hamlet.word_tokens(hamlet.text) # all words in the text
    print('Here are the first 100 tokens from Hamlet:', end='\n\n')
    print(word_tokens[:100])
    pause()
    cont()
    print('Lexical diversity can be displayed for any group of tokens:')
    ld = hamlet.lexical_diversity(word_tokens)
    print('Lexical diversity of all the tokens in the text is ' + ld)
    settings = hamlet.get_settings()
    pause()
    cont()
    print('Settings are available; settings_flow helps to display them')
    pause()
    cont()
    hamlet.settings_flow(settings)
    pause()
    cont()
    print('Characters are available as well')
    chars = hamlet.get_characters(hamlet.text)
    pause()
    cont()
    print(chars)
    pause()
    cont()
    print('You can tokenize the character strings or not. ' + 
    'cfdist_tabulate shows the frequency of a given character')
    print('For example, Hamlet:')
    hamlet.cfdist_tabulate(chars, 'Hamlet')
    pause()
    cont()
    print('cfdist_tabulate can be used for settings as well')
    pause()
    cont()

#if __name__ == '__main__':
#    main()
    
    
