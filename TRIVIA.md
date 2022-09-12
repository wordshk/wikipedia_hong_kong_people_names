# Tried and discarded

- Tried to change do this, turns out it only affected 3 entries.

```
-        WHERE c1.cl_to = 'YYYY年出生' AND c2.cl_to LIKE '%香港%'
+        WHERE c1.cl_to = 'YYYY年出生' AND c2.cl_to LIKE '%香港%' AND
+        NOT c1.cl_from IN (SELECT c3.cl_from FROM categorylinks AS c3 WHERE c3.cl_to LIKE '%虛構%')
```


