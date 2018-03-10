# newsdata
This is for Udacity Full Stack Nanodegree, Logs Analysis Project. It is for practising SQL in a real world scenario. 

In this project I have given an SQL database with some newspaper website log for a month. There are 3 questions asked in
this database;

QUESTION 1: What are the most popular three articles of all time?  
QUESTION 2: Who are the most popular article authors of all time?  
QUESTION 3: On which days did more than 1% of requests lead to errors?  

To be able to run this, user need to have the required news database running locally.

I have created 2 views for answering 3rd question;

dailylog -> 
```sql
CREATE VIEW dailylog 
AS SELECT time ::timestamp::date, COUNT(*) AS requests 
FROM log 
GROUP BY time::timestamp::date;
```

dailyerrors ->            
 ```sql           
CREATE VIEW dailyerrors 
AS SELECT time ::timestamp::date, COUNT(*) AS errors 
FROM log 
WHERE status = '404 NOT FOUND'
GROUP BY time::timestamp::date;
```

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
