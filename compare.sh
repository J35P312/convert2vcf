#first argument: The array file
#secondd argument: Thevcf 

svdb --merge --vcf $1 $2 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
