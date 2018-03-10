import psycopg2

db = psycopg2.connect(database="news")

c = db.cursor()

# QUESTION 1: What are the most popular three articles of all time?

query1 = '''SELECT articles.title, COUNT(path)
            AS views FROM articles
            JOIN log ON CONCAT('/article/', articles.slug) = path
            GROUP BY articles.title
            ORDER BY views DESC LIMIT 3;'''

c.execute(query1)

posts = c.fetchall()
print("Most popular three articles of all time are;")
for post in posts:
    print("{0} -- {1} views".format(post[0], post[1]))


# QUESTION 2: Who are the most popular article authors of all time?


query2 = '''SELECT authors.name, COUNT(k.author) as reads
            FROM (
            SELECT articles.author, log.path
            FROM articles
            JOIN log ON CONCAT('/article/', articles.slug) = path )
            k
            JOIN authors ON k.author=authors.id
            GROUP BY authors.name ORDER BY reads DESC;'''

c.execute(query2)

posts = c.fetchall()
print("Most popular article authors of all time are;")
for post in posts:
    print("{0} -- {1} views".format(post[0], post[1]))

"""QUESTION 3: On which days did more than 1% of requests lead to errors?"""

# Create a view of log entries for every day

c.execute("CREATE VIEW dailylog \
            AS SELECT time ::timestamp::date, COUNT(*) AS requests \
            FROM log \
            GROUP BY time::timestamp::date;")

# Create a view of errors happened every day

c.execute("CREATE VIEW dailyerrors \
            AS SELECT time ::timestamp::date, COUNT(*) AS errors \
            FROM log \
            WHERE status = '404 NOT FOUND'\
            GROUP BY time::timestamp::date;")

query3 = '''SELECT (dailyerrors.errors::float * 100 / dailylog.requests::float),
    dailyerrors.time
    FROM dailylog JOIN dailyerrors ON dailylog.time=dailyerrors.time
    WHERE(dailyerrors.errors::float * 100 / dailylog.requests::float) > 1.0;'''

c.execute(query3)
posts = c.fetchall()

print("Days which had more than 1% of requests lead to errors?")
for post in posts:
    print("{0} -- {1:.2f}% errors".format(post[1], float(post[0])))

db.close()
