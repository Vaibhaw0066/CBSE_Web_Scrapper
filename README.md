# CBSE_Web_Scrapper

This scrip uses Beautiful soup and selenium to scrap  affiliation numbers of all CBSE school across India . This script is designed and implemented for autonomous and dynamic scrapping of affiliation number . 


Flow of script : - 
1. Choosing particular CBSE  region selection radio-button . (Selecting to a radio button) -{Using selenium}
2. Selecting particular region of CBSE .(Selecting options from drop-down menu) -  {Using Selenium}
3. Scrapping data(Affiliation no) using Beautiful soup  from the loaded page and then click on next-button to scrap other school's affiliation no. .
4. Loop continues from  1-3 till each school's affiliation no. is being scrapped .
5. Data is being stored in JSON file at end.
