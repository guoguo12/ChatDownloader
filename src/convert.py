#!/usr/bin/env python

"""convert.py: Converts a raw downloaded Gmail chat log to a HTML file."""

import quopri
import sys

def convert(inputFile, outputFilename = ""):
    if outputFilename == "":
        outputFilename = inputFile.split('.')[0] + ".html"

    outputText = "<html><font face=\"Arial\" size=\"2\">\n"
    outputText += extractConvo(getRaw(inputFile))
    outputText += "</font></html>"
    toFile(outputFilename, outputText)

    print "'" + inputFile + "' converted to '" + outputFilename + "'."

def convertFilelist(filelist, separateOutputFiles, outputFilename = "output.html"):
    if separateOutputFiles:
        for filename in filelist:
            convert(filename)
    else:
        outputText = "<html><font face=\"Arial\" size=\"2\">\n"
        for filename in filelist:
            outputText += extractConvo(getRaw(filename))
            outputText += "\n\n<hr>\n"
        outputText += "</font></html>"
        toFile(outputFilename, outputText)
        print str(len(filelist)) + " files converted to '" + outputFilename + "'."

def getRaw(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def extractConvo(text):
    text = text.split('\r\n\r\n')[3]
    text = text.split('------=_Part_')[0]
    text = quopri.decodestring(text)
    return text

def toFile(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()

def main():
    args = sys.argv
    if len(args) != 2:
        filename = raw_input("File: ")
    else:
        filename = args[1]

    convert(filename)

if __name__ == '__main__':
    main()