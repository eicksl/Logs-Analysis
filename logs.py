#!/usr/bin/python3

import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

c.execute("""
SELECT articles.title, count(*) as num
from log, articles
where log.path = '/article/' || articles.slug
group by articles.title
order by num desc
limit 3;
""")

top_articles = c.fetchall()

c.execute("""
SELECT authors.name, count(*) as num
from authors, articles, log
where log.path = '/article/' || articles.slug
and authors.id = articles.author
group by authors.name
order by num desc;
""")

top_authors = c.fetchall()

c.execute("""
WITH errors as (
select time::date as day, count(*) as total,
       sum((log.status != '200 OK')::int)::float as err
from log
group by day
)
select to_char(day, 'FMMonth FMDD, YYYY'),
       round((err/total*100)::numeric, 2) || '%' as error_rate
from errors
where err / total > .01;
""")

high_errors = c.fetchall()

db.close()

print("\n\n\n")
print("Top three popular articles:\n")
for i in top_articles:
    print("\"{}\" -- {} views".format(i[0], i[1]))

print("\n\nAuthor popularity:\n")
for i in top_authors:
    print("{} -- {} views".format(i[0], i[1]))

print("\n\nDays when error rate of requests exceeded 1%:\n")
for i in high_errors:
    print("{} -- {} errors".format(i[0], i[1]))
print("\n\n\n")

exit()
