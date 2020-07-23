# UMI
Unique Molecular Identifiers 


Documentation:

Create a directory with all the sample fastq files.
Also add to this directory a file that has primer sequence information along with locus, chr, genomic position, strand, and anchor sequence. This information will be used to pull the DNA fragment (containing STR sequence) between primer and anchor. 

In UMIscript.py, add the path to this directory to the variable 'directory'. Add primer file name along with path to the variable 'file_primer' in the script.
UMIscript.py uses strfuzzy.py to search for anchor sequence with fuzzines. Default settings allow for fuzziness of a single nucleotide base. This setting can be changed by changing the numeric value of the variable 'fuzz' to desired fuzziness. strfuzzy.py should be in the same directory where UMIscript.py is located.  

UMIscript.py will loop through all the fastq files and create output files with information about locus, DNA fragment (containing STR sequence), UMI sequence, respective primer and anchor sequence, and the count of DNA fragment.
