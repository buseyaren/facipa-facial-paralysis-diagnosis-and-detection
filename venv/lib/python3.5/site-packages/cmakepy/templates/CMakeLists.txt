cmake_minimum_required (VERSION 2.8)
project ({{project}})


SET(EXECUTABLE_OUTPUT_PATH ../Binaries)
SET(PROJECT_FOLDER ../{{project}})

add_executable({{project}} src/main.cpp)