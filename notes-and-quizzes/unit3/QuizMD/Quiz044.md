# Quiz 044

## Prompt
Download the database cmoon.db from the learning log and write the SQL statements to solve the questions.

## Code Structure

### SQL Script
```.sql
SELECT name from sqlite_master where type = "table";

select count(*) from INHABITANT where gender = "Male" and state = "Friendly";

select avg(gold) from INHABITANT group by villageid;

select count(*) from ITEM where item like "A%";

select count(distinct job) from INHABITANT;

select item from ITEM, INHABITANT where INHABITANT.personid = ITEM.owner and INHABITANT.job = "Herbalist";
```

## Evidence

![](/Assets/Quiz044_EvidenceA.jpg)
*Fig.1* **Image showing result of the first query**

![](/Assets/Quiz044_EvidenceB.jpg)
*Fig.2* **Image showing result of the second query**

![](/Assets/Quiz044_EvidenceC.jpg)
*Fig.3* **Image showing result of the third query**

![](/Assets/Quiz044_EvidenceD.jpg)
*Fig.4* **Image showing result of the fourth query**

![](/Assets/Quiz044_EvidenceE.jpg)
*Fig.5* **Image showing result of the fifth query**

![](/Assets/Quiz044_EvidenceF.jpg)
*Fig.6* **Image showing result of the sixth query



