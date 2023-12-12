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

project_id=$(omero obj new Project name=$OMERO_DATASET)
dataset_id=$(omero obj new Dataset name=$OMERO_PROJECT)
omero obj new ProjectDatasetLink parent=$project_id child=$dataset_id

omero transfer prepare $ARC_ASSAY_PATH
omero transfer unpack --folder $ARC_ASSAY_PATH

