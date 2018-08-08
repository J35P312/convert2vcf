grep "<DEL>" $1 | wc -l
grep -E "<TDUP>|<DUP>|<DUP:TANDEM>" $1 | wc -l
grep -v "#" $1 | wc -l
grep "<INS>" $1 | wc -l
grep -v "	<" $1 | grep -v "#" | wc -l
grep "<INV>" $1 | wc -l
grep "<UNK>" $1 | wc -l
