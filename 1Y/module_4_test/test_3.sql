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
          fare_conditions,
          fare_conditions_seats,
          sum(fare_conditions_seats) over(PARTITION BY aircraft_code) total_seats
   FROM
     (SELECT t1.aircraft_code,
             model,
             RANGE,
             fare_conditions,
             COUNT(seat_no) fare_conditions_seats
      FROM dst_project.aircrafts t1
      JOIN dst_project.seats t2 ON t1.aircraft_code = t2.aircraft_code
      GROUP BY t1.aircraft_code,
               model,
               RANGE,
               fare_conditions) tt
   ORDER BY 1),
     TF AS
  (SELECT flight_id,
          fare_conditions,
          fare_conditions_total_amount,
          sum(fare_conditions_total_amount) over(PARTITION BY flight_id) total_amount
   FROM
     (SELECT flight_id,
             fare_conditions,
             sum(amount) fare_conditions_total_amount
      FROM dst_project.ticket_flights -- WHERE flight_id = 136122

      GROUP BY flight_id,
               fare_conditions) tt)
SELECT *
FROM F
JOIN AC ON AC.aircraft_code = F.aircraft_code
JOIN TF ON TF.flight_id = F.flight_id
AND TF.fare_conditions = AC.fare_conditions
WHERE F.flight_id = 136122