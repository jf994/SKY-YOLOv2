from oologic.event import Event
from oologic.create_italy_france import createItaFra


class Test:
    match = createItaFra()
    event1 = Event("00:15:36", "Red_Card", match.guest_team.coach)
    event2 = Event("00:18:34", "Bella parata", match.home_team.rooster[0])
    event3 = Event("00:35:22", "Goal su punizione", match.home_team.rooster[6])
    match.home_team.score_goal()
    match.event_list.append(event1)
    match.event_list.append(event2)
    match.event_list.append(event3)

    match.json_and_txt_create()
