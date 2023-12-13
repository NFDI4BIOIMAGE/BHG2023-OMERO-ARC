#!/bin/bash
set -euxo pipefail

ISA_INVESTIGATION_PATH=$1
ARC_ASSAY_PATH=$2
OMERO_SERVER=$3
OMERO_USER=$4
OMERO_GROUP=$5
OMERO_PWD=$6

# Login to OMERO, the session is used for all other commands
omero login \
    -s $OMERO_SERVER \
    -u $OMERO_USER \
    -g $OMERO_GROUP \
    -w $OMERO_PWD

# Identify all the images that will be imported and write transfer.xml
omero transfer prepare $ARC_ASSAY_PATH

# Modify the transfer.xml file to add all the annotations extracted from the ARC
python3 metadata_filler.py $ARC_ASSAY_PATH/transfer.xml  $ISA_INVESTIGATION_PATH \
	$ARC_ASSAY_PATH

# Import the images and add all annotations using the modified transfer.xml
omero transfer unpack --folder $ARC_ASSAY_PATH


