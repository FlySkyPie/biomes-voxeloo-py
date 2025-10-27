cmake_minimum_required (VERSION 3.15...4.0)

project(
    VoxelooPy
    VERSION 0.1.0
    LANGUAGES CXX)

set(CEREAL_BUILD_DOC OFF)
set(EIGEN_BUILD_DOC OFF)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++20")
set(VOXELOO_BUILD_TEST OFF)

include(cmake/CPM.cmake)

CPMAddPackage("gl:libeigen/eigen#3.4.0")
CPMAddPackage("gh:jupp0r/prometheus-cpp@1.0.1")
CPMAddPackage("gh:pybind/pybind11@2.9.2")
CPMAddPackage("gh:USCiLab/cereal@1.3.2")
CPMAddPackage("gh:martinus/robin-hood-hashing#3.11.5")
CPMAddPackage("gh:FlySkyPie/biomes-voxeloo-geometry@0.1.1")
CPMAddPackage("gh:FlySkyPie/biomes-voxeloo-light-kernelry@0.1.3")
CPMAddPackage(
    NAME OpenSimplexNoise
    GITHUB_REPOSITORY "FlySkyPie/OpenSimplexNoise"
    GIT_TAG v1.0.3
    OPTIONS 
        "OSN_BUILD_STATIC ON"
        "OSN_BUILD_SHARED OFF"
)
CPMAddPackage("gh:FlySkyPie/tomasakeninemoeller@1.0.0")
CPMAddPackage("gh:FlySkyPie/biomes-voxeloo#develop")

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 REQUIRED)

python_add_library(
    voxeloo MODULE 
    src/biomes.cpp
    src/blocks.cpp
    src/culling.cpp
    src/ext.cpp
    src/galois.cpp
    src/geometry.cpp
    src/meshes.cpp
    src/noise.cpp
    src/primitives.cpp
    src/rasterization.cpp
    src/rays.cpp
    src/runs.cpp
    src/shards.cpp
    src/spatial.cpp
    src/tensors.cpp
    src/voronoi.cpp
    src/voxels.cpp
    WITH_SOABI)

target_link_libraries(
    voxeloo
    PRIVATE
    VoxelooGeometry
    VoxelooLightKernelry
    Voxeloo
    OpenSimplexNoise
    robin_hood::robin_hood
    pybind11::pybind11
    Eigen3::Eigen
    cereal::cereal
    tomasakeninemoeller)

target_include_directories(
    voxeloo
    PUBLIC 
    ${PROJECT_SOURCE_DIR}/include
)

# This is passing in the version as a define just as an example
target_compile_definitions(voxeloo PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS voxeloo DESTINATION VoxelooPy)