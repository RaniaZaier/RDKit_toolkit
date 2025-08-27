the steps for the RDKIT test:

1- Reads a CSV file (smiles.csv) with system names and SMILES strings.

2- Converts each SMILES into a molecule using RDKit.

3- Calculates basic molecular descriptors (molecular weight, logP, TPSA, aromatic rings, H-bond donors/acceptors, valence electrons, IPC).

4- Saves all results into a new file rdkit_features.csv.
