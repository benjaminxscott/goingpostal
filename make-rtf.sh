#!/bin/bash

#TODO handle profiles (e.g. refer to different grammars in make-latex)
#TODO read in seperated list of files to gen from STDIN
PREVDIR=$PWD
SCIGENDIR=/home/ben/mitre/honeynet/mod_scigen
TMPDIR=/tmp/make-rtf
USAGE="Usage: $0 title author\nCreates an rtf file with given title under ./rtf\n"
TITLE=$1
AUTHOR="$2"
#check args
if [ $# -lt 2 ]
then 
	echo -e $USAGE
	exit
fi

#check if rtf repo exists
if [ ! -d $PREVDIR/rtf ]
then 
	echo "makin' a directory here"
	mkdir $PREVDIR/rtf 
fi

#get the first word of title
FILENAME=$(echo $TITLE | awk -F" " '{print $1}')
cd $SCIGENDIR
./make-latex.pl --savedir $TMPDIR --title "$TITLE" --author "$AUTHOR"
cd $TMPDIR
TEX=$(ls *.tex)
#create the RTF file
latex $TEX
latex2rtf $TEX
cp *.rtf $PREVDIR/rtf/$FILENAME.rtf
cd $PREVDIR
