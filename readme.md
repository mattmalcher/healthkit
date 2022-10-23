# Playing with Healthkit data

Apple devices collect a lot of information about you, I want to take a peek at at. 

## Topics
Some ideas:

* analysis of relationship between cycling speed and journey time (i.e. are you just getting to traffic lights sooner?)
* Which factors can be used to predict an increase VO2 max?
    * daily steps?
    * consistent running streaks?
* can I make a pretty plot of where I have walked (table contains millions of points)

## Tools to try

* [datasette & spatialite](https://docs.datasette.io/en/stable/spatialite.html)
* [grafana](https://www.ivaylopavlov.com/charting-apple-healthkit-data-in-grafana/)
* [bokeh](https://github.com/openPfizer/DigitalHealthData/blob/master/AppleWatchLib/plot_apple_watch_data.py)
* [R & ggplot2](https://www.mitchhenderson.org/2020/05/visualising-data-measured-from-activity-watches/)

## Other Ideas
* make a docker container that contains all the bits for a healthkit data exploring app.

# Setup

```sh
virtualenv ~/virtualenv/healthkit
source ~/virtualenvs/healthkit/bin/activate
pip install datasette healthkit_to_sqlite
```

# Attempt 1

```sh
healthkit-to-sqlite export.zip healthkit.db
```

This resulted in some errors

# The fix
Looks like the v12 of the healthkit data has some issues

This thread here put me on the right track
https://discussions.apple.com/thread/254202523


Install xmllint
```sh
sudo apt-get install libxml2-utils
```
Use xmllint to point you at the errors

```sh
unzip export.zip
xmllint apple_health_export/export.xml 
```

edit the xml in vi to remove the errors - a missing bracket, some invalid sections like in the link
* `: set number`
* esc + {line_no} + shift-G to jump



# Start Datasette

```sh
datasette healthkit.db 
``` 




