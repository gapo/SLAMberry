#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "pangolin" for configuration "Release"
set_property(TARGET pangolin APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(pangolin PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "/usr/lib64/libGLU.so;/usr/lib64/libGL.so;/usr/lib64/libGLEW.so;-lX11;/usr/lib64/libpython3.5m.so;/usr/lib64/libdc1394.so;/usr/lib64/libavcodec.so;/usr/lib64/libavformat.so;/usr/lib64/libavutil.so;/usr/lib64/libswscale.so;/usr/lib64/libpng.so;/usr/lib64/libz.so;/usr/lib64/libjpeg.so;/usr/lib64/libtiff.so;/usr/lib64/libIlmImf.so"
  IMPORTED_LOCATION_RELEASE "/usr/local/lib/libpangolin.so"
  IMPORTED_SONAME_RELEASE "libpangolin.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS pangolin )
list(APPEND _IMPORT_CHECK_FILES_FOR_pangolin "/usr/local/lib/libpangolin.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
