import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

def smiles_to_aromatic(smi):
    try:
        mol = Chem.MolFromSmiles(smi)
        if mol:
            Chem.SetAromaticity(mol)
            return Chem.MolToSmiles(mol, kekuleSmiles=False)
        else:
            return ""
    except:
        return ""

if __name__ == "__main__":
    input_csv = "data_test.csv"
    output_csv = "data_test_aromatic.csv"
    output_folder = "input-structures"

    # Create folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read CSV and convert SMILES
    df = pd.read_csv(input_csv)
    df["Aromatic_SMILE"] = df["SMILES"].apply(smiles_to_aromatic)

    # Save molecule images
    for i, smi in enumerate(df["Aromatic_SMILE"]):
        if smi:  # Only if conversion worked
            mol = Chem.MolFromSmiles(smi)
            if mol:
                img_path = os.path.join(output_folder, f"mol_{i+1}.png")
                Draw.MolToFile(mol, img_path)

    # Save updated CSV
    df.to_csv(output_csv, index=False)

    print(f"✅ Conversion complete. Results saved in {output_csv}")
    print(f"🖼️ Molecule images saved in folder: {output_folder}")

