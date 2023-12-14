
### How to install omero-cli-transfer-arc from Christoph


#### Now the omero-arc plugin is merged in omero-cli-transfer.

##### The installation instructions are availabe from the following github

Github for original omero-cli-transfer : https://github.com/ome/omero-cli-transfer

1. python3 -m venv clitest

2. source clitest/bin/activate

3. git clone https://github.com/ome/omero-cli-transfer.git

4. cd omero-cli-transfer

5. pip3 install .

6. cd ..

7. git clone https://github.com/ome/omero-cli-transfer.git

8. cd omero-arc

9. pip3 install .
    
10. cd ../clitest/bin/
  
11. wget https://github.com/nfdi4plants/ARCCommander/releases/download/v1.0.0-preview.2/arc_linux-x64

12. omero transfer pack --plugin arc Project:111 /path/to/arc/













### Old installation instructions

### Before it was officially accepted by omero-cli-transfer from Erick Martins.



1. conda create -n omero-arc1 -c conda-forge python=3.8 zeroc-ice=3.6.5

2. conda activate omero-arc1

3. git clone -b pack_plugin --single-branch https://github.com/cmohl2013/omero-cli-transfer.git

4. cd omero-cli-transfer/

5. pip install .

6. git clone git@github.com:cmohl2013/omero-arc.git

7. pip install .

8. cd omero-arc

9. omero transfer pack --plugin arc Project:1111 /path/to/my/new/arc/











