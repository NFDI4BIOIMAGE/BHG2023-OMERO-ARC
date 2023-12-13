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

    transfer = ome_types.from_xml(xml_path)
    investigation = pd.read_excel(isa_investigation_path, header=None)
    investigation = dict(zip(investigation[0], investigation[1]))

    transfer.projects.append(
            ome_types.model.Project(name = investigation["Study Identifier"],
                description = investigation["Study Description"]))
    transfer.datasets.append(
            ome_types.model.Dataset(name = assay_path.split("/")[-3]))
    transfer.projects[0].dataset_refs.append(
        ome_types.model.DatasetRef(id=transfer.datasets[0].id))
    transfer.projects[0].annotation_refs = []

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

    isa_assay_path = "/".join(assay_path.split("/")[:-2]) + "/isa.assay.xlsx"
    assay = pd.read_excel(isa_assay_path, header=None, sheet_name="Assay")
    assay = dict(zip(assay[0], assay[1]))

    assay_metadata_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:ASSAY:ASSAY METADATA",
            value = {"ms" : [{"k" : "Measurement Type",
                "value" : assay["Measurement Type"]},
                {"k" : "Measurement Type Term Accession Number",
                    "value" : assay["Measurement Type Term Accession Number"]},
                {"k" : "Technology Type",
                    "value" : assay["Technology Type"]},
                {"k" : "Technology Platform",
                    "value" : assay["Technology Platform"]}]})
    transfer.structured_annotations.append(assay_metadata_details)
    transfer.datasets[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=assay_metadata_details.id))

    assay_performer_details = ome_types.model.MapAnnotation(
            namespace = "ARC:ISA:ASSAY:ASSAY PERFORMER",
            value = {"ms" : [{"k" : "Last Name",
                "value" : assay["Last Name"]},
                {"k" : "First Name",
                    "value" : assay["First Name"]},
                {"k" : "Email",
                    "value" : assay["Email"]},
                {"k" : "Address",
                    "value" : assay["Address"]},
                {"k" : "Roles",
                    "value" : assay["Roles"]},
                {"k" : "Affiliation",
                    "value" : assay["Affiliation"]}]})
    transfer.structured_annotations.append(assay_performer_details)
    transfer.datasets[0].annotation_refs.append(
            ome_types.model.AnnotationRef(id=assay_performer_details.id))

    # Link every image in the transfer.xml to the dataset
    for image in transfer.images:
        transfer.datasets[0].image_refs.append(ome_types.model.ImageRef(id=image.id))

    # Convert ome object back to xml and replace the original transfer file
    xml = transfer.to_xml()
    with open(xml_path, 'w') as xml_file:
        xml_file.write(xml)                   


    #ome.screen = investigation["Study Identifier"]         # Study
    #ome.plate  = assay_path.split("/")[-2]         # Assay
    #ome.materials = isa.      # Well


    #ome.project.owner.institution = isa.   # Investigation person Affiliation

    #ome.project.name = isa.               # study title
    #ome.project.description = isa.        # Study Description 

    #ome.image.id = isa.      # Image ID
    #ome.image.SizeX = isa.    # Image SizeX
    #ome.image.SizeY = isa.    # Image SizeY
    #ome.image.pixel.SizeX = isa. # Image Size X
    #ome.image.pixel.SizeY = isa. # Imas
    #ome.image.pixel.SizeZ = isa.
    #ome.image.pixel.sizeUnit = isa.
