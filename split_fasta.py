import gzip
max_prot=5000
nb_prot = 0
with gzip.open("/home/julie/Documents/Protein_Localisation_ML/data/UP000005640.fasta.gz", 'rt') as fin:
    fout = open("/home/julie/Documents/Protein_Localisation_ML/data/split_genome_0.fasta","w")
    file_nb = 1
    for i,line in enumerate(fin):
        if line[0] == ">":
            nb_prot +=1
        if nb_prot > max_prot:
            nb_prot = 1
            fout.close()
            fout = open("/home/julie/Documents/Protein_Localisation_ML/data/split_genome_%d.fasta" % (file_nb), "w")
            file_nb += 1

        fout.write(line)
    fout.close()