from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pybuilder_playground"
default_task = "publish"


@init
def set_properties(project):
    # This setting works fine with pip 7.1.2. With pip 8.0.0 it
    # causes "pybuilder install_dependencies" to fail.
    project.set_property('install_dependencies_upgrade', True)


    # This package triggers the bug, others (e.g. mock) do not trigger it.
    project.build_depends_on("argparse")
