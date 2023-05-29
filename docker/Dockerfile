FROM ros:noetic

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
# VOLUME <directorio_o_nombre_de_tu_volumen>:/home/robotics/data
RUN mkdir /catkin_ws
COPY catkin_ws/ catkin_ws/
# Set the working directory
WORKDIR /catkin_ws

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash;catkin_make'
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Set the command to be executed when the container starts
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]