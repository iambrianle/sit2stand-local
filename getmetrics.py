
from utils import process_subject, run_openpose
import os
import numpy as np
import pandas as pd
import pickle
import traceback
from utils import videometa

subjects = [r.replace(".npy","") for r in os.listdir("videos/np/")]

# Initialize empty list to hold results
all_res = []
skipped = []


# Process only the first 3 subjects
for subjectid in subjects:  # Slicing the first 3 items
    print(subjectid)
    try:
        results = process_subject(subjectid)
    except Exception as e:
        traceback.print_exc()
        skipped.append(subjectid)
        print("Skipped " + subjectid)
        continue
    all_res.append(results)

print(skipped)

for s in skipped:
    print(s)

res_df = pd.DataFrame(all_res)
res_df

res_df.to_csv("results-20220420.csv")
