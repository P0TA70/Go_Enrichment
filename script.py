import sys
chrom_dict = {str(i): i for i in range(1,23)}
chrom_dict["X"] = 23
chrom_dict["Y"] = 24

for line in sys.stdin:
    l_items = line.split("\n")[0].split("\t")
    if l_items[4] in chrom_dict:
        number = int(l_items[7])+1
        print(f"chr{l_items[4]}\t{l_items[7]}\t{number}\tchr{l_items[4]}@{l_items[7]}-{number}|{l_items[6]}\t.\t{'+' if int(l_items[5])==1 else '-'}")
