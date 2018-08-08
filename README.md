# convert2VC

a collection fo scripts for converting various databases into vcf file. All scripts require python 2.7

# Conrad2vcf

Covert the CNV list of "Origins and functional impact of copy number variation in the human genome" into a vcf file. Download the list of variants from this  link: https://media.nature.com/original/nature-assets/nature/journal/v464/n7289/extref/nature08516-s3.xls

The excel file needs to be converted into a tab separated file.

then run the script: 

	python Conrad2vcf.py input.txt > output.vcf

# DGV2vcf

Convert the DGV database file into vcf, the database may be downloaded through this link: http://dgv.tcag.ca/dgv/docs/GRCh37_hg19_variants_2016-05-15.txt

command:
	
	python DGV2vcf.py input.txt > output.vcf

# array2vcf

Convert OGH cgh files into vcf:

	python array2vcf.py input.txt > output.vcf
