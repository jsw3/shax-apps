# a script to process folio text and create files for each play

import Shax_Folio as sxf
import re

#create full text object to get all titles
fol_obj = sxf.Play()

# use titles to name documents and to access texts
all_titles = fol_obj.titles 

# the string to write the html file, if contains acts
def act_grammar(title, act1, act2, act3, act4, act5): # add sections for each act
    html ='''<!DOCTYPE html>
    <html>
    <head>
        <link href="play_style.css" rel="stylesheet">
        <script src="folio.js"></script>
        </head>
    <body>
        <h1 id="title">'''+title+'''</h1>
        <div id="actions"></div>
            <ul>
                <li>
                    <a href="#act1">Act 1</a>
                    <a href="#act2">Act 2</a>
                    <a href="#act3">Act 3</a>
                    <a href="#act4">Act 4</a>
                    <a href="#act5">Act 5</a>
                </li>
                <li>
                    <button id="previous">Previous</button>
                    <button id="next">Next</button>
                    <button id="reset">Reset</button>
                    <button id="home">Home</button>
                </li>
            </ul>
            <form name="concordance" method="get">
                <label id="lab">Show Concordance
                <input type="text" name="word" placeholder="Enter a Word">
            </form>
        </div>
        <p id="act1" class="text">'''+act1+'''</p>
        <p id="act2" class="text">'''+act2+'''</p>
        <p id="act3" class="text">'''+act3+'''</p>
        <p id="act4" class="text">'''+act4+'''</p>
        <p id="act5" class="text">'''+act5+'''</p>
    </body>
    </html>
    '''
    return html

def no_act_grammar(title, text):
    html ='''<!DOCTYPE html>
    <html>
    <head>
        <link href="play_style.css" rel="stylesheet">
        <script src="folio.js"></script>
        </head>
    <body>
        <h1 id="title">'''+title+'''</h1>
        <div id="actions"></div>
            <ul>
                <li>
                    <button id="previous">Previous</button>
                    <button id="next">Next</button>
                    <button id="reset">Reset</button>
                    <button id="home">Home</button>
                </li>
            </ul>
            <form name="concordance" method="get">
                <label id="lab">Show Concordance
                <input type="text" name="word" placeholder="Enter a Word">
            </form>
        </div>
        <p id="fulltext" class="text">'''+text+'''</p>
    </body>
    </html>
    '''
    return html

#the function to process the texts
def process():
    for t in all_titles:
        play = sxf.Play(title=t)

        if play.act1:
            # now process the text for html
            act1 = play.act1.replace('\n', '<br>')
            act2 = play.act2.replace('\n', '<br>')
            act3 = play.act3.replace('\n', '<br>')
            act4 = play.act4.replace('\n', '<br>')
            act5 = play.act5.replace('\n', '<br>')

            #now create file and write html
            file = open(t+'.html', 'w', encoding='utf-8')
            file.write(act_grammar(t, act1, act2, act3, act4, act5))
            file.close
        else: # in case the play does not have act breaks
            text = play.text.replace('\n', '<br>')
            file = open(t+'.html', 'w', encoding='utf-8')
            file.write(no_act_grammar(t, text))
            file.close

def preface():
    play = sxf.Play()
    pattern = re.compile('To the Reader.*?FINIS', re.S)
    text = pattern.findall(play.text)
    text = ' '.join(text)
    text = text.replace('\n', '<br>')
    file = open('Preface.html', 'w', encoding='utf-8')
    file.write(no_act_grammar('Prefatory Matter', text))
    file.close

if __name__ == '__main__':
    peface()
    process()
