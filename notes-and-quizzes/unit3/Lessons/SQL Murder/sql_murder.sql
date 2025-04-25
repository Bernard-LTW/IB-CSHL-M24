select * from crime_scene_report where city = "SQL City" and type = "murder" and date = 20180115

select * from person where address_street_name = "Northwestern Dr" order by address_number desc

select * from person where id = 14887

select * from person where address_street_name = "Franklin Ave" and name like "Annabel%"

select * from person where id = 16371

select * from interview where person_id = 14887 or person_id = 16371

select * from get_fit_now_member, drivers_license where drivers_license.plate_number like "H42W%" and get_fit_now_member.id like "48Z%" and get_fit_now_member.membership_status = "gold"

select * from get_fit_now_member,get_fit_now_check_in where get_fit_now_member.person_id = 16471 and get_fit_now_check_in.membership_id = get_fit_now_member.id and get_fit_now_check_in.check_in_date = 20180109

select * from get_fit_now_member where person_id = 16371

select * from get_fit_now_check_in where membership_id = 90881

select * from get_fit_now_check_in, get_fit_now_member where check_in_date = 20180109 and get_fit_now_check_in.membership_id = get_fit_now_member.id and get_fit_now_member.membership_status = "gold" and get_fit_now_member.id like "48%"

select * from person where name = "Joe Germuska" or name = "Jeremy Bowers"

select * from facebook_event_checkin where person_id = 28819 or person_id = 67318

INSERT into solution values (1, "Jeremy Bowers")
SELECT * FROM solution

select * from interview where person_id = 67318

select * from person, drivers_license where drivers_license.car_make = "Tesla" and drivers_license.car_model = "Model S" and drivers_license.hair_color = "red" and drivers_license.height like 65 and drivers_license.gender = "female"


