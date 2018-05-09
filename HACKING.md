
Alternatively, on windows: get ProTex, latex2rtf
1. install cygwin, miktex 2.8, latex2rtf,
2. "install" mod_scigen folder into a directory, say 'fakefiles' in cygwin
3. "install" make-rtf.pl, rtfsave.pl into 'fakefiles'
4. cd to 'fakefiles' in cygwin
5. create an input list of titles and authors, like 
>echo -e "Cyberdeterrence"\tBen Schmoker" > files.in
6. pipe that list to make-rtf.pl, like 
> ./make-rtf.pl < files.in
NOTE: files are created in ./rtf/ by default
TODO add cmd line option to specify output dir / redir stderr
7. cd to 'fakefiles' in cmd.exe
8. run >perl rtfsave.pl rtf\[filename] 
NOTE: silent output means no error
TODO make sure it handles globbing
9. RTF file is now saved as 'out.docx' in the current directory
TODO name it the actual filename
TODO add cmd line option to specify output dir
(Optional) 10. Run 'mod_md.pl' to modify the internal metadata 

### Generate basic text

-scigen::expand is main logic for how grammar is generated
-$pretty can be set to 1 (def) to make minor improvements to the formatting
-Changing SCI_FIELDS to more "relevant" ones helps a little
?Modify grammar more to make it mor useful 
-Commented out latex diagrams (under sci_rules.in, under Latex stuff)
-Got rid of diagram references
-Less references to old hardware

### Modifying text output

-scigen.pl basically only takes command line arguments and runs scigen.pm functions
-sci_rules.in is essentially a CFG that dictates how documents come about
-Modifying the rules is possible, as scigen::read_rules parses them
FORMAT:
NAME FIRST_NAME LAST_NAME
FIRST_NAME Ben
FIRST_NAME Jim
LAST_NAME Jeffcoat
LAST_NAME Schmoker
VERSION + 5 //will generate a sequential number
#comment
blank lines are thrown away

Keep tex file without translating to .ps
-Use --savedir flag to create a folder with the .tex file in it
-Essentially does not latex them together
!WARNING, deletes the specified directory if it exists

CURRENT SETUP: From *NIX, 'make-rtf.pl' reads tab seperated lines of files to generate, which calls mod_scigen to create each latex file, then translates to rtf format. Stores these in a folder called 'rtf'. Then from the Windows side run 'rtfsave.pl' which called OLE modules to save an rtf file as a docx. This docx file can then be run through 'mod_md.pl' to spoof the author, date created, etc.

'make-rtf.sh' is a shell script that does similar things to make-rtf.pl
'gen_docs.py' uses pyRTF to build rtf files, but the API isn't great..
