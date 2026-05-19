# Go_Enrichment
All files obtained during class practicals

**script.py**: converts human_gene_annotation.tsv into the bed file, by filtering out irrelevant names and then rearranging data.

**human_gene_annotation.bed**: bed file consisting of filtered data 

**extended.bed**: obtained by running bedtools slop on previous file (w/ hg38.chrom.sizes), to extend regions by 500bp according to + or -

**promoterSeq.7z**: obtained by running bedtools getfasta on previous file (w/ hg38.fa), to get all the sequences for us to search our motif in (compressed because full file is too big to upload)

**dreg_hits.txt**: obtained by running dreg with the seqs above on the pattern "GCGC..GCGC". This file may be incomplete as it was taking very long to run on my system
