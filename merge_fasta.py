nb_file = 4
out = open("/home/julie/Documents/Protein_Localisation_ML/data/Predictions_signalIP5/signalIP5_preds.txt", "w")
out.write('ID	Prediction	SP(Sec/SPI)	OTHER	CS Position\n')
for i in range(nb_file+1):
    fin = "/home/julie/Documents/Protein_Localisation_ML/data/Predictions_signalIP5/output_protein_type_%d.txt" % (i)
    print(fin)
    with open(fin, 'r') as f:
        for line in f:
            if line[0] != '#':
                out.write(line)
out.close()