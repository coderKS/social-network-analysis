#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from dateUtil import get_week, get_time
import re
import urllib
import urllib2
import sys
import codecs
import string

def getPost(url):
	d = pq(url=url)
	data = d("a")
	posts_url = [] 
	for item in data.items():
		if item.attr('rel') == 'bookmark':
			posts_url.append(item.attr('href').encode('utf-8'))

	posts_url = list(set(posts_url)) # remove duplicates
	return posts_url

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getCommentContent(dom_item):
	data = dom_item(".comment-content p")
	comment = []
	printable = set(string.printable)

	for item in data.items():
		comment_block = item.html().encode('utf-8')
		# filter non-ascii char
		comment.append(filter(lambda x: x in printable, comment_block))

	if (len(comment) == 0):
		data = dom_item(".comment-body p")
		for item in data.items():
			comment_block = item.html().encode('utf-8')
			# filter non-ascii char
			comment.append(filter(lambda x: x in printable, comment_block))

	comment = ''.join(comment)
	comment = cleanhtml(comment)
	return comment

def getCommentRecord(blog_url, post_url, starting_date):
	post_url = post_url.strip()
	print "%s" % post_url

	d = pq(url=post_url)
	data = d(".comment")
	printable = set(string.printable)
	comment_records = []

	for item in data.items():
		source_url = item('a.url').attr("href")
		if(source_url == None):
			print "source_url not found"
			continue

		source_url = source_url.encode('utf-8')
		time = item('time').attr('datetime')
		if(time == None):
			time = item('.comment-header p a').html()
			if(time == None):
				time = item('.comment-meta a').html().strip()
				if(time == None):
					print "time not found"
					continue

		print time
		time = time.encode('utf-8')
		comment = getCommentContent(item)

		# time = time[0:10]
		comment = filter(lambda x: x in printable, comment) # filter non-ascii char
		week = get_week(starting_date, time)
		time = get_time(time)
		comment_abbreviation = comment[0:20] + "......" + comment[-20:]
		print "\t\t target=[%s], source=[%s], time=[%s], week=[%s], comment=[%s]" % (blog_url, source_url, time, week, comment_abbreviation)

		record = []
		record.append(blog_url)
		record.append(source_url)
		record.append(time)
		record.append(week)
		record.append(comment)

		comment_records.append(record)

	print "\n"
	return comment_records

def getBlogCommentRecord(blog_url, starting_date):
	blog_comment_records = []
	posts_url = getPost(blog_url);

	for post_url in posts_url:
		comment_records = getCommentRecord(blog_url, post_url, starting_date)
		for record in comment_records:
			blog_comment_records.append(record)

	return blog_comment_records
