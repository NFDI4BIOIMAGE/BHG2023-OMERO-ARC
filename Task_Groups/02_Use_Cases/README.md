# Use Cases

Worked on by: Michele Bortolomeazzi, Eik Dahms, Andrea Schrader, Torsten Stöter, Peter Zentis 


## Mutlimodal imaging ARC: MRI and LightSheet image stacks of Rat brains

Repository: https://git.nfdi4plants.org/torsten.stoeter/rat-mri-ls

* Dataset consists of MRI and LightSheet image stacks of four rats
* LightSheet image has ~4k z slices and 2 channels => many binary files >32k with small size ~8MB
* In total the dataset is large >250GB
* Due to small file size Git-LFS is not used, which blows up .git directory as well
* Each file needs to be annotated in isa.assay.xslx => 32k lines in spreadsheet

