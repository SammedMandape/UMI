<!-- PROJECT TITLE -->
# Unique Molecular Identifiers (UMIs)
UMIs for mixture interpretation

<!-- TABLE OF CONTENTS -->
## Table of contents
* [Introduction](#introduction)
* [Quick start](#quick-start)
* [Overview of algorithm](#overview-of-algorithm)
* [Funding](#funding)


<!-- Introduction -->
## Introduction
The scripts are used to extract the DNA fragments containing STR sequence between gene specific primer and anchor sequence from paired-end fastq files. The DNA fragment composition is shown in figure 1. The 11 nucleotide (nt) long common sequence (CS) was used as a marker to identify the 12nt long UMI sequence from read2.

<p align="center">
<img src="images/DNAfragComp.png" alt="Image">
<p style="text-align: center;"><strong>Figure 1. </strong> An illustration of QIAseq DNA fragment composition. Read1 is in the order of locus-specific primer -> targeted DNA sequence -> common sequence in all reads -> unique molecular identifier while read2 begins with UMI followed by CS and targeted DNA sequence.
</p>


<!-- Quick start -->
## Quick start  
* Clone this repository and cd into the directory
```bash
git clone https://github.com/SammedMandape/UMI.git
cd UMI
```

* Create a data directory and copy paired-end fastq files for all samples
* Create a tab separated file named "PrimedAnchors.txt" with information (in the same order as mentioned) about all loci, and their respective chromosome, genomic start position, strand (0 or 1), primer sequence, and anchor sequence
* Save and run the python script
```bash
/usr/bin/python3 UMIscript.py
```

* UMIscript.py will loop through all the fastq files and create output files in the same directory with information about locus, and their respective DNA fragment (containing STR sequence), UMI sequence, primer, anchor sequence, and the count of DNA fragment.


<!-- Overview of algorithm -->
## Overview of algorithm
UMIscript.py, along with fastq files and PrimedAnchors.txt as inputs, uses python script strfuzzy.py by [Benjamin Crysup](https://github.com/Benjamin-Crysup). strfuzzy searches for anchor sequence with fuzziness. Default setting allow for one mismatch when searching for anchor sequence. This setting can be changed by varying the variable 'fuzz' in UMIscript to desired number of mismatches allowed when searching for anchor sequence (the line of code is shown below). Flowchart describing the python implementation is represented in figure 2.

> anchorIndex = strfuzzy.fuzzyFind(readR1, anchor, fuzz=\<numeric value of desired fuzziness\>)

<p align="center">
<img src="images/Algo_flowchart.jpg" alt="Image">
<p style="text-align: center;"><strong>Figure 2. </strong> A representation of implementation of python script UMIscript.py. The inputs to this script are paired-end fastq files (read1, read2) and primer file(locus, chr, pos, strand, primer sequence, anchor sequence). The outputs are files for each sample with information about the targeted DNA sequence for a locus-specific primer along with respective UMI, anchor, and count.
</p>
</p>

## Funding
