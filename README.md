# IR_Search_Engine

This is a simple search engine..


Requirements:
1. Elasticsearch(version - 7.7.1 or higher) should be up and running.
2. Kibana(version - 7.7.1 or higher) should be up and running.
3. Node.js should be installed. Confirm it by typing, (node --version ) in command prompt without brackets.


All you need to do is : 

1. Clone this reository by 
( git clone https://github.com/isuru9625/IR_Search_Engine.git )

2. Run the data.js file by typing, (node index.js) in command prompt without brackets. It will add all the meta data(which are in out.json file) to elasticsearch. There are 2700 songs with meta data in out.json file.

3. Run the index.js file by typing, (node index.js) in command prompt without brackets.

4. Go to the  browser and go to the url - http://localhost:3001/

5. Search for the word either in sinhala or english ( But when you want sinhala, get the sinhala words from anywhere and paste it there)

6. Examples for sinhala words : - "අම්මා", "අම්", "මන්දාරම්" , "මන්දාර"


Description - 

1. Python code(scraper.py) that has been used to scrape the meta data of sinhala songs is in the Scrape folder. 

2. Scraped json file(out.json) is in the root folder.

