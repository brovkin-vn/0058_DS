select f.flight_id,
        f.flight_no,
        f.scheduled_departure,
        f.scheduled_arrival,
        f.departure_airport,
        f.arrival_airport,
        a.airport_name,
        a.city,
        a.longitude,
        a.latitude,
        a.timezone,
        f.status,
        f.aircraft_code,
        ac.model,
        ac.range,
        f.actual_departure,
        f.actual_arrival,
        tf.fare_conditions as class,
        count(s.seat_no) as total_seats,
        count(tf.fare_conditions) as seats_paid,
        sum(tf.amount) as total_paid,
        sum(tf.amount) / count(tf.fare_conditions) * count(s.seat_no) as possible_total
from dst_project.flights as f
        left join dst_project.ticket_flights as tf on tf.flight_id = f.flight_id
        left join dst_project.airports as a on a.airport_code = f.arrival_airport
        left join dst_project.aircrafts as ac on ac.aircraft_code = f.aircraft_code
        left join dst_project.seats as s on s.aircraft_code = f.aircraft_code
where f.departure_airport = 'AAQ'
        and f.status != 'Cancelled'
group by f.flight_id,
        a.airport_name,
        a.city,
        a.longitude,
        a.latitude,
        a.timezone,
        ac.model,
        ac.range,
        tf.fare_conditions
order by f.flight_id