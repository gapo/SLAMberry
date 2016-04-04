# Compute paths
get_filename_component( PROJECT_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH )
SET( Pangolin_INCLUDE_DIRS "/home/gapo/meng/deps/pangolin/include;/home/gapo/meng/deps/pangolin/build/src/include;/usr/include;/usr/include" )
SET( Pangolin_INCLUDE_DIR  "/home/gapo/meng/deps/pangolin/include;/home/gapo/meng/deps/pangolin/build/src/include;/usr/include;/usr/include" )

# Library dependencies (contains definitions for IMPORTED targets)
if( NOT TARGET pangolin AND NOT Pangolin_BINARY_DIR )
  include( "${PROJECT_CMAKE_DIR}/PangolinTargets.cmake" )
  
endif()

SET( Pangolin_LIBRARIES    pangolin )
SET( Pangolin_LIBRARY      pangolin )
SET( Pangolin_CMAKEMODULES /home/gapo/meng/deps/pangolin/src/../CMakeModules )
