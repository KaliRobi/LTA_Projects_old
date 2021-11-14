insert into Geo (city, county ) VALUES('Balmazújváros', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Debrecen', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Egyek', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Vámospércs', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Hajdúhadház', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Hajdúböszörmény', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Mikepércs', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Budapest', 'Pest' );
insert into Geo (city, county ) VALUES('Bagamér', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Nyírábrány', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Tiszacsege', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Derecske', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Józsa', 'Hajdú-Bihar' );
insert into Geo (city, county ) VALUES('Hajdúszoboszló', 'Hajdú-Bihar' );



SELECT 
place_of_residence,
religion,
count(religion)  
FROM lta_main WHERE place_of_residence in 
(SELECT city FROM geo WHERE county = 'Hajdú-Bihar' order by city)
group by place_of_residence, religion
ORDER BY place_of_residence;

select extract('year' from date_of_birth) from lta_main fetch first 25 rows only;
select CAST(SUBSTRING(id,0,4) as INTEGER) from lta_main fetch first 25 rows only;




select crime, sex, CAST(SUBSTRING(id,1,4)as INTEGER)  - extract('year' from date_of_birth) as age, count(crime) from lta_main where place_of_residence = 'Debrecen' and crime is not null and date_of_birth is not null group by crime, sex, age  order by count(crime) desc;


