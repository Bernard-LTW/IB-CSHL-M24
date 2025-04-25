SELECT name from sqlite_master where type = "table"

select count(*) from INHABITANT where gender = "Male" and state = "Friendly"

select avg(gold) from INHABITANT group by villageid

select count(*) from ITEM where item like "A%"

select job, count(job) from INHABITANT group by job

select count(distinct job) from INHABITANT

select item from ITEM, INHABITANT where INHABITANT.personid = ITEM.owner and INHABITANT.job = "Herbalist"