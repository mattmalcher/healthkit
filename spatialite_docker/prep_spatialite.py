import sqlite3

conn = sqlite3.connect("museums.db")
# Lead the spatialite extension:
conn.enable_load_extension(True)
conn.load_extension("/usr/local/lib/mod_spatialite.dylib")
# Initialize spatial metadata for this database:
conn.execute("select InitSpatialMetadata(1)")
# Add a geometry column called point_geom to our museums table:
conn.execute(
    "SELECT AddGeometryColumn('museums', 'point_geom', 4326, 'POINT', 2);"
)
# Now update that geometry column with the lat/lon points
conn.execute(
    """
    UPDATE museums SET
    point_geom = GeomFromText('POINT('||"longitude"||' '||"latitude"||')',4326);
"""
)
# Now add a spatial index to that column
conn.execute(
    'select CreateSpatialIndex("museums", "point_geom");'
)
# If you don't commit your changes will not be persisted:
conn.commit()
conn.close()
