create index parcel_geom_index
on assessors_2024_geo
using gist (geometry);
