#!/bin/bash

ARC_ASSAY_PATH=$1
OMERO_SERVER=$2
OMERO_USER=$3
OMERO_GROUP=$4
OMERO_PWD=$5
OMERO_PROJECT=$6
OMERO_DATASET=$7

omero login \
    -s $OMERO_SERVER \
    -u $OMERO_USER \
    -g $OMERO_GROUP \
    -w $OMERO_PWD

omero transfer prepare $ARC_ASSAY_PATH
python3 xml_stuffer.py $ARC_ASSAY_PATH/transfer.xml $OMERO_PROJECT $OMERO_DATASET
omero transfer unpack --folder $ARC_ASSAY_PATH


