# ARC2OMERO

ARC2OMERO imports an ARC assay to OMERO.

## Workflow
The tool uses omero-cli-tranfer to identify the images to import and import them, \
as well as making the project, dataset and other annotations.
The workflow is:
+ 1) Login to OMERO
+ 2) `omero transfer prepare` identifies the image to import and creates a tranfer.xml file in the dataset folder.
+ 3) `metadata_filler.py` reads the metadata from the xlsx files for the investigation and the study, and converts them into new annotations in the transfer.xml file.
+ 4) `omero transfer unpack` imports the images into OMERO and creates the annotations specified in the transfer.xml file.

In this prototype the workflow is packaged in the `workflow.sh` script.

## Prototype

### Usage
`workflow.sh` takes the following positional arguments:
+ 1) ISA_INVESTIGATION_PATH = Path to the isa.investigation.xlsx file
+ 2) ARC_ASSAY_PATH = Path to the dataset folder of the assay to import
+ 3) OMERO_SERVER = OMERO server address (assumes port = 4064)
+ 4) OMERO_USER = OMERO user which will be the owner of images + annotations 
+ 5) OMERO_GROUP = OMERO group where the data will be deposited 
+ 6) OMERO_PWD = Password for the OMERO user

### TO DO
- Finish adding all metadata for investigation, study, assay.
- Plate, screen, well format.
- What if the project / dataset already exist?
- Remove transfer.xml from the ARC.

