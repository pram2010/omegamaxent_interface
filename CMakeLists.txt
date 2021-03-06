# Start configuration
cmake_minimum_required(VERSION 2.8.12)
project(omegamaxent_interface CXX)
if(POLICY CMP0074)
  cmake_policy(SET CMP0074 NEW)
endif()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

# Default to Release build type
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Type of build" FORCE)
endif()
message( STATUS "-------- BUILD-TYPE: ${CMAKE_BUILD_TYPE} --------")

# Load Dependencies
find_package(TRIQS 2.1 REQUIRED)
find_package(Cpp2Py 1.5 REQUIRED)

# Default Install directory to TRIQS_ROOT if not given or invalid.
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT OR (NOT IS_ABSOLUTE ${CMAKE_INSTALL_PREFIX}))
  message(STATUS "No install prefix given (or invalid). Defaulting to TRIQS_ROOT")
  set(CMAKE_INSTALL_PREFIX ${TRIQS_ROOT} CACHE PATH "default install path" FORCE)
endif()
message(STATUS "-------- INSTALL_PREFIX: ${CMAKE_INSTALL_PREFIX} --------")

# Define the omegamaxent_interface version numbers and get the git hash
set(OMEGAMAXENT_INTERFACE_VERSION_MAJOR 2)
set(OMEGAMAXENT_INTERFACE_VERSION_MINOR 2)
set(OMEGAMAXENT_INTERFACE_VERSION_PATCH 0)
set(OMEGAMAXENT_INTERFACE_VERSION ${OMEGAMAXENT_INTERFACE_VERSION_MAJOR}.${OMEGAMAXENT_INTERFACE_VERSION_MINOR}.${OMEGAMAXENT_INTERFACE_VERSION_PATCH})
triqs_get_git_hash_of_source_dir(OMEGAMAXENT_INTERFACE_GIT_HASH)
message(STATUS "app4triqs version : ${OMEGAMAXENT_INTERFACE_VERSION}")
message(STATUS "Git hash: ${OMEGAMAXENT_INTERFACE_GIT_HASH}")

add_subdirectory(omegamaxent)
add_subdirectory(python)

# Tests
option(Build_Tests "Build tests" ON)
if(Build_Tests)
  enable_testing()
  add_subdirectory(test/python)
endif()

option(Build_Documentation "Build documentation" OFF)
if(Build_Documentation)
  find_package(MathJax REQUIRED)
  message(STATUS "Detected MathJax at ${MATHJAX_PATH}")
  if(NOT TRIQS_WITH_DOCUMENTATION)
    message(WARNING " TRIQS library has not been compiled with its documentation!\n Cannot build documentation!")
  else()
    message(STATUS "Documentation Build enabled")
    add_subdirectory(doc)
  endif()
endif()

option(BUILD_DEBIAN_PACKAGE "Build a deb package" OFF)
if(BUILD_DEBIAN_PACKAGE)
  if(NOT CMAKE_INSTALL_PREFIX STREQUAL "/usr")
    message(FATAL_ERROR "CMAKE_INSTALL_PREFIX must be /usr for packaging")
  endif()
  SET(CPACK_GENERATOR "DEB")
  SET(CPACK_PACKAGE_VERSION ${OMEGAMAXENT_INTERFACE_VERSION})
  SET(CPACK_PACKAGE_CONTACT "https://github.com/TRIQS/omegamaxent_interface")
  EXECUTE_PROCESS(COMMAND dpkg --print-architecture OUTPUT_VARIABLE CMAKE_DEBIAN_PACKAGE_ARCHITECTURE OUTPUT_STRIP_TRAILING_WHITESPACE)
  SET(CPACK_DEBIAN_PACKAGE_DEPENDS "triqs (>= 2.2)")
  SET(CPACK_DEBIAN_PACKAGE_SHLIBDEPS ON)
  SET(CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS ON)
  INCLUDE(CPack)
endif()
