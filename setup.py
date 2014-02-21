from setuptools import setup
from setuptools.command.test import test as TestCommand
from awscostmon import __version__


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name='serverdoctor',
    packages=['serverdoctor'],
    version=__version__,
    description='aws cost estimate api',
    author='Kenichi Sasaki',
    author_email='sasaki-k@klab.com',
    install_requires=[
        'argparse',
        'python-dateutil',
        'PyYAML',
        'enum34',
    ],
    scripts=[
        'scripts/srvdr',
        'scripts/srvdr-init',
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest }
)
