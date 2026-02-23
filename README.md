# frog-behavior-pipeline
An automated computer vision framework for quantifying species-specific parental care and recruitment behavior in *Ranitomeya imitator* and *Ranitomeya variabilis* nurseries.

## Project Overview
This pipeline automates the labor-intensive process of scoring motion-activated nursery recordings. It translates raw video data into standardized behavioral ethograms, allowing for high-throughput analysis of parental investment.

### 1. R. variabilis Mode (Uniparental Focus)
Focuses on paternal attendance and occupancy within experimental conditions.
- **Parental Attendance:** Quantifies time spent by the father perching on the rim, inside, or immediately above a cup or the **Parent Shelter**.
- **Condition Monitoring:** Tracks male interaction with tadpoles to measure care effort across different treatment sites.

### 2. R. imitator Mode (Biparental & Recruitment Focus)
Tracks complex social coordination and parent-offspring communication.
- **Biparental Attendance:** Tracks both male and female occupancy across all ROIs.
- **Tadpole Behavior:** Detection of **Tadpole Begging Bouts** (extended vibrational "twitching") directed at a parent.
- **Feeding Recruitment:** Monitors the sequence of Male Calling (vocal sac inflation) → Female Approach → **Trophic Egg Feeding** (female posterior dipping).

## Experimental Design & ROI Mapping
The nursery setup consists of 5 primary Regions of Interest (ROIs). The pipeline automatically maps behavioral data to these specific experimental treatments:

| ROI | Label | Experimental Condition | Description |
| :--- | :--- | :--- | :--- |
| **Cup 1** | Treatment A | **Parental (P)** | The parent's own biological offspring. |
| **Cup 2** | Treatment B | **Foster (F)** | A non-biological (translocated) tadpole. |
| **Cup 3** | Treatment C | **Parental (P)** | Duplicate biological offspring site. |
| **Cup 4** | Treatment D | **Foster (F)** | Duplicate non-biological offspring site. |
| **Shelter** | Home Base | **N/A** | Black film canister retreat for the parents. |

## Data Recording & Scoring Standards
The pipeline strictly adheres to the Yang Lab "Dash vs. Comma" scoring protocol for seamless integration into research templates:

- **Continuous Contact (Dash `-`):** If a parent is detected in the same ROI across sequential motion-activated videos, the system merges the events (e.g., `23-24`).
- **Separate Visits (Comma `,`):** Non-sequential videos are recorded as distinct arrival events (e.g., `05, 12`).
- **Bout Grouping (Brackets `[]`):** For *R. imitator*, sequences of begging and recruitment occurring in sequential videos are grouped into single behavioral units.
- **Total Time Calculation:** The system calculates "Unique Minutes" of contact, ensuring overlapping parental presence is not double-counted.

## Tech Stack
- **Vision:** [YOLOv8](https://github.com/ultralytics/ultralytics) (Object Detection) & [ByteTrack](https://github.com/ifzhang/ByteTrack) (Individual Tracking)
- **Interface:** [Streamlit](https://streamlit.io/) (For ROI/Cup Setup UI) & [Click](https://click.palletsprojects.com/) (For Batch Processing CLI)
- **Spatial Analysis:** [Supervision](https://github.com/roboflow/supervision) (For ROI mapping of Cups 1-4 & Shelter)
- **Temporal Logic:** Custom Python TimeDelta logic for "Dash vs. Comma" stay-duration aggregation.
- **Behavioral Logic:** State-machine architecture to detect *R. imitator* feeding recruitment bouts and tadpole begging.
- **Data Management:** [Pandas](https://pandas.pydata.org/) (Standardized Lab Excel/CSV output) & [PyYAML](https://pyyaml.org/) (Configuration Management)