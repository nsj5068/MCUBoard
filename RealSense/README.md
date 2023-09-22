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
    cd librealsense  
    mkdir build && cd build  
    cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true  
    make && sudo make install  
    ```
    
3. Error
    1. gcc error
        1. aarch64-linux-gnu-gcc error
           - 임시 방편 해결법 : 터미널 창에서 다음 코드를 그대로 치고 엔터를 누른다.
           - `export CC=/usr/bin/gcc`
           - aarch64-linux-gnu-gcc이 컴파일러를 일반 gcc 컴파일러로 바꾼다는 의미...
             

    2. Memory 부족 문제
        1. Swapfile
            - 설명 : 저장 공간을 임시 메모리로 쓰는 방법
            - 실행법 :
               1. `free -m` : 현재 시스템의 스왑 사이즈 확인
               2. `sudo fallocate -l 4G /swapfile` : 4GB 크기의 스왑 파일 생성
               3. `sudo chmod 600 /swapfile` : 스왑 파일 권한 설정
               4. `sudo mkswap /swapfile` : 스왑 영역으로 설정
               5. `sudo swapon /swapfile` : 스왑 파일 등록
               6. `echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab` : 부팅 시 마다 자동 적용

 

### Python Example
1. 
2. 
3. 
4. 
