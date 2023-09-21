# Intel RealSense

## Configuraion 
- Jetson nano B01
- Intel RealSense D435i
- Ubuntu 18.04.06 LTS
- GNU/Linux 4.9.140-tegra aarch64

### Python Binding

1. 설치 1
    1. pip install pyrealsense2
2. 설치 2
    1. sudo apt-get update
    2. sudo apt-get upgrade
    3. sudo apt-get install libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
    4. sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev
    5. sudo apt-get install cmake python3 python3-dev python3-pip
    6. git clone https://github.com/IntelRealSense/librealsense.git
    7. sudo apt-get install libudev-dev
    8. make
    ```
    cd librealsense  # Move into the cloned directory
    mkdir build && cd build  # Create a build directory and move into it
    cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true  # Run CMake to configure the project
    make && sudo make install  # Build and install the project
    ```



  
 

### Python Example
1. 
2. 
3. 
4. 
