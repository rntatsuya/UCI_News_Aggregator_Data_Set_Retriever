# -*- coding: utf-8 -*-

import codecs
import csv
import sys
import urllib2
from newspaper import Article
from os import listdir, path, mkdir

### HELPER METHOD ###

# converts unicode value to corresponding ASCII value, not extensive!
def unicodetoascii(text):

	TEXT = (text.
			replace('\xe2\x80\x99', "'").
			replace('\xc3\xa9', 'e').
			replace('\xe2\x80\x90', '-').
			replace('\xe2\x80\x91', '-').
			replace('\xe2\x80\x92', '-').
			replace('\xe2\x80\x93', '-').
			replace('\xe2\x80\x94', '-').
			replace('\xe2\x80\x94', '-').
			replace('\xe2\x80\x98', "'").
			replace('\xe2\x80\x9b', "'").
			replace('\xe2\x80\x9c', '"').
			replace('\xe2\x80\x9c', '"').
			replace('\xe2\x80\x9d', '"').
			replace('\xe2\x80\x9e', '"').
			replace('\xe2\x80\x9f', '"').
			replace('\xe2\x80\xa6', '...').
			replace('\xe2\x80\xb2', "'").
			replace('\xe2\x80\xb3', "'").
			replace('\xe2\x80\xb4', "'").
			replace('\xe2\x80\xb5', "'").
			replace('\xe2\x80\xb6', "'").
			replace('\xe2\x80\xb7', "'").
			replace('\xe2\x81\xba', "+").
			replace('\xe2\x81\xbb', "-").
			replace('\xe2\x81\xbc', "=").
			replace('\xe2\x81\xbd', "(").
			replace('\xe2\x81\xbe', ")").
			replace('\n', " ").
			replace('\'', "'")

				 )
	return TEXT


def main():
	if len(sys.argv) < 3:
		print "Specify input and output directories in following format:"
		print "python UCI_news_aggregator_DS_retriever.py <input_folder_name> <output_folder_name>"
		exit()
	
	
	input_folder = sys.argv[1]
	output_folder = sys.argv[2]
	
	if not path.isdir(output_folder):
		mkdir(output_folder)
	
	# get file names for raw data directory and completed data directory
	raw_files = listdir(input_folder)
	done_files = listdir(output_folder)
	
	# remove files that have already been parsed
	for file in done_files:	
		if file[:9]+'.csv' in raw_files:
			raw_files.remove(file[:9]+'.csv')

	# remove this "invisible" file
	if '.DS_Store' in raw_files:
		raw_files.remove('.DS_Store')

	print "Starting Data Extraction"
	ret = []
	for file in raw_files:
		count = 0
		keeping = 0
		# write to output data file as csv
		with codecs.open(output_folder+'/'+file[:9]+'DATA.csv', "wb", errors='ignore') as csv_file:
			writer = csv.writer(csv_file, delimiter=',')
			
			# read from input data csv file
			with codecs.open(input_folder+'/'+file, 'rb', errors='ignore') as csvfile:
				reader = csv.reader(csvfile, delimiter='\t')
				for row in reader:
					title = row[1]
					url = row[2]
					category = row[4]
					id = row[5]
					
					count += 1
					# try accessing url, skip if we encounter an error
					try:
						urllib2.urlopen(url)
					except Exception as e:
						print "%d: ignoring because %s" % (count, e)
					else:
						keeping += 1
						print "%d: keeping" % count
						article = Article(url)
						
						article.download()
						article.parse()
						
						article_text = unicodetoascii(article.text.encode("utf8", 'ignore'))
						title = title.encode("utf8", 'ignore')
						category = category.encode("utf8", 'ignore')
						id = id.encode("utf8", 'ignore')
						
						writer.writerow([title, article_text, category, id])


		print "Writing out %d articles to csv file: %s" % (keeping, file[:9]+'DATA.csv')
	

if __name__ == "__main__":
	main()