SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name,
    e.salary,
    l.city,
    l.state_province,
    c.country_name,
    r.region_name
FROM HR.EMPLOYEES e
LEFT JOIN HR.DEPARTMENTS d
       ON e.department_id = d.department_id
LEFT JOIN HR.LOCATIONS l
       ON d.location_id = l.location_id
LEFT JOIN HR.COUNTRIES c
       ON l.country_id = c.country_id
LEFT JOIN HR.REGIONS r
       ON c.region_id = r.region_id
ORDER BY
    r.region_name,
    c.country_name,
    l.city,
    e.salary DESC;