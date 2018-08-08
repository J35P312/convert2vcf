import sys
first=True
print "#CHROM\tPOS\ID\tREF\tALT\QUAL\tFILT\tINFO\tFORMAT\tConrad"
for line  in open(sys.argv[1]):
	if first:
		first=False
		continue

	content=line.strip().split("\t")
	var=content[5]
	if var == "CNV":
		continue
	elif content[5] == "deletion":
		var="DEL"
	elif content[5] == "loss":
		var="DEL"
	elif content[5] == "duplication":
		var="DUP"
	elif content[5] == "gain":
		var="DUP"

	elif content[5] == "insertion":
		var="INS"
	elif content[5] == "novel sequence insertion":
		var="INS"

	elif content[5] == "inversion":
		var="INV"
	elif content[5] == "tandem duplication":
		var="DUP"
	elif content[5] == "complex":
		var="COMPLEX"
	else:
		continue
	
	print "{}\t{}\t{}\tN\t<{}>\t.\tPASS\tEND={};SVTYPE={}\tGT\t./1".format(content[1],content[2],content[0],var,content[3],var)
