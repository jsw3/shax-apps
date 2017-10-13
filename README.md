# shax-apps

These are basic tools for processing and extracting information about Shakespeare's First Folio.

There are three main pieces:

A main script written in Python that processes a .txt file containing the first folio itself (slightly modified). This file is "Shax_Folio.py". It uses the two .txt files and all four .db files.

A basic website that used a Python helper script to generate html documents. I have not included the html files but you can generate them on your own using the "ff_processor.py" file. Simply execute the file in the desired directory and it will create 35 html files corresponding to each play. You must also place "Shax_Folio.py" and "FirstFolio.txt" in the same directory. The website includes some Javascript, in "folio.js", to navigate the site and also to access a "concordance" for a given word that the user is interested in.

A small Java applet that again used the main Python text processor to generate an XML document that the applet uses to display information for the play selected by the user.
