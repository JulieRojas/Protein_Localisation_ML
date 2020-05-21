import gzip
import csv


def read_fasta(filename):
    fasta_dict = {}
    with gzip.open(filename, 'rt') as file:
        name = ""
        seq = ""
        seq_list = []
        for line in file:
            if line[0] == ">":
                if name != "":
                    fasta_dict[name] = seq
                seq = ""
                name = line.split('|')[1]
            else:
                seq += line.rstrip()
        fasta_dict[name] = seq
    return fasta_dict

dict= read_fasta("data/UP000000589.fasta.gz")

def database_maker(map_file):
    with open(map_file, 'r') as csv_file:
        table = csv.reader(csv_file, delimiter="\t")
        lead_prot_id = ""
        Compartment = ""
        Confidence = ""
        Global_class = ""
        Sequence = ""
        My_data = []
        missing = []
        for l in table:
            lead_prot_id = l[1]
            Compartment = l[5]
            Confidence = l[7]
            Global_class = l[8]
            if lead_prot_id == "Canonical lead protein ID":
                Sequence = 'Sequence'
            else:
                if '-' in lead_prot_id:
                    lead_prot_id = lead_prot_id.split('-')[0]
                if lead_prot_id in dict:
                    Sequence = dict[lead_prot_id]
                else:
                    missing.append(lead_prot_id)
            # if no prediction, we don't include them in the dataset
            if Compartment != "" or Global_class != "":
                My_data.append([lead_prot_id, Compartment, Confidence, Global_class, Sequence])

        #print(missing)
        print(len(missing))
        print(len(My_data))
    return(My_data)

rows = database_maker('data/mouse_neuron.csv')

with open('data/Dataset.csv', 'w') as dataset:
    writer = csv.writer(dataset, delimiter='\t')
    writer.writerows(rows)
