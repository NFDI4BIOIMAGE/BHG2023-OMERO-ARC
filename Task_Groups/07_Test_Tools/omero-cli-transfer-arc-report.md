## Errors and issues with omero-arc plugin.


arc-omero plugin was tested for different cases.

Case 1 : Empty Projects and Datasets and Images.

omero-arc plugin creates an ARC in the local machine as expected.


Case 2 : Projects and Datasets and Images with some random metadata but without ISA fomat and namespaces.

omero-arc plugin creates an ARC in the local machine but without the random metadata (expected).


Case 3 : Projects and Datasets with ISA format and namespaces.

Firstly, there are issues regarding what namespaces to be used exactly.
If the 'Assay Identifier' key is not present in the assay metadata there is an error.
Most of the isa.assay.xlsx file are not containing this key.
We had to add this key manually or using script from MicheleB



In some cases we get the following error
KeyError: 'Assay Identifier'

## The issue is related to the namespaces
## Christoph have certain namespaces and this needs to be discussed.

See Issue github : https://github.com/cmohl2013/omero-arc/issues/3




## Round trip MicheleB script works fine. 
Workflow puts metadata and data to omero but does not download all the metadata (for example performers metadata in the assay)
We are missing some stuff (i.e. metadata) in assay file (performers)
Also in the Christoph's ARC in OMERO there is metadata annotated but we do not get any metadata in the ARC created from OMERO.


See Issue Github : https://github.com/cmohl2013/omero-arc/issues/5


This issue could be caused by mismatched version of Arcommander.

