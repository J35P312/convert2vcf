#first argument: The array file
#secondd argument: Thevcf 

svdb --merge --vcf dgv_COMPLEX.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
svdb --merge --vcf dgv_DEL.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
svdb --merge --vcf dgv_DUP.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
svdb --merge --vcf dgv_INS.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
svdb --merge --vcf dgv_INV.vcf $1 --no_intra --bnd_distance 100000 --overlap 0.4 --no_var | grep "set=Intersection	" | wc -l
