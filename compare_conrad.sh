#first argument: The array file
#secondd argument: Thevcf 

svdb --merge --vcf conrad_del.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
svdb --merge --vcf conrad_dup.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
