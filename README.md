### sequence-design-guide
Protocol to redesign enzyme sequences with ProteinMPNN followed in Krasnow et. al. 2025

## Section I: generate residue constraints

# Distance analysis for active site constraints

This step will analyze the structure of your protein and measure the distance from each residue to the active site, generating list of constrained residues below a specified distance cutoff. Since it is likely that no structure of your protein has been solved in complex with substrate, the script is written to do the distance measurements on a homolog bound to substrate and map the constrained residues to your target protein. You can use a substrate-bound structure of the target protein if one is available or an AlphaFold3 model if you trust it.

Required software: 
•	distance_constraint_analysis.ipynb (Google Colab Notebook)

1.	Find a homolog of your target protein that is closely related in structure and has a structure solved with the substrate bound, or generate an AF3 structure. Download the pdb file of this substrate-bound structure.
2.	Create a folder in your Google Drive home directory titled ‘pdbs’. Upload the pdb file of the pdb of the homolog with substrate bound into this folder.
3.	Create a pairwise alignment between your protein sequence and the homolog protein sequence (this can be done in Geneious). The homolog should be the first sequence and the target protein should be the second. Export the alignment in .fasta format.
4.	Create a folder in your Google Drive home directory titled ‘fastas’. Upload the .fasta alignment from step 2.
5.	Upload the Colab notebook to your ‘Colab Notebooks’ folder to your Drive home directory.
6.	Run all the cells in the Colab Notebook one at a time, following instructions in the file as indicated in the text. Comments are provided to explain code and provide warnings for potential changes needed for different situations that weren't encounted in this paper. 
