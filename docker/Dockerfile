FROM ros:noetic

LABEL maintainer="Kevin Vega <A01612430@tec.mx>"

# Expose ports
EXPOSE 6080 80 22 4800

RUN apt-get update -qq && \
    apt-get install -y \
    build-essential \
    nano \
    git \
    autoconf \
    libtool \
    python3-pip \
    mesa-utils \
    ros-noetic-cv-bridge \  
    && rm -rf /var/lib/apt/lists/*

# Set up volumes
VOLUME /dev/shm

COPY library/ library/

# Build the library
WORKDIR /library
RUN g++ -c -fPIC multiplier.cpp -o multiplier.o
RUN g++ -shared -o libmultiplier.so multiplier.o
RUN cp libmultiplier.so /usr/lib
RUN chmod 0755 /usr/lib/libmultiplier.so

WORKDIR /
COPY catkin_ws/src catkin_ws/src
WORKDIR /catkin_ws
# Set the working directory


RUN /bin/bash -c '. /opt/ros/noetic/setup.bash;catkin_make'
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Set the command to be executed when the container starts
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]