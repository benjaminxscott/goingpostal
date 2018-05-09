# Setup

## Install SCIgen 

```
1. Get cvs - apt-get install cvs
2. pull down scigen using cvs
	-cvs -d :pserver:anoncvs@cvs.pdos.csail.mit.edu:/cvs login
	-no pass
	-cvs -d :pserver:anoncvs@cvs.pdos.csail.mit.edu:/cvs co -P scigen

3. get latex - apt-get install texlive

4. install gnuplot and graphviz using synaptic
```

## Usage


1. run ./make-latex, possibly with --title or --author.
2. enter 'R' at the prompts until it actually opens the file (fixed by removing figures)
3. Save as whatever.ps (or use --file to save directly)
4. ps2ascii whatever.ps > whatever.txt
5. tada! a text file with random paper in it.

Alternatively:
1. run ./make-latex --savedir "tmpdir" --title "mytitle" --author "Ben"
2. cd to tmpdir
3. latex texfile
4. latex2rtf texfile
5. Convert rtf to docx on windows using OLE perl module

