the steps for the RDKIT test:

- Reads a CSV file (smiles.csv) with system names and SMILES strings.
- Converts each SMILES into a molecule using RDKit.
- Calculates basic molecular descriptors (molecular weight, logP, TPSA, aromatic rings, H-bond donors/acceptors, valence electrons, IPC).
- Saves all results into a new file rdkit_features.csv.
