import pyrealsense2 as rs
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Configure depth stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start streaming
pipeline.start(config)

try:
    # Wait for a coherent pair of frames: depth and color
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()

    # Convert images to numpy arrays
    depth_image = np.asanyarray(depth_frame.get_data())

    # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    # Display the resulting frame with matplotlib using 'jet' colormap
    plt.imshow(depth_colormap)
    plt.show()

finally:

    # Stop streaming
    pipeline.stop()

