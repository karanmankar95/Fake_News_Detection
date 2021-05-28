# Fake_News_Detection

1. Please follow the following steps to recreate the project and successfully run the code in the "code" folder.

2. The dataset has been taken from two different sources, one is the Politifact Dataset taken from https://github.com/KaiDMML/FakeNewsNet/tree/master/dataset and the other is        PhemeRNR Dataset taken from https://figshare.com/articles/dataset/PHEME_dataset_of_rumours_and_non-rumours/4010619

3. To download the Politfact dataset please directly download the data named politifact_real.csv and politifact_fake.csv from the repository. To download the PhemeRNR dataset,        please visit the link mentioned above and then download .tar.bz2 file at the bottom of the page. This particular dataset needs to be extracted from the tar file to access.

4. Once the both the politifact files are downloaded, run FakeNewsNet.ipynb notebook over both the files by making appropriate changes in the filepath and following the comments      in the notebook

5. For the PhemeRNR dataset, after the data has been extracted, please run the script convert.py by providing the appropriate path for the rootdir variable and please repeat the      procedure for all the five events.

6. Please run the PhemeData.ipynb notebook over the newly created CSV files of the PhemeRNR dataset. Use the code from this notebook for concatenation of politifact_fake and          politifact_real files as well.

7. Once the real and fake datasets have been merged for both politifact and phemeRNR datasets, run the Politifact_cleaning.ipynb and Pheme_cleaning.ipynb notebooks over the          respective databases following the text instructions given inside the notebook in Markdown cells.

8. After that please run the Exploratory_Data_Analysis.ipynb notebook over the newly combined finalData followed by the Modeling.ipynb notebook.

9. I have included all the result .csv files created by the above operations in the Data folder. 
