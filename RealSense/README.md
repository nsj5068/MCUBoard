# Intel RealSense

## Configuraion 
- Jetson nano B01 4GB RAM
- Intel RealSense D435i
- Ubuntu 18.04.06 LTS
- GNU/Linux 4.9.140-tegra aarch64

### Python Binding

1. 설치 1
    1. pip install pyrealsense2
2. 설치 2
    1. `sudo apt-get update`
    2. `sudo apt-get upgrade`
    3. `sudo apt-get install libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev`
    4. `sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev`
    5. `sudo apt-get install cmake python3 python3-dev python3-pip`
    6. `git clone https://github.com/IntelRealSense/librealsense.git`
    7. `sudo apt-get install libudev-dev`
    8. `cd librealsense`
    9. `mkdir build && cd build`
    10. `cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true` : 파이썬 바인딩을 해야 관련된 .so 파일이 나타남. 
    11. `make && sudo make install` : 본 보드 기준, 걸리는 시간 = 약 2시간
        - 혹시 빌드나, make 도중 오류가 걸렸을 경우 취해야 할 행동
            1. `cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true` or `make && sudo make install` 를 다시 시도했을 때, 별 문제 없이 되는 경우
                - 메모리 부족으로 인한 문제가 대다수임.
            2. 위 1번 코드를 다시 실행 했을 때 안되는 경우
                - cmake 설정에 문제가 있다거나, gcc 문제일 가능성이 큼.
                - 자잘한 에러들을 다 해결한 후에 build 이전 파일로 돌아가서 (`/librealsense`) 다음 코드를 실행.
                - `sudo rm -rf /build` : build 파일 삭제
                - 다시 위 과정 중 `mkdir build && cd build` 코드 부터 다시 실행.
                - ~~최악의 경우 설치하는 데만 3~4시간 정도 걸림~~    

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
