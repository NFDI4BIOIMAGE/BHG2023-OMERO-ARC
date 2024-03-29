import ome_types
import argparse
import pandas as pd

def get_arguments():    
    parser = argparse.ArgumentParser(description = "Adds metadata to the unpacked xml.")
    parser.add_argument("xml_path", help = "xml file from omero-cli-tranfer unpack")
    parser.add_argument("investigation_path", help = "isa investigation xlsx file")
    parser.add_argument("assay_path", help = "path to the assay folder")
    args = parser.parse_args()
    return args.xml_path, args.investigation_path, args.assay_path

if __name__ == "__main__":
    xml_path, isa_investigation_path, assay_path= get_arguments()
    
    # Read the transfer.xml file
    transfer = ome_types.from_xml(xml_path)

    # Read the isa investigation file and use "" for empty values
    investigation = pd.read_excel(isa_investigation_path, header=None, dtype = str)
    investigation = investigation.fillna("")
    investigation = dict(zip(investigation[0], investigation[1]))

    # Create project and dataset and link the dataset to the project
    transfer.projects.append(
            ome_types.model.Project(name = investigation["Study Identifier"],
                description = investigation["Study Description"]))
    transfer.datasets.append(
            ome_types.model.Dataset(name = assay_path.split("/")[-3]))
    transfer.projects[0].dataset_refs.append(
        ome_types.model.DatasetRef(id=transfer.datasets[0].id))
    transfer.projects[0].annotation_refs = []

    # Annotate the project with Key-Value pairs divided in namespaces
    owner_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:INVESTIGATION:INVESTIGATION CONTACTS",
            value = {"ms" : [{"k" : "Investigation Person First Name",
                "value" : investigation["Investigation Person First Name"]},
                {"k" : "Investigation Person Last Name",
                    "value" : investigation["Investigation Person Last Name"]},
                {"k" : "Investigation Person Email",
                    "value" : investigation["Investigation Person Email"]},
                {"k" : "Investigation Person Address",
                    "value" : investigation["Investigation Person Address"]},
                {"k" : "Investigation Person Affiliation",
                    "value" : investigation["Investigation Person Affiliation"]}]})
    transfer.structured_annotations.append(owner_details)
    transfer.projects[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=owner_details.id))

    protocol_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:STUDY:STUDY PROTOCOLS",
            value = {"ms" : [{"k" : "Study Protocol Name",
                "value" : investigation["Study Protocol Name"]},
                {"k" : "Study Protocol Type",
                    "value" : investigation["Study Protocol Type"]},
                {"k" : "Study Protocol Description",
                    "value" : investigation["Study Protocol Description"]},
                {"k" : "Study Protocol Components Name",
                    "value" : investigation["Study Protocol Components Name"]},
                {"k" : "Study Protocol Components Type",
                    "value" : investigation["Study Protocol Components Type"]}]})
    transfer.structured_annotations.append(protocol_details)
    transfer.projects[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=protocol_details.id))

    publication_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:INVESTIGATION:INVESTIGATION PUBLICATIONS",
            value = {"ms" : [{"k" : "Investigation Publication DOI",
                "value" : investigation["Investigation Publication DOI"]},
                {"k" : "Investigation Publication PubMed ID",
                    "value" : investigation["Investigation Publication PubMed ID"]},
                {"k" : "Investigation Publication Author List",
                    "value" : investigation["Investigation Publication Author List"]},
                {"k" : "Investigation Publication Title",
                    "value" : investigation["Investigation Publication Title"]},
                {"k" : "Investigation Publication Status",
                    "value" : investigation["Investigation Publication Status"]}]})
    transfer.structured_annotations.append(publication_details)
    transfer.projects[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=publication_details.id))

    
    # Read isa.assay.xlsx, and set empy values to "".
    # Here we need to process multiple excel column for the values
    isa_assay_path = "/".join(assay_path.split("/")[:-2]) + "/isa.assay.xlsx"
    assay = pd.read_excel(isa_assay_path, header=None, sheet_name="Assay", dtype = str)
    assay = assay.fillna("")
    assay_cols = []
    for i in assay.columns[1:]:
        assay_cols.append(dict(zip(assay[0], assay[i])))

    # Annotate the dataset with Key-Value pairs divided in namespaces
    for assay_col in assay_cols:
        assay_performer_details = ome_types.model.MapAnnotation(
                namespace = "ARC:ISA:ASSAY:ASSAY PERFORMER",
                value = {"ms" : [{"k" : "Last Name",
                    "value" : assay_col["Last Name"]},
                    {"k" : "First Name",
                        "value" : assay_col["First Name"]},
                    {"k" : "Email",
                        "value" : assay_col["Email"]},
                    {"k" : "Address",
                        "value" : assay_col["Address"]},
                    {"k" : "Roles",
                        "value" : assay_col["Roles"]},
                    {"k" : "Affiliation",
                        "value" : assay_col["Affiliation"]}]})
        transfer.structured_annotations.append(assay_performer_details)
        transfer.datasets[0].annotation_refs.append(
                ome_types.model.AnnotationRef(id=assay_performer_details.id))

    assay_metadata_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:ASSAY:ASSAY METADATA",
            value = {"ms" : [{"k" : "Assay Identifier",
                    "value" : assay_cols[0]["Assay Identifier"]},
                {"k" : "Measurement Type",
                    "value" : assay_cols[0]["Measurement Type"]},
                {"k" : "Measurement Type Term Accession Number",
                    "value" : assay_cols[0]["Measurement Type Term Accession Number"]},
                {"k" : "Technology Type",
                    "value" : assay_cols[0]["Technology Type"]},
                {"k" : "Technology Platform",
                    "value" : assay_cols[0]["Technology Platform"]}]})
    transfer.structured_annotations.append(assay_metadata_details)
    transfer.datasets[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=assay_metadata_details.id))

    # Link every image in the transfer.xml to the dataset
    for image in transfer.images:
        transfer.datasets[0].image_refs.append(ome_types.model.ImageRef(id=image.id))

    # Convert ome object back to xml and replace the original transfer file
    xml = transfer.to_xml()
    with open(xml_path, 'w') as xml_file:
        xml_file.write(xml)                   

