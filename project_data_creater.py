import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from crawler import getBlogCommentRecord
from urlparse import urlparse
from csvUtil import create_csv_file
from dateUtil import get_week

CONSTANTS_START_DATE_STR = '2017-01-22'
CONSTANTS_WP_LINKS_PATH = './data/wp_links.txt'
CONSTANTS_CSV_FILE_NAME = './data/project_data.csv'
CONSTANTS_WP_LINKS_TEMP_PATH = './data/wp_links_temp.txt'

# print(get_week(CONSTANTS_START_DATE_STR, '2017-03-22'))
with open(CONSTANTS_WP_LINKS_PATH) as f:
   wp_links = f.readlines()

all_blog_comment_records = [['target','source','time','week','comment']]
for wp_link in wp_links:
	if (wp_link[0] == '#'):
		continue

	parsed_link = urlparse(wp_link)
	target = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_link)
	print "#########################################"
	print "# taget blog = [%s] " % target
	print "#########################################"
	blog_comment_records = getBlogCommentRecord(target, CONSTANTS_START_DATE_STR)
	for record in blog_comment_records:
			all_blog_comment_records.append(record)

create_csv_file(CONSTANTS_CSV_FILE_NAME, all_blog_comment_records)
