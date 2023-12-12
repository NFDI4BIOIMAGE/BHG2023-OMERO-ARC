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

    transfer = ome_types.from_xml(xml_path)

    transfer.projects.append(ome_types.model.Project(name = omero_project))
    transfer.datasets.append(ome_types.model.Dataset(name = omero_dataset))
    transfer.projects[0].dataset_refs.append(
        ome_types.model.DatasetRef(id=transfer.datasets[0].id))

    for image in transfer.images:
        transfer.datasets[0].image_refs.append(ome_types.model.ImageRef(id=image.id))

    xml = transfer.to_xml()
    with open(xml_path, 'w') as xml_file:
        xml_file.write(xml)                   
