# Logs Analysis Project

## Introduction

This is for Udacity Full Stack Nanodegree, Logs Analysis Project. It is for practising SQL in a real world scenario. 

In this project I have given an SQL database with some newspaper website log for a month. There are 3 questions asked in
this database;

QUESTION 1: What are the most popular three articles of all time?  
QUESTION 2: Who are the most popular article authors of all time?  
QUESTION 3: On which days did more than 1% of requests lead to errors?  

## Requirements

To be able to run this, user need to have the required news database running locally.

This project can be run in a virtual environment using vagrant;
    Vagrant https://www.vagrantup.com/  
    VirtualBox https://www.virtualbox.org/wiki/Downloads

It can be developed locally as well by using Python

    Python ver 3  
    PostgreSQL 
    psycopg2 

## Database Set-up
 To be able to work in this project user needs an accessible database setup.
 
 If you have downloaded and setup vagrant system, this comes automatically.
 If not you need to download and import sql file
 from this link;  
 https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

*Important*
I have created 4 views these needs to be imported by using the views.sql file  
by using;  
```
psql -d news -f create_views.sql
```
## How To Run
```
python news.py
```


## Results

Output of the program after it is run is;

Most popular three articles of all time are;  
Candidate is jerk, alleges rival -- 338647 views  
Bears love berries, alleges bear -- 253801 views  
Bad things gone, say good people -- 170098 views   

Most popular article authors of all time are;  
Ursula La Multa -- 507594 views  
Rudolf von Treppenwitz -- 423457 views  
Anonymous Contributor -- 170098 views  
Markoff Chaney -- 84557 views  

Days which had more than 1% of requests lead to errors?  
2016-07-17 -- 2.26 % errors 
