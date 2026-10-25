# Clients of system services, one library per directory, linking only
# the toolkit's base library. They form the CutefishClients package; a
# consumer asks for them by directory name:
#   find_package(CutefishClients REQUIRED COMPONENTS appearance)
#   target_link_libraries(app PRIVATE Lingmo::AppearanceClient)

find_package(LingmoToolkit REQUIRED)

set(CUTEFISH_FRAMEWORK_CLIENTS "all" CACHE STRING
    "The clients/ directories to build: all, or a list of their names")

# lingmo_add_client(<name> TARGET <Target> SOURCES ... HEADERS ... [LIBRARIES ...])
# builds liblingmo-<name>-client as Lingmo::<Target>, its headers included
# as <lingmo/<name>/...>.
function(lingmo_add_client name)
    cmake_parse_arguments(arg "" "TARGET" "SOURCES;HEADERS;LIBRARIES" ${ARGN})
    lingmo_framework_add_library(lingmo-${name}-client
        TARGET ${arg_TARGET}
        MODULE ${name}
        EXPORT CutefishClient${name}Targets
        SOURCES ${arg_SOURCES}
        HEADERS ${arg_HEADERS}
        PUBLIC_LIBRARIES Lingmo::ToolkitBase ${arg_LIBRARIES}
    )
    lingmo_framework_export(CutefishClients CutefishClient${name}Targets)
endfunction()

file(GLOB client_directories LIST_DIRECTORIES true ${CMAKE_CURRENT_SOURCE_DIR}/*)
foreach(directory ${client_directories})
    get_filename_component(name ${directory} NAME)
    if(NOT EXISTS ${directory}/CMakeLists.txt)
        continue()
    endif()
    if(CUTEFISH_FRAMEWORK_CLIENTS STREQUAL "all" OR name IN_LIST CUTEFISH_FRAMEWORK_CLIENTS)
        add_subdirectory(${name})
    endif()
endforeach()

lingmo_framework_add_package(CutefishClients)
