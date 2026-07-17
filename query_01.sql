SELECT
    e.EMPLOYEE_ID AS funcionario_id,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS nome_completo,
    e.HIRE_DATE AS data_contratacao,
    e.SALARY AS salario,
    d.DEPARTMENT_NAME AS departamento,
    j.JOB_TITLE AS cargo,
    j.MIN_SALARY AS salario_min_cargo,
    j.MAX_SALARY AS salario_max_cargo
FROM
    HR.EMPLOYEES e
LEFT JOIN
    HR.DEPARTMENTS d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN
    HR.JOBS j ON e.JOB_ID = j.JOB_ID
WHERE
    e.DEPARTMENT_ID IS NOT NULL
    AND e.SALARY IS NOT NULL
ORDER BY
    d.DEPARTMENT_NAME ASC,
    e. SALARY DESC;
