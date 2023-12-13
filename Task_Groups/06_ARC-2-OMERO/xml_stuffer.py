import ome_types
import argparse

def get_arguments():    
    parser = argparse.ArgumentParser(description = "Adds metadata to the unpacked xml.")
    parser.add_argument("xml_path", help = "xml file from omero-cli-tranfer unpack")
    parser.add_argument("omero_project", help = "omero project name")
    parser.add_argument("omero_dataset", help = "omero dataset name")
    args = parser.parse_args()
    return args.xml_path, args.omero_project, args.omero_dataset

if __name__ == "__main__":
    xml_path, omero_project, omero_dataset = get_arguments()
    
    # Read the transfer.xml file as a ome object
    transfer = ome_types.from_xml(xml_path)

    # Add the Project and Dataset to the ome object and link them
    transfer.projects.append(ome_types.model.Project(name = omero_project))
    transfer.datasets.append(ome_types.model.Dataset(name = omero_dataset))
    transfer.projects[0].dataset_refs.append(
        ome_types.model.DatasetRef(id=transfer.datasets[0].id))

    # Link every image in the transfer.xml to the dataset
    for image in transfer.images:
        transfer.datasets[0].image_refs.append(ome_types.model.ImageRef(id=image.id))

    # Convert ome object back to xml and replace the original transfer file
    xml = transfer.to_xml()
    with open(xml_path, 'w') as xml_file:
        xml_file.write(xml)                   





# Important info for OMER
ome.project = isa.study   # Study
ome.Dataset = isa.        # Assay

ome.screen = isa.         # Study
ome.plate  = isa.         # Assay
ome.materials = isa.      # Well

ome.project.owner.Name = isa.          #  Investigation person First Name
ome.project.owner.LastName = isa.      # Investigation person last name
ome.project.owner.Email = isa.         # Investigation person Email

ome.project.owner.institution = isa.   # Investigation person Affiliation

ome.project.name = isa.               # study title
ome.project.description = isa.        # Study Description 

ome.image.id = isa.      # Image ID
ome.image.SizeX = isa.    # Image SizeX
ome.image.SizeY = isa.    # Image SizeY
ome.image.pixel.SizeX = isa. # Image Size X
ome.image.pixel.SizeY = isa. # Imas
ome.image.pixel.SizeZ = isa.
ome.image.pixel.sizeUnit = isa.
