
#### Summery

This model is for Trajectory Preprocessing, there are five important steps:

1. Noise filtering
2. Stay point detection
3. Trajectory compression
4. Trajectory Segmentation
5. Map matching


#### 1. StayPoint generate

Because we need split user-date's data, so we code plt2csv2.py to generate user-date's csv and user-date's json

```python

python plt2csv2.py

```

Then It will generate many user-date's file


#### 2. allstayPoints.json generate

```python

python AllUserDetection.py

```


#### 3。 finalAllStayPoints.json generate

```python

python StayPointsCluster.py

```





















