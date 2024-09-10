FROM python:3.12.3
RUN mkdir track-coach-timer-race-service
COPY . /track-coach-timer-race-service/
WORKDIR /track-coach-timer-race-service
RUN pip install -r requirements.txt
WORKDIR /track-coach-timer-race-service/track_coach_timer_race_service
RUN python manage.py makemigrations
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
WORKDIR /track-coach-timer-race-service/track_coach_timer_race_service/