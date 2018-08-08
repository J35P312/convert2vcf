import sys

first=True
print "#CHROM\tPOS\ID\tREF\tALT\QUAL\tFILT\tINFO\tFORMAT\tConrad"
for line  in open(sys.argv[1]):
	if first:
		first=False
		continue

	content=line.strip().split("\t")
	var="DUP"
	if content[5] == "loss":
		var="DEL"
	print "{}\t{}\t{}\tN\t<{}>\t.\tPASS\tEND={};SVTYPE={}\tGT\t./1".format(content[1],content[2],content[0],var,content[3],var)
	
