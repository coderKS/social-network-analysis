#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from dateUtil import get_week
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
	return posts_url

def getCommentsByPost(post_url):
	d = pq(url=post_url)
	data = d(".comment-content")
	comment = ''
	post_comments = []
	printable = set(string.printable)

	for item in data.items():
		comment = item('p').html().encode('utf-8')
		# filter non-ascii char
		post_comments.append(filter(lambda x: x in printable, comment))

	posts_url = ''.join(post_comments)
	posts_url = list(set(posts_url)) # remove duplicates
	return posts_url

def getCommentRecord(blog_url, post_url, starting_date):
	print "%s" % post_url
	d = pq(url=post_url)
	data = d(".comment")
	printable = set(string.printable)
	comment_records = []

	for item in data.items():
		source_url = item('a.url').attr("href")
		if(source_url == None):
			continue

		source_url = source_url.encode('utf-8')
		time = item('time').attr('datetime')
		if(time == None):
			time = item('.comment-header p a').html()
			if(time == None):
				continue
		time = time.encode('utf-8')
		comment = item('.comment-content p').html().encode('utf-8')

		time = time[0:10]
		comment = filter(lambda x: x in printable, comment) # filter non-ascii char
		week = get_week(starting_date, time)
		print "\t\t source=[%s], time=[%s], week=[%s], comment=[%s]" % (source_url, time, week, comment)

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
