from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd().parent.parent)

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE]

# Images config
IMAGES_DIR = '../' 
DEFAULT_IMAGE = IMAGES_DIR + 'Data/' + 'case1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR + 'Output/' + 'prediction/'+ 'case1.png'

# Result Images


# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'YOLOV8.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'segment.pt'
# print(ROOT)
