To create the library we need to compile with '-fPIC' (position-independent code) flag

```bash
g++ -c -fPIC multiplier.cpp -o multiplier.o
```

Then we create the shared library with the object file

```bash
g++ -shared -o libmultiplier.so multiplier.o
```

then we can use the library in our main program

```bash
g++ main.cpp -L. -lmultiplier -o main
```

To add it so i can use it in my system and give rights to use it
    
```bash
    cp libmultiplier.so /usr/lib
    chmod 0755 /usr/lib/libmultiplier.so
```
In order to use the library with ROS you need to add it to the CMakeLists.txt file

```bash
    add_library(multiplier SHARED src/multiplier.cpp)
    target_include_directories(multiplier PUBLIC include)
    target_link_libraries(multiplier ${catkin_LIBRARIES})
```
```bash
target_link_libraries(hundred_pub_node
  ${catkin_LIBRARIES}
  multiplier
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ../../library
)

```