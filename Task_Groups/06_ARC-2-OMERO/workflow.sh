#!/bin/bash
set -euxo pipefail

ARC_ASSAY_PATH=$1
OMERO_SERVER=$2
OMERO_USER=$3
OMERO_GROUP=$4
OMERO_PWD=$5
OMERO_PROJECT=$6
OMERO_DATASET=$7

# Login to OMERO, the session is used for all other commands
omero login \
    -s $OMERO_SERVER \
    -u $OMERO_USER \
    -g $OMERO_GROUP \
    -w $OMERO_PWD

# Identify all the images that will be imported and write transfer.xml
omero transfer prepare $ARC_ASSAY_PATH

# Modify the transfer.xml file to add all the annotations extracted from the ARC
python3 xml_stuffer.py $ARC_ASSAY_PATH/transfer.xml $OMERO_PROJECT $OMERO_DATASET

# Import the images and add all annotations using the modified transfer.xml
omero transfer unpack --folder $ARC_ASSAY_PATH


