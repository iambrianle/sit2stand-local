# Sit2Stand Local

This repository provides custom code to run the Sit2Stand library, enabling analysis of sit-to-stand movements using OpenPose.

## Prerequisites

- OpenPose must be installed to extract pose data from videos. A [OpenPose fork](https://github.com/franzcrs/openpose-with-caffe-for-MacM1?tab=readme-ov-file) is recomended.
- Python dependencies listed in the `requirements.txt` file need to be installed.

## Installation

1. Clone the repository and navigate into the project directory.
2. Install the required Python dependencies.
3. Install OpenPose by following the instructions in the recommended repository or the official documentation.

## Usage

1. Run the main script (main.py) on a video file to generate JSON files containing pose data.
2. Process the JSON files using the preparation script (prepare.py) to create a NumPy file.
3. Modify the `links.csv` file to ensure the file names and paths are correctly set.
4. Use the metrics script (getmetrics.py) to generate final graphs, charts, and a results file based on the processed data.

## Configuration

All script paths must be updated to match the system’s directory structure. Ensure that file paths in all Python scripts and `links.csv` are correctly set before running the analysis.

## Acknowledgments

This project was inspired by and builds upon work from [Stanford NMBL's Sit2Stand Analysis](https://github.com/stanfordnmbl/sit2stand-analysis). The `utils.py`, `getmetrics.py` and `prepare.py` scripts were modified from their original implementation to run locally.
