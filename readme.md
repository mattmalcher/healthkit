# Playing with Healthkit data

Apple devices collect a lot of information about you, I want to take a peek at at. 

## Areas for Analysis
Some ideas:

* analysis of relationship between cycling speed and journey time (i.e. are you just getting to traffic lights sooner?)
* Which factors can be used to predict an increase VO2 max?
    * daily steps?
    * consistent running streaks?
* can I make a pretty plot of where I have walked (table contains millions of points)

## Tools to Try

* [datasette & spatialite](https://docs.datasette.io/en/stable/spatialite.html)
* [grafana](https://www.ivaylopavlov.com/charting-apple-healthkit-data-in-grafana/)
* [bokeh](https://github.com/openPfizer/DigitalHealthData/blob/master/AppleWatchLib/plot_apple_watch_data.py)
* [R & ggplot2](https://www.mitchhenderson.org/2020/05/visualising-data-measured-from-activity-watches/)

## Other Ideas
* make a docker container that contains all the bits for a healthkit data exploring app.

# Links
* [Apple Healthkit Docs](https://developer.apple.com/documentation/healthkit)
* [Q: problem with import of XML Apple HealthKit Export Version: 12](https://discussions.apple.com/thread/254202523)
* [automated-exporting-of-health-kit-data](https://ianbelcher.me/tech-blog/automated-exporting-of-health-kit-data)


# Healthkit Data Issues

```sh
virtualenv ~/virtualenv/healthkit
source ~/virtualenvs/healthkit/bin/activate
pip install datasette healthkit_to_sqlite
```

## Attempt 1

```sh
healthkit-to-sqlite export.zip healthkit.db
```

This resulted in some errors about invalid syntax. Looks like the v12 of the healthkit data has some issues!

## The fix

This thread here put me on the right track
https://discussions.apple.com/thread/254202523.


Install xmllint
```sh
sudo apt-get install libxml2-utils
```
Use xmllint to point you at the errors

```sh
unzip export.zip
xmllint apple_health_export/export.xml 
```

Edit the xml in `vi` to remove the errors - a missing bracket, some invalid sections like in the link
* `: set number`
* esc + {line_no} + shift-G to jump



