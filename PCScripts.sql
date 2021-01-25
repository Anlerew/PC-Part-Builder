--1
SELECT *
FROM cool;

--2
SELECT *
FROM cpu;

--3
SELECT *
FROM gpu;

--4
SELECT *
FROM mem;

--5
SELECT *
FROM mobo;

--6
SELECT *
FROM pcase;

--7
SELECT *
FROM psu;   

--8
SELECT *
FROM stor;

--9
SELECT cpu_name
FROM cpu
WHERE cpu_socket = 'AM4';

--10
/*INSERT INTO pcase (pcase_name, pcase_formfactor, pcase_price)
VALUES ('Cooler Master H500 ARGB Mesh', 'ATX', 109.47);*/

--11
/*DELETE FROM pcase WHERE pcase_name LIKE '%Mesh';*/

--12
/*UPDATE pcase
SET pcase_formfactor = 'EATX'
WHERE pcase_name LIKE '%Mesh';*/

--13
SELECT gpu_name
FROM gpu
WHERE gpu_price > 1000;

--14
SELECT mem_name, mem_capacity
FROM mem
WHERE mem_slots = 4;

--15
SELECT mobo_name
FROM mobo
WHERE mobo_socket = 'AM4';

--16
SELECT stor_name, stor_capacity
FROM stor
WHERE stor_type = 'NVME';

--17
SELECT psu_name
FROM psu
WHERE psu_power > 700;

--18
SELECT cool_name
FROM cool
WHERE cool_type = 'AIO';

--19
SELECT cpu_name, cpu_cores, cpu_threads
FROM cpu
WHERE cpu_cores >= 8;

--20 
SELECT pcase_name
FROM pcase
WHERE pcase_formfactor = 'ATX';

--21
SELECT DISTINCT motherboard, cpu, gpu, mem, memcap, cooler, psu, psupower, pccase, price
FROM (SELECT DISTINCT mobo_name as motherboard
, cpu_name as cpu 
, gpu_name as gpu
, mem_name as mem
, mem_capacity as memcap
, cool_name as cooler
, psu_name as psu
, psu_power as psupower
, pcase_name as pccase
, ROUND(SUM(mobo_price + cpu_price + gpu_price + mem_price + cool_price + psu_price + pcase_price), -1) as price
FROM mobo, cpu, gpu, mem, cool, psu, pcase WHERE mobo_socket = ?
AND cpu_socket = mobo_socket
AND gpu_price >= ? 
AND mem_capacity >= ?
AND cool_type = ?
AND psu_power >= ?
AND pcase_formfactor = ?
GROUP BY motherboard, cpu, gpu, mem, memcap, cooler, psu, psupower, pccase) 

--22
SELECT pcase_name, cpu_name, cpu_socket
FROM pcase
INNER JOIN cpu ON cpu_socket = mobo_socket
INNER JOIN mobo ON mobo_formfactor = pcase_formfactor
WHERE pcase_price > 100 
AND cpu_name LIKE "%Ryzen%" 
AND cpu_socket = 'AM4'
