#!/usr/bin/env python

import os, sys, re
#dir_path_to_data="/tsl/data/reads/two_blades/exome_capture_field_samples_jan2018/exome_capture/samples/raw/"
#dir_path_to_data="/usr/users/TSL_20/shrestha/workarea/yogesh/exome_capure/testfolder/"
dir_path_to_data=sys.argv[1]
reference=sys.argv[2]

data_files=os.listdir(dir_path_to_data)

sample_set=set()
for data in  data_files:
    match=re.search('(.*)_L\d_\d.fq.gz', data)
    if match:
        sample_set.add(match.group(1))


for sample in sample_set:
    cmd1="source ruby-2.3.1; rake -f rakefile projectdir=/usr/users/TSL_20/shrestha/workarea/yogesh/exome_capure  sampleid=" + sample + " R1=" + dir_path_to_data + "/" + sample + "_L1_1.fq.gz" + " reference=" + reference + " R2=" + dir_path_to_data + "/" + sample + "_L1_2.fq.gz" + " trimmomatic:run bbmap:run"
    cmd2=cmd1.replace("_L1_", "_L2_")
    varscan_cmd="rake -f rakefile projectdir=/usr/users/TSL_20/shrestha/workarea/yogesh/exome_capure  sampleid=" + sample + " reference=" + reference + " bcftools:run"
    os.system('sbatch --mem 10G -o ' + sample + '.rakelog ' + ' -J ' + sample + ' --wrap ' + '\"' + cmd1 + "; " + cmd2 + "; " + varscan_cmd + '\"')
    #print "rake --projectdir="."  R1=" + dir_path_to_data + data + "_L2_1.fq.gz" + " R2=" + dir_path_to_data + data + "_L2_2.fq.gz" + " reference=/usr/users/sl/guptay/field_samples/exome_capture/sequence_bait_unique.fasta trimmomatic:run "


exit(0)
