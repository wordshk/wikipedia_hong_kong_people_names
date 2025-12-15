SELECT page_title from page where page_id IN
    (SELECT c1.cl_from
        from categorylinks as c1
        join linktarget as l1 on c1.cl_target_id = l1.lt_id

        join categorylinks as c2 on c1.cl_from = c2.cl_from
        join linktarget as l2 on c2.cl_target_id = l2.lt_id


        WHERE l1.lt_title = 'YYYY年出生' AND l2.lt_title LIKE '%香港%' AND (l2.lt_title = '獲頒授香港榮譽勳章者' OR (NOT l2.lt_title LIKE '%香港%名譽%' AND NOT l2.lt_title LIKE '%香港%榮譽%'))
    );
