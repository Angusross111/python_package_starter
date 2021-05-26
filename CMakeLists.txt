cmake_minimum_required(VERSION 3.0.2)
project(python_package_starter)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
)

catkin_python_setup()

include_directories(
    ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
    scripts/example_script
    nodes/example_node
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)