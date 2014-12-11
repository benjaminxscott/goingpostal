#!/usr/bin/python
#Ben Schmoker -MITRE Corporation
#SYNOPSIS: grab URLs of the files we want, and download them to a local folder 
#Uses local proxy settings

from xgoogle.search import *
from optparse import OptionParser
from urllib import urlretrieve
import os

def getfilename (title):
	#get string after last /
	(before, sep, after) = title.rpartition('/')
	return after

def get_file (url):
	print "DOWNLOAD" , url
	filename = getfilename(line.url)
	filename = save_dir + filename 
	try:
		urlretrieve(url, filename)
		print "\tSAVED", filename
	except IOError, e:
		print "Problem downloading %s, code: %s" %filename %e
	return  
	
#-------------MAIN---------------
#handle arguments/options	
parser = OptionParser()
parser.add_option("-n", "--num_files", dest="num_files", help="number of files to download, default 10")
#save in given dir
parser.add_option("-d", "--savedir", dest="save_dir", help="directory in which to save files, default './out_files'")
#filetype
parser.add_option("-t", "--filetype", dest="filetype", help="type of file to download, default pdf")
#TODO dl from a given engine
parser.add_option("-s", "--source", dest="source", help="sources to download files from, default google")
#TODO dl from sites listed in newline sep file
parser.add_option("-f", "--sitesfile", dest="sitesfile", help="file containing particular target sites, one per line")

(options, args) = parser.parse_args()
save_dir = options.save_dir
filetype = options.filetype
source = options.source

if len(args) != 1:
	parser.error("incorrect number of args")
else:
	topic = args[0]

#default values and such
if save_dir is None:
	save_dir= "./out_files/"
if not save_dir.endswith('/'):
	save_dir += '/'
if options.num_files is None:
	num_files= 10
else:
	num_files = int(options.num_files)
if filetype is None:
	filetype = 'pdf'
if filetype.startswith('.'):
	filetype = filetype [1:]
if source is None:
	source = 'google'

#build query based on our input
query = "filetype:%s " %filetype
query = query + topic 

try:
	search = GoogleSearch( query )
	search.results_per_page = num_files
	#I may not the best cop on the force, but I get results.
	results = search.get_results()

	#create target dir if not exist
	if not os.path.isdir( save_dir ):
		os.makedirs( save_dir )

	#pull down our files
	print "STARTING PULLDOWN. This may take a while"
	for line in results:
		get_file(line.url)

except SearchError, e:
	print "Failure to search, code: %s" % e
