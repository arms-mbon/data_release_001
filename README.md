# data_release_001

These are the data associated with the EurOBIS DOI XXX (still to be created): species identifications from ARMS-MBON data from 2018-2020 for the COI marker gene. These data include: 
* The individual files that when combined, create the DwCA file that can be found in EurOBIS: a file of occurrences (species and event data), the DNA extension information (omics data), the EMOF (extra information that cannot otherwise be added to the other two files).
* The data that are from the sampling events from which the material that was processed into COI was obtained

For more information on ARMS-MBON, see its [data landing page](data.arms-mbon.org) and references therein. 

For information on the bioinformatics workflow that was used (PEMA), and its input and output files: go to this [GitHub repo](https://github.com/arms-mbon/analysis_release_001)


## EurOBIS DwCA file
These are the files that are combined into one DarwinCore Archive ZIP
* The [CSV containing the occurrences](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_Occurrence.csv) 
* The [CSV containing the DNA data](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_DNAextension.csv) 
* The [CSV containing the extended measurements or facts](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_EMOF.csv) 


## The sampling event data
These are the files that contain the sampling event data. This is a subset of the entire set of [combined event data](https://github.com/arms-mbon/data_workspace/tree/main/QualityControlledData/Combined), and include: 
* A CSV data file containing [observatory information](https://github.com/arms-mbon/data_release_001/blob/main/ObservatoryData_data_release_001.csv), with a metadata file that explains the entries therein
* A CSV data file containing sampling event information, with a metadata file that explains the entries therein
* A CSV data file containing [raw sequence information](https://github.com/arms-mbon/data_release_001/blob/main/OmicsData_data_release_001.csv), with a metadata file that explains the entries therein
* A CSV data file containing [images information](https://github.com/arms-mbon/data_release_001/blob/main/ImageData_data_release_001.csv) (note that there are 1000s of rows in this spreadseheet), with a metadata file that explains the entries therein


