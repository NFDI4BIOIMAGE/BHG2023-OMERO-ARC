
# 👋 BHG2023-OMERO-ARC

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Repository for documentation during the **[2nd de.NBI BioHackathon Germany](https://www.denbi.de/de-nbi-events/1547-biohackathon-germany-2)** - 11.-15.12.2023 - **[OMERO-ARC project](https://www.denbi.de/de-nbi-events/1614-towards-omero-and-arc-interoperability-for-rdm-compliant-bio-image-data)** (in short: **BHG2023-OMERO-ARC**)  

🚧 Under construction. 🚧

## Code of Conduct
Please also adhere here to the [ELIXIR Germany Code of Conduct](https://www.denbi.de/code-of-conduct). 

## Task_Groups
Initially prepared and suggested based on defined task of participants.

## Branch protection
- The main branch is protected. For merging a branch into main you need a PR with at least one approving review.
- @andreaschrader only initially bypasses this in order to set up the repository for the participants for the Hackathon.

## [.gitignore](./\.gitignore)
- currently selected: Visual Studio
- Prep_stage/
  - You can create this directroy inside your cloned BHG2023-OMERO-ARC repo and use it when you want to prepare files or place data in this repo locally but do not want to push these to this repo.
 

<br/>

---
---

## Overview of the content in this repository

```
.
├── .zenodo.json
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── Reporting
│   ├── BioHack_2023_Final_OMERO_ARC.pdf
│   └── BioHack_2023_Intro_OMERO_ARC.pdf
├── Task_Groups
│   ├── 01_Roadmap
│   │   ├── README.md
│   │   └── arc-omero-roundtrip-proposal.md
│   ├── 02_Use_Cases
│   │   └── README.md
│   ├── 03_RDMcompliant_Metadata
│   │   ├── IDRtemplates-2-ARC
│   │   ├── IDRtemplates-2-ARC.md
│   │   ├── README.md
│   │   ├── REMBI-2-ARC
│   │   ├── REMBI-2-ARC.md
│   │   ├── REMBI_Templates
│   │   │   └── RGC_Ca2+_imaging.csv
│   │   └── REMBI_Templates.md
│   ├── 04_Metadata_Transfer
│   │   └── README.md
│   ├── 05_OMERO-2-ARC
│   │   └── README.md
│   ├── 06_ARC-2-OMERO
│   │   ├── README.md
│   │   ├── metadata_filler.py
│   │   ├── requirements.txt
│   │   ├── transfer.xml
│   │   └── workflow.sh
│   ├── 07_Test_Tools
│   │   ├── README.md
│   │   ├── omero-cli-transfer-arc-installation.md
│   │   └── omero-cli-transfer-arc-report.md
│   ├── 08_Teaching_Material
│   │   └── README.md
│   ├── 09_Documentation
│   │   └── README.md
│   └── README.md
└── images
    └── rat-brain-ls.png
```
21-01-2024 (created using tree v2.1.1 © 1996 - 2023 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro)

<br/>

---
---

## Contributions

**Notes on contributions during the Hackathon are [here](CONTRIBUTING.md).**

 <br />

🙌 Thank you for any contribution to the **BHG2023-OMERO-ARC** repository!!!  

When contributing, please consider that (parts of) this repository might be used by people with various background and intentions including teaching in the future. Therefore, it is appreciated if you can provide ***a brief non-specialist targeted introduction / summary*** preceding your content and work on Hackathon tasks.  


## Contributors
🤝 Participants contributing to the **BHG2023-OMERO-ARC project** can provide their name, GitHub handle, ORCID iD and ROR here - if you like.  

Suggestion: alphabetical order (surname):  

|name|GitHub|ORCID|ROR|  
|---|---|---|---|  
|Mohamed Abdrabbou|[@MM-abdrabbou](https://github.com/MM-abdrabbou) | [https://orcid.org/0000-0003-2778-7483](https://orcid.org/0000-0003-2778-7483)|
|Michele Bortolomeazzi|[@MicheleBortol](https://github.com/michelebortol)|https://orcid.org/0000-0001-5805-5774||
|Jean-Marie Burel|[@jburel](https://github.com/jburel)|https://orcid.org/0000-0002-1789-1861|[https://ror.org/03h2bxq36](https://ror.org/03h2bxq36)|
|Niraj Kandpal|[@Nirkan](https://github.com/Nirkan)|https://orcid.org/0009-0007-5101-4786|[https://ror.org/00rcxh774](https://ror.org/00rcxh774) <br>[https://ror.org/04c4bwh63](https://ror.org/04c4bwh63)|
|Josh Moore|[@joshmoore](https://github.com/joshmoore)|https://orcid.org/0000-0003-4028-811X|[https://ror.org/05tpnw772](https://ror.org/05tpnw772)|
|Andrea Schrader|[@andreaschrader](https://github.com/andreaschrader)|https://orcid.org/0000-0002-3879-7057|https://ror.org/034waa237<br>https://ror.org/00rcxh774| 
|Peter Zentis|[@pzentis](https://github.com/pzentis)|[https://orcid.org/0000-0002-6999-132X](https://orcid.org/0000-0002-6999-132X)|[https://ror.org/00rcxh774](https://ror.org/00rcxh774) <br>[https://ror.org/04c4bwh63](https://ror.org/04c4bwh63) |



## Acknowledgement
🚧 Under construction. 🚧

To be filled after the Hackathon.

## Funding enabling project leads organization and Hackathon participation

#### DataPLANT and NFDI4BIOIMAGE
We acknowledge the support of DataPLANT and NFDI4BIOIMAGE, both funded by the German Research Foundation
(DFG) within the framework of the NFDI – project numbers: 442077441 and 501864659.

### Other Organisations
#### CEPLAS
Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) within Germany’s Excellence Strategy – EXC-2048/1 – project number 390686111.

#### CECAD
Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany's Excellence Strategy - EXC 2030 - 390661388.

#### CRC TRR341
Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 456082119.
