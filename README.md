# Squirrel-Tracker

## Introduction
This is a web application which is developed using Django to keep track of all the reported squirrels in Central Park. A 2018 Central Park Squirrel Census is uploaded to the database. The website allows the viewers to add unique squirrels, to update existing squirrels information, to view the general stats for the squirrels, and to view all the reported squirrels on Central Park's map. 

## Contributors information

Project Group: Jing & Jiaqi, Section 1

Name: [Jiaqi Yang,Jing Xiao]

UNIs: [jy3094, jx2422]


## Detailed infomation

The map for the first 100 sightings of squirrels can be found here:
```
/map/
```

List of all the squirrels in the database can be found here:
```
/sightings/
```

To update a particular squirrels sighting information, go to:
```
/sightings/<unique-squirrel-id>
```

To create a new squirrel sightings, go to:
```
/sightings/add/
```

Stats for all the squirrel sightings can be found here:
```
/sightings/stats/
```

