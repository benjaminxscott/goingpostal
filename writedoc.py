#!/usr/bin/env python

#Generate RTF file using PyRTF, 
#examples were liberally used to help create this program

from optparse import OptionParser
import sys
from PyRTF import *
from random import choice


def OpenFile( name ) :
	#name as using word doc extension
	return file( '%s.doc' % name, 'w' )

def rand_author ():
	first = ['Dan', 'Jack', 'Brad', 'Denise', 'Rakash']
	last = ['Flanagan', 'Thomas', 'Smith', 'Ramachandran']
	name = choice(first) + ' ' + choice(last)

	return name

def rand_title ():
	general_area = ['Security', 'Biometric']
	general_type = ['Review', 'Literature Review', 'Assessment']
	title = choice(general_area) + ' ' + choice(general_type)

	return title

#---Garbage----------------------
# Takes: lines (def 1)
# Returns: paragraph containing garbage
#-----------------------------------
def Garbage (num_lines=1) :
	p = Paragraph( )
	
	with open(garbageFile, 'r') as infile:
		for i in range(0, num_lines):
			p.append(infile.readline())
	return p

#---Author----------------------
# Takes: author (def random)
# Returns: paragraph containing author shoutout
#-----------------------------------
def Author () :
	p = Paragraph('By ' , author)
	return p

#---Title----------------------
# Takes: Title (def random)
# Returns: paragraph containing title
#-----------------------------------
def Title () :
	p = Paragraph(title)

	return p

#---genDoc----------------------
# Takes: 
# Returns: RTF document
#----------------------------------
def genDoc ( ) :
	doc = Document()
	ss = doc.StyleSheet
	section = Section()
	doc.Sections.append( section )
		
	#XXX frustrating format stuff

	section.append(Title( ))

	section.append(Author( ))
	p = Paragraph( ss.ParagraphStyles.Normal )
 
	section.append( Garbage(10) )
	section.append( Garbage(10) )
	
#set footer
	p = Paragraph( ss.ParagraphStyles.Normal )
	p.append( footer )
	section.Footer.append( p )

	return doc

#-----------MAIN---------------
if __name__ == '__main__' :
	#handle arguments/options	
	parser = OptionParser()
	parser.add_option("-a", "--author", dest="author", help="author of document")
	parser.add_option("--footer", dest="footer", help="page footer, default is MITRE Proprietary")
	parser.add_option("-t", "--title", dest="title", help="title of the document")
	parser.add_option("-g", "--garbage", dest="garbage", help="file containing the garbage data you want")

	(options, args) = parser.parse_args()
	author = options.author
	footer = options.footer
	title = options.title
	garbageFile = options.garbage

	if len(args) < 1:
		parser.error("incorrect number of args")
	else:
		filename = args[0]

	if author is None:
		author = rand_author()
	if footer is None:
		footer = 'MITRE Proprietary'
	if title is None:
		title = rand_title()
	if garbageFile is None:
		garbageFile = './rooter.txt'
		
	#generate the document
	DocRenderer = Renderer()
	outfile = genDoc()

	DocRenderer.Write( outfile, OpenFile( filename ) )

	print "Done"
