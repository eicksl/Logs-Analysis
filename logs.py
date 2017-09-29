#!/usr/bin/python3

import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

c.execute(" \
SELECT articles.title, count(*) AS num \
FROM log, articles \
WHERE POSITION(articles.slug IN log.path) > 0 \
GROUP BY articles.title \
ORDER BY num DESC \
LIMIT 3;")

top_articles = c.fetchall()

c.execute(" \
SELECT authors.name, count(*) AS num \
FROM authors, articles, log \
WHERE POSITION(articles.slug IN log.path) > 0 \
AND authors.id = articles.author \
GROUP BY authors.name \
ORDER BY num DESC;")

top_authors = c.fetchall()

c.execute(" \
WITH error_requests AS ( \
SELECT time::date AS day, count(*) AS num \
FROM log \
WHERE status = '404 NOT FOUND' \
GROUP BY day \
ORDER BY day ASC \
), ok_requests AS ( \
SELECT time::date AS day, count(*) AS num \
FROM log \
WHERE status = '200 OK' \
GROUP BY day \
ORDER BY day ASC \
), error_rate AS ( \
SELECT ok_requests.day, error_requests.num / ok_requests.num::float AS rate \
FROM error_requests, ok_requests \
WHERE error_requests.day = ok_requests.day \
AND ok_requests.num != 0 \
) \
SELECT error_rate.day, ROUND(error_rate.rate::numeric * 100, 1) || '%' AS rate \
FROM error_rate \
WHERE rate > .01;")

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