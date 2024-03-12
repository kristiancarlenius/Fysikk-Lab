filename = "t8.txt"
with open(filename) as fin, open('N'+filename, 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ';'))