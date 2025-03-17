import os
import os.path

def run_openpose(path, fps=10):
    # Create necessary directories in the current working directory
    input_dir = "input"
    output_dir = "output"
    keypoints_dir = os.path.join(output_dir, "keypoints")
    plots_dir = os.path.join(output_dir, "plots")

    # Ensure directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(keypoints_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    # Check video rotation with ffprobe
    CMD = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1 -i {}".format(path)
    rotate = os.popen(CMD).read().strip()

    # Convert video to specified fps and handle rotation if present
    processed_path = os.path.join(input_dir, "processed_input.mp4")
    if rotate:
        # If rotated, correct rotation and set to specified fps
        CMD = "ffmpeg -y -i {} -r {} -vf 'rotate={}:c=black' {}".format(path, fps, rotate, processed_path)
    else:
        # If not rotated, just set to specified fps
        CMD = "ffmpeg -y -i {} -r {} {}".format(path, fps, processed_path)
    os.system(CMD)

    # Define absolute paths for OpenPose
    openpose_dir = "openpose-with-caffe-for-MacM1"
    openpose_bin = os.path.join(openpose_dir, "build/examples/openpose/openpose.bin")
    model_folder = os.path.join(openpose_dir, "models")

    # Run OpenPose command with model folder specified on the processed video
    output_video = os.path.join(output_dir, f"output_{fps}fps.mp4")  # Include fps in output filename
    openpose_cmd = (
        'rm -r {}/* ; '  # Clear output directory
        'mkdir -p {} ; '  # Recreate plots directory
        '{} '            # Absolute path to openpose.bin
        '--model_folder {} '  # Specify model folder
        '--video {} '
        '--display 0 '
        '--write_json {} '
        '--write_video {}'
    ).format(
        output_dir, 
        plots_dir, 
        openpose_bin, 
        model_folder,
        processed_path,  # Use the processed video with specified fps
        keypoints_dir, 
        output_video
    )
    os.system(openpose_cmd)

# Example usage
# run_openpose("1ovgasC1.mp4")  # Default 10 fps
run_openpose("1ovgasC1.mp4", fps=30)  # Example with 30 fps