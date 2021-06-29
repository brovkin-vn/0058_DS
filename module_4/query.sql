WITH F AS
  (SELECT flight_id,
          flight_no,
          scheduled_departure,
          scheduled_arrival,
          departure_airport,
          arrival_airport,
          actual_departure,
          actual_arrival,
          status,
          aircraft_code,
          airport_name,
          airport_code,
          city,
          longitude,
          latitude,
          timezone
   FROM dst_project.flights t
   JOIN dst_project.airports t2 ON t2.airport_code = t.arrival_airport
   WHERE departure_airport = 'AAQ'
     AND (date_trunc('month', scheduled_departure) in ('2016-01-12',
                                                       '2017-01-01',
                                                       '2017-02-01'))
     AND status not in ('Cancelled') ),
     AC AS
  (SELECT aircraft_code,
          model,
          RANGE,
          sum(business_seats) business_seats,
          sum(comfort_seats) comfort_seats,
          sum(economy_seats) economy_seats,
          sum(total_seats) total_seats
   FROM
     (SELECT t1.aircraft_code,
             model,
             RANGE,
             CASE
                 WHEN fare_conditions = 'Business' THEN 1
                 ELSE 0
             END AS business_seats,
             CASE
                 WHEN fare_conditions = 'Comfort' THEN 1
                 ELSE 0
             END AS comfort_seats,
             CASE
                 WHEN fare_conditions = 'Economy' THEN 1
                 ELSE 0
             END AS economy_seats,
             1 AS total_seats
      FROM dst_project.aircrafts t1
      JOIN dst_project.seats t2 ON t1.aircraft_code = t2.aircraft_code) t
   GROUP BY aircraft_code,
            model,
            RANGE),
     TF AS
  (SELECT flight_id,
          sum(business_amount) business_amount,
          sum(comfort_amount) comfort_amount,
          sum(economy_amount) economy_amount,
          sum(total_amount) total_amount
   FROM
     (SELECT flight_id,
             fare_conditions,
             CASE
                 WHEN fare_conditions = 'Business' THEN amount
                 ELSE 0
             END AS business_amount,
             CASE
                 WHEN fare_conditions = 'Comfort' THEN amount
                 ELSE 0
             END AS comfort_amount,
             CASE
                 WHEN fare_conditions = 'Economy' THEN amount
                 ELSE 0
             END AS economy_amount,
             amount total_amount
      FROM dst_project.ticket_flights) t
   GROUP BY flight_id)
SELECT F.flight_id,
       flight_no,
       scheduled_departure,
       scheduled_arrival,
       departure_airport,
       arrival_airport,
       actual_departure,
       actual_arrival,
       actual_arrival - actual_departure total_time,
       status,
       airport_name,
       airport_code,
       city,
       longitude,
       latitude,
       timezone,
       F.aircraft_code,
       model,
       RANGE,
       business_seats,
       comfort_seats,
       economy_seats,
       total_seats ,
       business_amount,
       comfort_amount,
       economy_amount,
       total_amount
FROM F
JOIN AC ON AC.aircraft_code = F.aircraft_code
JOIN TF ON TF.flight_id = F.flight_id 

