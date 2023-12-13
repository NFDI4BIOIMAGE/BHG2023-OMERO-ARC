
### How to install omero-cli-transfer-arc from Christoph
### Until its officially accepted by omero-cli-transfer from Erick Martins.

1. conda create -n omero-arc1 -c conda-forge python=3.8 zeroc-ice=3.6.5

2. conda activate omero-arc1

3. git clone -b pack_plugin --single-branch https://github.com/cmohl2013/omero-cli-transfer.git

4. cd omero-cli-transfer/

5. pip install .

6. git clone git@github.com:cmohl2013/omero-arc.git

7. pip install .

8. cd omero-arc

9. omero transfer pack --plugin arc Project:1111 /path/to/my/new/arc/





#### It seems now the omero-arc plugin is merged in omero-cli-transfer.

##### The installation instructions will be availabe from the following github

Github for original omero-cli-transfer : https://github.com/ome/omero-cli-transfer









