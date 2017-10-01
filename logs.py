#!/usr/bin/python3

import psycopg2


top_articles = """
SELECT articles.title, count(*) as num
from log, articles
where log.path = '/article/' || articles.slug
group by articles.title
order by num desc
limit 3;
"""

top_authors = """
SELECT authors.name, count(*) as num
from authors, articles, log
where log.path = '/article/' || articles.slug
and authors.id = articles.author
group by authors.name
order by num desc;
"""

high_errors = """
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
"""


def connect(db_name="news"):
    '''Connects to a database'''
    try:
        db = psycopg2.connect(database=db_name)
        c = db.cursor()
        return db, c
    except:
        print("Failed to connect to {} database.".format(db_name))


def run_queries(**kwargs):
    '''Runs queries specified in keyword arguments'''
    db, c = connect()
    for query in kwargs:
        c.execute(kwargs[query])
        kwargs[query] = c.fetchall()
    db.close()
    return kwargs


def print_data():
    '''Prints output of queries'''
    output = run_queries(top_articles=top_articles, top_authors=top_authors,
                                                    high_errors=high_errors)
    print("\n\n\n")
    print("Top three popular articles:\n")
    for i in output['top_articles']:
        print("\"{}\" -- {} views".format(i[0], i[1]))

    print("\n\nAuthor popularity:\n")
    for i in output['top_authors']:
        print("{} -- {} views".format(i[0], i[1]))

    print("\n\nDays when error rate of requests exceeded 1%:\n")
    for i in output['high_errors']:
        print("{} -- {} errors".format(i[0], i[1]))
    print("\n\n\n")


print_data()
exit()
