name = "partio"

version = "1.12.0"

authors = [
    "Walt Disney Animation Studios"
]

description = \
    """
    C++ (with python bindings) library for easily reading/writing/manipulating common animation particle formats such
    as PDB, BGEO, PTC.
    """

requires = [
    "cmake",
    "gcc-6",
    "python",
    "zlib"
]

variants = [
    ["platform-linux","arch-x86_64"]
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
    env.PYTHONPATH.prepend("{root}/lib64/python3.9/site-packages")

    # Helper environment variables.
    env.PARTIO_BINARY_PATH.set("{root}/bin")
    env.PARTIO_INCLUDE_PATH.set("{root}/include")
    env.PARTIO_LIBRARY_PATH.set("{root}/lib64")
