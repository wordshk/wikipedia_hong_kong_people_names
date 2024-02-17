SELECT count(page_title) as cc, page_title from page as pg JOIN pagelinks AS pl ON pl.pl_title = pg.page_title where pg.page_id IN (
    SELECT c1.cl_from
        from categorylinks as c1
        join categorylinks as c2 on c1.cl_from = c2.cl_from
        WHERE c1.cl_to LIKE '%虛構%' AND c2.cl_to LIKE '%角色%'
) group by pg.page_title order by cc desc;
