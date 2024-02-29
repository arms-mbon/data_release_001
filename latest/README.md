# data_release_001

<!--These are the data files associated with the first ARMS-MBON dataset submitted to EurOBIS ([DOI](https://doi.org/10.14284/620)): -->
These are the data files to be submitted to EurOBIS: species identifications, sampling even metadata, image metadata for the COI, ITS, and 18S marker gene for the events between 2018 and 2020 (all events that started in 2018 and 2019). This includes: 
* The individual files that when combined, create the DwCA file that can be found in EurOBIS: a file of occurrences (species and event data), the DNA extension information (omics data), the EMOF (extra information that cannot otherwise be added to the other two files).
* The observatory, sampling event, omics and image data related to the sampling events included in this EurOBIS dataset. These expand somewhat on the information included in the EurOBIS file.

The source files for the omics and taxonomic data that are included in the EurOBIS file can be found in [the analysis_release_001](https://github.com/arms-mbon/analysis_release_001) repository: the input and output files for the bioinformatics analysis done with PEMA can be found there.

For more information on ARMS-MBON, see its [data landing page](https://data.arms-mbon.org/) and references there in. 

<!--
## EurOBIS DwCA file
These are the files that are combined into one DarwinCore Archive ZIP
* The [CSV containing the occurrences](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_Occurrence.csv) 
* The [CSV containing the DNA data](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_DNAextension.csv) 
* The [CSV containing the extended measurements or facts](https://github.com/arms-mbon/data_release_001/blob/main/ARMS_COI_EMOF.csv) 
-->

## The sampling event data
These are the files that contain the sampling event data. This is a subset of the entire ARMS-MBON set of [combined event data](https://github.com/arms-mbon/data_workspace/tree/main/qualitycontrolled_data/combined), and include: 
* A CSV data file containing [observatory metadata](https://github.com/arms-mbon/data_release_001/blob/main/OservatoryData_release001.csv), with an accompanying metadata file
* A CSV data file containing [sampling event metadata](https://github.com/arms-mbon/data_release_001/blob/main/SamplingeventData_release001.csv), with an accompanying metadata file
* A CSV data file containing [raw sequence metadata](https://github.com/arms-mbon/data_release_001/blob/main/OmicsData_release001.csv), with an accompanying metadata file; including the ENA accession numbers and a limited amount of additional omics metadata. For more information on the processing of the samples and subsequence bioinformatics, see the EurOBIS files in this folder and the [analysis_release_001](https://github.com/arms-mbon/analysis_release_001) repository.
* A CSV data file containing [images metadata](https://github.com/arms-mbon/data_release_001/blob/main/ImageData_release001.csv), with an accompanying metadata file (note that there are 1000s of rows in this spreadsheet), with a metadata file that explains the entries therein. Images are currently stored in PlutoF and can be downloaded by accessing the links 
in the "Download URL" column.


