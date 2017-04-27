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

def read_links(file):
	with open(file) as f:
		links = f.readlines()
   	links = [l for l in links if l[0] != '#']
  	return links
	return None

def parse_url(url):
	parsed_link = urlparse(url)
	formatted_link = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_link)
	return formatted_link

def create_url_mapping():
	url_mapping = dict()
	url_mapping_id = 1
	links = read_links(CONSTANTS_WP_LINKS_PATH)
	if links == None:
		return None
	for link in links:
		link = link.strip()
		link = parse_url(link)
		url_mapping[link] = url_mapping_id
		url_mapping_id += 1 # increment key
	return url_mapping

def get_id(link, link_map):
	link = link.strip()
	link = parse_url(link)
	if link in link_map:
		return link_map[link]
	else:
		return "id not found"

def start(links_file):
	url_mapping = create_url_mapping()
	wp_links = read_links(links_file)
	all_blog_comment_records = [['target','source','time','week','comment','target_id','source_id']]
	url_without_comments = []
	for wp_link in wp_links:
		target = wp_link.strip()
		print "#########################################"
		print "# taget blog = [%s] " % target
		print "#########################################"
		blog_comment_records = getBlogCommentRecord(target, CONSTANTS_START_DATE_STR)
		if(len(blog_comment_records) == 0):
			print "!!! Cannot find any comment !!!\n"
			url_without_comments.append(wp_link)
		for record in blog_comment_records:
			target = record[0]
			source = record[1]
			record.append(get_id(target, url_mapping))
			record.append(get_id(source, url_mapping))
			all_blog_comment_records.append(record)

	create_csv_file(CONSTANTS_CSV_FILE_NAME, all_blog_comment_records)
	print "url_without_comments:"
	print url_without_comments

# Program starts here
start(CONSTANTS_WP_LINKS_TEMP_PATH)
