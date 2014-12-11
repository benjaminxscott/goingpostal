#!/usr/bin/perl -w

use strict;
use warnings;
use Cwd;
use feature 'say';

#TODO handle profiles (e.g. refer to different grammars in make-latex)
my $prevdir = getcwd;
my $repo = "$prevdir/out";
my $usage="Usage: $0 < tab_sep_list in form: title" .'\t'."author\nReads lines of files to gen from STDIN\n";
my ($title, $author) = "";
my $delim = '\t';

#redirect stderr

die $usage if (defined shift);
open(*STDERR, '>', "/dev/null") or die "ERROR: couldn't redir stderr";

#check if rtf repo exists
if (! -d $repo)
{
	say "making $repo";
	system("mkdir $repo");
}

#read lines from stdin
while (<>)
{
#create rtf based on line (Title\tAuthor)
	if ($_ ~~ /(\w+)+$delim(\w+)+/)
	{
		($title, $author) = split ($delim, $_);
		say "Creating $title with $author...";
		&genrtf($title, $author);
	}
	else { say "Line $. was not processed due to bad format"};
}

sub genrtf()
{
	my $prevdir = getcwd;
	my $scigen="/home/ben/mitre/honeynet/mod_scigen";
	my $tmp="/tmp/make-rtf";
	my ($title, $author) = @_;

#get the first word of title
	my ($filename) = $title =~ /(\w+)/;

#make TEX file
	chdir $scigen;
	system("./make-latex.pl --savedir $tmp"
			." --title \"$title\" " 
			." --author \"$author\" 1>/dev/null ");
	chdir $tmp;
#create the RTF file
	system("latex *.tex 1>/dev/null");
	system("latex2rtf *.tex");
	system("cp *.rtf $prevdir/rtf/$filename.rtf");
	chdir $prevdir;

}
