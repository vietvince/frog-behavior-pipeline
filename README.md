# frog-behavior-pipeline
An automated computer vision tool for quantifying parental care and recruitment behaviors in *Ranitomeya imitator* and *Ranitomeya variabilis*.

## Project Overview
This pipeline processes motion-activated nursery videos to extract high-resolution behavioral data. It is designed to handle two distinct biological scenarios:

### 1. R. variabilis Mode (Uniparental Focus)
Focuses on paternal attendance and occupancy within experimental cup conditions.
- **Parental Attendance:** Quantifies how often the father frog visits each cup and the total duration of stay.
- **Experimental Mapping:** Links behavior to specific cups, where each cup represents a unique experimental condition.

### 2. R. imitator Mode (Biparental & Recruitment Focus)
Tracks complex social interactions and biparental coordination.
- **Biparental Attendance:** Tracks both male and female visit frequency and duration per cup.
- **Tadpole Behavior:** Detection and timestamping of specific **tadpole begging bouts** (vibratory motion).
- **Recruitment Events:** Logs the success or failure of feeding coordination (the sequence of Dad arrival → Tadpole Begging → Mom arrival).

## Tech Stack
- **Vision:** [YOLOv8](https://github.com/ultralytics/ultralytics) (Object Detection) & [ByteTrack](https://github.com/ifzhang/ByteTrack) (Individual Tracking)
- **Interface:** [Streamlit](https://streamlit.io/) (For ROI/Cup Setup) & [Click](https://click.palletsprojects.com/) (For Batch Processing CLI)
- **Spatial Analysis:** [Supervision](https://github.com/roboflow/supervision) (For Region of Interest/Cup mapping)
- **Data Management:** [Pandas](https://pandas.pydata.org/) (CSV/Excel output) & [PyYAML](https://pyyaml.org/) (Configuration Management)
- **Environment:** Python 3.10+ (Cross-platform Linux Mint / Windows)