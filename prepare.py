import os
import traceback
import json
import numpy as np

videos = ["1ovgasC1"]
print("Videos to process:", videos)

output_np_dir = "videos/np"
os.makedirs(output_np_dir, exist_ok=True)

def json2np(keypoints_dir, subjectid):
    json_files = sorted([f for f in os.listdir(keypoints_dir) if f.endswith(".json")])
    if not json_files:
        raise ValueError(f"No JSON files found in {keypoints_dir}")
    
    frames = []
    for json_file in json_files:
        with open(os.path.join(keypoints_dir, json_file), "r") as f:
            data = json.load(f)
            if not data["people"]:
                keypoints = np.zeros((25, 3))
            else:
                keypoints = np.array(data["people"][0]["pose_keypoints_2d"]).reshape((25, 3))
            frames.append(keypoints)
    
    # Convert to (n_frames, 25, 3) then flatten to (n_frames, 75)
    arr = np.array(frames)  # (n_frames, 25, 3)
    return arr.reshape(arr.shape[0], -1)  # (n_frames, 75)

for subjectid in videos:
    try:
        keypoints_dir = "output/keypoints"
        print(f"Converting keypoints for {subjectid} from {keypoints_dir}")
        if not os.path.exists(keypoints_dir):
            raise FileNotFoundError(f"Keypoints directory {keypoints_dir} does not exist")
        res = json2np(keypoints_dir, subjectid)
        np.save(f"{output_np_dir}/{subjectid}.npy", res)
        print(f"Saved NumPy array to {output_np_dir}/{subjectid}.npy")
    except Exception as e:
        print(f"Error converting {subjectid}: {str(e)}")
        traceback.print_exc()