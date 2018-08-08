import sys,re

kb=0
tkb=0
hkb=0
lhkb=0

for line in open(sys.argv[1]):
        if line[0] =="#":
                continue
        content=line.strip().split("\t")

        if "SVLEN=" in line:
          length=abs(int(line.split("SVLEN=")[-1].split(";")[0]))
          if length < 1000:
                kb+=1
          elif length < 10000:
                tkb+=1

          elif length < 100000:
                 hkb+=1
          else:
                 lhkb+=1

        elif not "<" in line:
          B=content[4]
          
          B=re.split("[],[]",B)
          lst=[]
          for entry in B:
              if ":" in entry:
                  lst=entry.split(":")
          chrB=lst[0]
          if not chrB == content[0]:
                continue
          pos=int(lst[1])
          length=abs(pos-int(content[1])+1)

          if length < 1000:
                kb+=1
          elif length < 10000:
                tkb+=1

          elif length < 100000:
                 hkb+=1
          else:
                 lhkb+=1
        
		



print kb
print tkb
print hkb
print lhkb
