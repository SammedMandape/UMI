<!-- PROJECT TITLE -->
# UMI (Unique Molecular Identifiers)
UMIs for mixture interpretation

<!-- TABLE OF CONTENTS -->
## Table of contents
* [Introduction](#introduction)
* [Usage](#usage)

<!-- Introduction -->
## Introduction
The scripts are used to extract the DNA fragments containing STR sequence between gene specific primer and anchor sequence from paired-end fastq files. The DNA fragment composition is shown in figure 1. The 11 nucleotide (nt) long common sequence (CS) was used as a marker to identify the 12nt long UMI sequence from read2.

<p align="center">
<img src="images/DNAfragComp.png" alt="Image" width="385" height="265">
</p>



<!-- Usage -->
## Usage

* Create a directory with all the sample fastq files.
* To this directory add a file that has primer sequence information along with locus, chr, genomic position, strand, and anchor sequence. This information will be used to pull the DNA fragment (containing STR sequence) between primer and anchor.

* Add path of this directory to the variable 'directory' in UMIscript.py
> directory = "path/of/directory/of/fastq/files"

* 

In UMIscript.py, add the path to this directory to the variable 'directory'. Add primer file name along with path to the variable 'file_primer' in the script.
UMIscript.py uses strfuzzy.py to search for anchor sequence with fuzzines. Default settings allow for fuzziness of a single nucleotide base. This setting can be changed by changing the numeric value of the variable 'fuzz' to desired fuzziness (the line of code is shown below). strfuzzy.py should be in the same directory where UMIscript.py is located.  

> anchorIndex = strfuzzy.fuzzyFind(readR1, anchor, fuzz=<numeric value of desired fuzziness>)

UMIscript.py will loop through all the fastq files and create output files with information about locus, DNA fragment (containing STR sequence), UMI sequence, respective primer and anchor sequence, and the count of DNA fragment.
