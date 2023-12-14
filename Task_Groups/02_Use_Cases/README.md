# Use Cases

Worked on by: Michele Bortolomeazzi, Eik Dahms, Andrea Schrader, Torsten Stöter, Peter Zentis 


## Mutlimodal imaging ARC: MRI and LightSheet image stacks of Rat brains

Repository: https://git.nfdi4plants.org/torsten.stoeter/rat-mri-ls

* Dataset consists of MRI and LightSheet image stacks of four rats
* LightSheet image has ~4k z slices and 2 channels => many binary files >32k with small size ~8MB
* In total the dataset is large >250GB
* Due to small file size Git-LFS is not used, which blows up .git directory as well
* Each file needs to be annotated in isa.assay.xslx => 32k lines in spreadsheet


## Vendor specific image container

* in this case Leica LIF files contain many images, i.e. different measurements with different parameters (samples, specimen, cultures, channels, ...)
* this is a problem with respect to file based metadata annotation as done in ARC
* therefore ARC specs encourage accompanying open formats besides raw data => data duplication or alternatively workflows for conversion
* possible solution use vendor software for data conversion and processing
* BUT: important technical metadata maybe lost (example: pixel sizes for maximum intensity projections in Leica software)
* alternative workflow: use OMERO for understanding vendor specific file formats and image extraction (1->N) and perform MIP in OMERO with results moved back into ARC
