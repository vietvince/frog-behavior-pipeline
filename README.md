# frog-behavior-pipeline
Automated behavioral analysis of poison frog parental care using computer vision and deep learning.

## Project Overview
This project aims to quantify parental care and detect recruitment-related behavioral events in poison frog nurseries. Using fixed-camera recordings, the pipeline automatically processes videos to generate time-resolved biological data, including:
- **Parental Attendance:** Visit frequency and duration per cup.
- **Tadpole Behavior:** Detection of tadpole begging bouts.
- **Recruitment Events:** Success/failure of feeding coordination between parents.

## Tech Stack
- **Detection and Trackig:** [YOLOv8](https://github.com/ultralytics/ultralytics) + [ByteTrack](https://github.com/ifzhang/ByteTrack)
- **Spatial Analysis:** [Supervision](https://github.com/roboflow/supervision) for Region of Interest (ROI) mapping.
- **Data Management:** [Pandas](https://pandas.pydata.org/) for biological metric logging.
- **Development:** Python 3.10+ (Cross-platform: Linux/Windows).