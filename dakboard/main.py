"""
Generates the result.jpg file directly
"""
from generate import *

if __name__ == "__main__": # pragma: no cover
    # Generate base and top image
    a = create_image_combine_top(os.path.join("photos", "test-top-edit.png"))

    # Get weather and temperature
    ## Put onto top image
    a = generate_time(a)
    a = generate_date(a)

    # Get time and date
    ## Put onto top image
    a = generate_temperature(a, weather.get_current_temperature())
    a = generate_weather_icon(a, weather.get_current_weather())

    dotw_header = dotw.dotw_header()
    a.paste(dotw_header, (0, 720))

    items = current_week_array()

    first_week = dotw.dotw_header(items)
    a.paste(first_week, (0, 720 + 140))

    # Generate First week
    first_week_arr = []
    for day in current_week_array(datetimeonly=True):
        z = ics_calendar.load_events(day)
        x = week.generate_day(z)
        first_week_arr.append(x)

    d = week.generate_week(first_week_arr)

    a.paste(d, (0, 720 + 140 + first_week.size[1]))

    a.save("result.jpg")
