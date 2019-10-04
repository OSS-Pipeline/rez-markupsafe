name = "markupsafe"

version = "1.1.1"

authors = [
    "Armin Ronacher"
]

description = \
    """
    Safely add untrusted strings to HTML/XML markup.
    """

requires = [
    "cmake-3+",
    "python-2.7+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "markupsafe-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
