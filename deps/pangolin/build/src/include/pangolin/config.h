#ifndef PANGOLIN_CONFIG_H
#define PANGOLIN_CONFIG_H

/*
 * Configuration Header for Pangolin
 */

/// Version
#define PANGOLIN_VERSION_MAJOR 0
#define PANGOLIN_VERSION_MINOR 3
#define PANGOLIN_VERSION_STRING "0.3"

/// Pangolin options
#define BUILD_PANGOLIN_GUI
#define BUILD_PANGOLIN_VARS
#define BUILD_PANGOLIN_VIDEO

/// Configured libraries
/* #undef HAVE_CUDA */
#define HAVE_PYTHON

#define CPP11_NO_BOOST
/* #undef HAVE_EIGEN */
/* #undef HAVE_TOON */

#define HAVE_DC1394
#define HAVE_V4L
/* #undef HAVE_OPENNI */
/* #undef HAVE_OPENNI2 */
/* #undef HAVE_UVC */
/* #undef HAVE_DEPTHSENSE */
/* #undef HAVE_TELICAM */
/* #undef HAVE_PLEORA */

#define HAVE_FFMPEG
/* #undef HAVE_FFMPEG_MAX_ANALYZE_DURATION2 */
#define HAVE_FFMPEG_AVFORMAT_ALLOC_OUTPUT_CONTEXT2

#define HAVE_GLEW
/* #undef GLEW_STATIC */

/* #undef HAVE_GLUT */
/* #undef HAVE_FREEGLUT */
/* #undef HAVE_APPLE_OPENGL_FRAMEWORK */
/* #undef HAVE_MODIFIED_OSXGLUT */
/* #undef HAVE_GLES */
/* #undef HAVE_GLES_2 */
/* #undef HAVE_OCULUS */

#define HAVE_PNG
#define HAVE_JPEG
#define HAVE_TIFF
#define HAVE_OPENEXR

/// Platform
#define _UNIX_
/* #undef _WIN_ */
/* #undef _OSX_ */
#define _LINUX_
/* #undef _ANDROID_ */
/* #undef _IOS_ */

/// Compiler
#define _GCC_
/* #undef _CLANG_ */
/* #undef _MSVC_ */

/// Defines generated when calling into Pangolin API. Not to be
/// used in compiled library code, only inlined header code.
#if (__cplusplus > 199711L) || (_MSC_VER >= 1700)
#define CALLEE_HAS_CPP11
#define CALLEE_HAS_RVALREF
#endif

#if (__cplusplus > 199711L) || (_MSC_VER >= 1800)
#define CALLEE_HAS_VARIADIC_TEMPLATES
#endif

#endif //PANGOLIN_CONFIG_H
