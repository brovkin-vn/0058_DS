WITH F AS
  (SELECT  flight_id,
        flight_no,
        scheduled_departure,
        scheduled_arrival,
        departure_airport,
        arrival_airport,
        actual_departure,
        actual_arrival
   FROM dst_project.flights t
   WHERE departure_airport = 'AAQ'
     AND (date_trunc('month', scheduled_departure) in ('2016-01-12',
                                                       '2017-01-01',
                                                       '2017-02-01'))
     AND status not in ('Cancelled') ),
A AS
(SELECT * FROM dst_airport WHERE )

SELECT *
FROM F