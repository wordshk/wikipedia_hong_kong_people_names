SELECT page_title from page where page_id IN
    (SELECT c1.cl_from
        from categorylinks as c1
        join categorylinks as c2 on c1.cl_from = c2.cl_from
        WHERE c1.cl_to = 'YYYY年出生' AND c2.cl_to LIKE '%香港%' AND (c2.cl_to = '獲頒授香港榮譽勳章者' OR (NOT c2.cl_to LIKE '%香港%榮譽%'))
    );
