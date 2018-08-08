import sys

count=False
i=0

print "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tBob"
for line in open(sys.argv[1]):


	if line.startswith("Aberrations"):
		count=True
		continue

	if count:
		content=line.strip().split("\t")
		if not "ISCN Notati" in line:
			var_type="DUP"
			if content[1] == "Loss":
				var_type="DEL"
			print("{}\t{}\tSV_{}\tN\t<{}>\t20\tPASS\tEND={}\tGT\t1/1".format(content[7],content[8],i,var_type,content[9]))
			i+=1
