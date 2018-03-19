## Introduction

This is a pipeline for analysing exom capture data to call SNPs. The master control script is a python script and the main analysis pipeline is written in ruby/rake programming lanugage.

## Requirements

1) python2 or python3
2) ruby/rake
3) FASTQC (for Quality check)
4) Trimmomatic (for quality trimming)
5) bbmap (for mapping)
6) samtools
7) bcftools (for SNP call)

## Usage:

1) python exome_capture_analysis.py path-to-dir-where-all-input-files-exist reference_sequence
2) python exome_capture_analysis.py /tsl/data/reads/two_blades/exome_capture_field_samples_jan2018/exome_capture/samples/raw/ reference.fasta

