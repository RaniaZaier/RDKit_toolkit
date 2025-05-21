from rdkit import Chem
from rdkit.Chem import Descriptors
import csv

input_file = "smiles.csv"
output_file = "rdkit_features.csv"

try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        # Automatically detect delimiter
        dialect = csv.Sniffer().sniff(infile.read(1024))
        #Re-read the file from beginning after defining the dialect
        infile.seek(0)

        reader = csv.reader(infile, dialect)
        headers = next(reader)

        output=[]
        for row in reader:
            system, smiles = row[0].strip(), row[1].strip()
            print(system, smiles)
            mol = Chem.MolFromSmiles(smiles)

            try:
                output.append([
                    system,
                    smiles,
                    round(Descriptors.MolWt(mol), 2),
                    round(Descriptors.MolLogP(mol), 2),
                    round(Descriptors.TPSA(mol), 2),
                    Descriptors.NumAromaticRings(mol),
                    Descriptors.NumHAcceptors(mol),
                    Descriptors.NumHDonors(mol),
                    Descriptors.NumValenceElectrons(mol),
                    round(Descriptors.Ipc(mol), 2)
                ])
                print(f"Processed: {system}")

            except Exception as e:
                print("Something went wrong")

    if output:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['system', 'smiles', 'MolWt', 'MolLogP', 'TPSA',
                             'NumAromaticRings', 'HAcceptor', 'HDonor', 'ValElect', 'IPC'])
            writer.writerows(output)
        print(f"file {output_file} generated with {len(output)} molecules.")
    else:
        print("No valid data found.")

except Exception as e:
    print("ERROR")
