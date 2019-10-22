name = "partio"

version = "1.10.1"

authors = [
    "Walt Disney Animation Studios"
]

description = \
    """
    C++ (with python bindings) library for easily reading/writing/manipulating common animation particle formats such
    as PDB, BGEO, PTC.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "python-2.7+<3",
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "partattr",
    "partconvert",
    "partedit",
    "partinfo",
    "partinspect",
    "partjson",
    "partview"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "partio-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PYTHONPATH.prepend("{root}/lib64/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")

    # Helper environment variables.
    env.PARTIO_BINARY_PATH.set("{root}/bin")
    env.PARTIO_INCLUDE_PATH.set("{root}/include")
    env.PARTIO_LIBRARY_PATH.set("{root}/lib64")
