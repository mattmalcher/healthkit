Getting the data into datasette is a good start but I think what I really want to do is create some maps.

datasette has some integration with spatialite that I want to try out, but I also want to avoid installing things on my host machine.

So, I think I want to make a container to try this stuff out. Happily simonw has an [example of creating a datasette spatialite API](https://github.com/simonw/timezones-api/blob/main/Dockerfile) that I can steal.

The main datasette docs have an example of how to [make a spatial index using existing lat/long columns](https://docs.datasette.io/en/stable/spatialite.html#spatial-indexing-latitude-longitude-columns).

And, looking at the output of running the [`healthkit-to-sqlite`](https://datasette.io/tools/healthkit-to-sqlite) plugin I can see that I have a `workout_points` table with the kind of thing I want:
*  	date
*	**latitude**
*	**longitude**
*	altitude
*	horizontalAccuracy
*	verticalAccuracy
*	course
*	speed
*	workout_id

# Setup
I want to be able to iterate on the visualisation so I dont want to have to keep re-importing the data. 

But, I dont want to:
* modify my `healthkit.db` database
* recreate the 

I think I could do something like:

* Have a single Dockerfile with all the dependencies I need

* `docker-compose -f prep_spatialite.yml up`
    * open a new database to hold my new spatialite tables
    * attach the existing healthkit.db database
    * use a query to create a new spatialite table in the new database using the existing database

* `docker-compose -f docker_compose.yml up`
    * read prepped spatialite db
    * host it using datasette and show some maps (write my own extension to do this?)


Before working on the second compose file I think I would want to do some exploration in QGIS or similar to understand how to work with the point data in this table - do I need to turn it into paths for example? 
