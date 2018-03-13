CREATE OR REPLACE VIEW smaller
    AS SELECT path, count(*)  AS views
    FROM log
    GROUP BY log.path;

CREATE OR REPLACE VIEW authorssmaller
    AS SELECT smaller.path, smaller.views, articles.slug, articles.author
    FROM smaller JOIN articles
    ON CONCAT('/article/', articles.slug)=smaller.path;

CREATE OR REPLACE VIEW dailylog
    AS SELECT time ::timestamp::date, COUNT(*) AS requests
    FROM log
    GROUP BY time::timestamp::date;

CREATE OR REPLACE VIEW dailyerrors
    AS SELECT time ::timestamp::date, COUNT(*) AS errors
    FROM log \
    WHERE status = '404 NOT FOUND'
    GROUP BY time::timestamp::date;
