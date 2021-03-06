# Write your MySQL query statement below
SELECT SUM(TIV_2016) as TIV_2016
FROM insurance
WHERE TIV_2015 IN (SELECT TIV_2015 FROM insurance GROUP BY TIV_2015 HAVING COUNT(*) > 1) AND
CONCAT(LAT, LON) IN (SELECT CONCAT(LAT, LON) as lat_lon FROM insurance GROUP BY CONCAT(LAT, LON) HAVING COUNT(*) = 1)
