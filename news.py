#!/usr/bin/env python3

import psycopg2

db = psycopg2.connect(database="news")

c = db.cursor()

# Dont forget to run views.sql to create the views needed!!

# QUESTION 1: What are the most popular three articles of all time?


def question1():

    query1 = '''SELECT title, views
                FROM articles
                JOIN smaller AS log
                ON log.path = '/article/' || articles.slug
                ORDER BY views DESC LIMIT 3;'''

    c.execute(query1)

    posts = c.fetchall()
    print("Most popular three articles of all time are;")
    for title, views in posts:
        print("{0} -- {1} views".format(title, views))
    print('\n')
    return None

# QUESTION 2: Who are the most popular article authors of all time?


def question2():

    query2 = '''SELECT authors.name, SUM(authorssmaller.views) as reads
                FROM authorssmaller
                JOIN authors ON authorssmaller.author=authors.id
                GROUP BY authors.name ORDER BY reads DESC;'''

    c.execute(query2)

    posts = c.fetchall()
    print("Most popular article authors of all time are;")
    for author, views in posts:
        print("{0} -- {1} views".format(author, views))
    print('\n')
    return None


"""QUESTION 3: On which days did more than 1% of requests lead to errors?"""


def question3():
    query3 = '''SELECT (dailyerrors.errors::float * 100 / dailylog.requests::float),
        dailyerrors.time
        FROM dailylog JOIN dailyerrors ON dailylog.time=dailyerrors.time
        WHERE(dailyerrors.errors::float * 100 / dailylog.requests::float) > 1.0;'''

    c.execute(query3)
    posts = c.fetchall()

    print("Days which had more than 1% of requests lead to errors?")
    for post in posts:
        print(
            "{0:%B %d, %Y} -- {1:.2f}% errors".format(post[1], float(post[0])))

    return None


question1()
question2()
question3()

db.close()
