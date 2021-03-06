#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO
import argparse
import os
from sklearn import metrics
from collections import OrderedDict

def bin_output(b,l):
    contig_names_bin = []
    file_names = []
    for filename in os.listdir(b):
        file_names.append(str(filename))
        if any((files.endswith(l)) for files in file_names):
                for record in SeqIO.parse(os.path.join(b,filename), "fasta"):
                    contig_names_bin.append(record.id)
        else:
            print "No file's with this Suffix exist in this directory: " , b
                
        
    new_ = dict(zip(contig_names_bin, file_names))
    files_sorted = []
    od = dict(OrderedDict(sorted(new_.items())))
    for key , value in od.iteritems():
        files_sorted.append(value)
    return files_sorted
    

def ari(a,b):
    print "------------------------------------------------------------------------------------"
    print "Adjusted-Rand-Index: " , metrics.adjusted_rand_score(a,b)
    print "Homogeneity, completeness, V-measure: " , metrics.homogeneity_completeness_v_measure(a,b)
    
           
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bin_evaluation.py', usage='%(prog)s -b Putative Genomes -r reference genomes -l suffix of fasta files')
    parser.add_argument("-b", dest="inputPutative", help="Specify the directory containing Putative genomes")
    parser.add_argument("-r", dest="inputreference", help="Specify directory containing reference genomes")
    parser.add_argument("-l", dest="inputSuffix", help="specify suffix of bins e.g .fa, .fna, .fasta, etc.")

    args = parser.parse_args()
    
    if args.inputPutative is None:
        print "Need to specify directory containing putative genomes"
        parser.print_help()
    elif args.inputreference is None:
        print "Need to specify directory containing reference genomes"
        parser.print_help()
    elif args.inputSuffix is None:
        print "Need to specify Suffix linking putative genomes/reference genomes"
        parser.print_help()
            
    
    
    else: 
        val1 = bin_output(args.inputPutative, args.inputSuffix)
        val2 = bin_output(args.inputreference, args.inputSuffix)
        ari(val2,val1)
        