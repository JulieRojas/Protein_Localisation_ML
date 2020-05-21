import gzip

with gzip.open("data/UP000005640.fasta.gz", 'rt') as file, open('data/noU_genome.fasta', 'w') as file_new:
    for line in file:
        seq = ""
        if line[0] == ">":
            file_new.write(line)
            seq = ""
        else:
            file_new.write(line.replace("U","C"))

