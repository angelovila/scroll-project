from flask import Flask, render_template, request, redirect, url_for
from flask import flash, jsonify, session as login_session, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy_personal import Base, Cases

import json
from urllib_personal import page_crawl_pick

##### CONNET DATABASE####
engine = create_engine('sqlite:///cases.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

##########################

MONTHS = ["January",
		  "February",
		  "March",
		  "April",
		  "May",
		  "June",
		  "July",
		  "August",
		  "September",
		  "October",
		  "November",
  		  "December"
  		  ]
YEARS_NEW= ["2016",
		 "2015",
		 "2014",
		 "2013"
		 ]
YEARS_OLD = ["2012",
		 "2011",
		 "2010",
		 "2009",
		 "2008",
		 "2007",
		 "2006",
		 "2005",
		 "2004",
		 "2003",
		 "2002",
		 "2001",
		 "2000",
		 "1999",
		 "1998",
		 "1997",
		 "1996",
		 "1995"
		 ]


REGULAR_EXPRESSION = '<li><a href="/pdf/web/viewer\.html\?file=(.+\.pdf)" target="_blank">(.+)Vs\. (.+)</a><br>\r\n.+G\.R\. No\. (\d+)\. (\w+) (\d+), (\d+)</li>'
## will generate 
## pdf link - ('/jurisprudence/2016/february2016/204970.pdf',
## party1- 'Spouses Claudio and Carmencita Trayvilla'
## party2 - 'Bernardo Sejas and Juvy Paglinawan represented by Jessie Paglinawan'
## G R NO - '204970',
## Date_month - 'February'
## Date_day - 1
## Date_year - 2016


#url_sample = 'http://sc.judiciary.gov.ph/jurisprudence/2016/toc/february.php'


#var = page_crawl_pick(url_sample, REGULAR_EXPRESSION)

url = 'http://sc.judiciary.gov.ph/jurisprudence/'

def query_cases():  #IN PROGRESS
	cases = session.query(Cases).all()
	return jsonify(items=[case.serialize for case in cases])
#jsonify(items=[i.serialize for i in items])


def multi_page_scrape(month_list, year_list, url): #IN PROGRESS, NEED TO ADD WRITE TO DATABASE CASE
	for year in year_list:
		for month in month_list:
			scrape_url = url+year+'toc/'+month+'.php'
			page_crawl_pic(url,REGULAR_EXPRESSION)


