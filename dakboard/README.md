## Personal Dakboard App
- Going to create image 
- Display image on the given dakboard with the following command:
  - ` fbi -d /dev/fb0 -T 1 --noverbose temp.jpg`

- ChatGPT says to use `-a --autorotate` to rotate 90 degrees clockwise

## OpenWeather API

## Google Calendar API
### To get a Google API key, you need to perform the following steps:

Go to the Google Cloud Console (https://console.cloud.google.com/).
Click the project drop-down and select or create the project for which you want to add an API key.
Click the hamburger menu and select APIs & Services > Credentials.
Click Create credentials > API key. The API key created dialog displays your newly created API key.
Note: To restrict usage of your API key to specific Google APIs, you can use the Cloud Console to enable APIs and set usage restrictions on the API key.

This API key can be used to access various Google services such as Google Maps, Google Calendar, and others. To use the Google Calendar API, you need to enable the Google Calendar API in the Google Cloud Console and obtain an API key.

### To restrict an API key to only access the Google Calendar API and related services, you need to perform the following steps:

Go to the Google Cloud Console (https://console.cloud.google.com/).
Click the project drop-down and select or create the project that contains the API key you want to restrict.
Click the hamburger menu and select APIs & Services > Library.
In the search box, enter "Google Calendar API" and click the result.
Click the Enable button.
Go back to the API Library, and search for other services that you want to enable (such as Google Calendar API).
Repeat step 5 to enable these APIs.
Go to the APIs & Services > Credentials page.
Click the Edit button for the API key you want to restrict.
In the Key restriction section, set Application restrictions to HTTP referrers.
Add the Referrers. The referrers you add will be able to use the API key.
Click Save.