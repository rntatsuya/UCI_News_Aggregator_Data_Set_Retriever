# UCI_News_Aggregator_Data_Set_Retriever

Want to work on a natural language processing project that involves categorizing news 
articles but can't find a good data set anywhere on the internet?

Then this is your lucky day because here's a tool that can literally make the data set for you!

This tool uses the [News Aggregator Data Set](https://archive.ics.uci.edu/ml/datasets/News+Aggregator) (which has been reorganized into smaller files in the rawData directory), which is available in the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.html). 


### Why did I make this tool? 

Because I wanted to dive into natural language processing with a simple categorization problem, and this UCI News Aggregator Data Set was one of the few data sets that had enough labeled data. BUT, unfortunately the downside to this was that due to restrictions on content and use of the news sources, the corpus was limited to web references (urls) to web pages and did not include any text content. 


### Run the program with

```
UCI_news_aggregator_DS_retriever.py rawData output
```

### Resulting Output

The output will be written to csv files, which will be saved in the specified output directory. Each output csv corresponds to one input csv, and they are formatted in the following way:

Article Title  |  Content  |  Category          |  ID
---------------|-----------|--------------------|-----------------
Fed's Plosser: Taper pace may be too slow          |  <article_content>  |  b |  ddUyU0VZz0BRneMioxUPQVP6sIxvM


If you can help me improve the time or memory efficiency of the program, feel free to send a pull request!
