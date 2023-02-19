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

    # Get the calendars
    calendars = ics_calendar.load_calendars()

    current_y = 0

    # DOTW Header
    dotw_header = dotw.dotw_header()
    current_y += 720
    a.paste(dotw_header, (0, current_y))


    for current_week in range(0,4):
        items = current_week_array(offset=current_week)
        wk = dotw.dotw_header(items)
        current_y += 140
        a.paste(wk, (0, current_y))

        wk_arr = []
        for day in current_week_array(datetimeonly=True, offset=current_week):
            z = ics_calendar.load_events(day, calendars)
            x = week.generate_day(z, minimal=(current_week == 0))
            wk_arr.append(x)

        d = week.generate_week(wk_arr)

        current_y += wk.size[1]

        a.paste(d, (0, current_y))



    a.save("result.jpg")
