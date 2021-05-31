from distutils.core import setup

setup(
    name='rosactive',
    version='1.0.0',
    license='GPLv3',
    description='CLI util to manage multiple simultaneous ROS1/ROS2 installations and workspaces',
    author='cst0',
    author_email='chris@cthierauf.com',
    url='https://github.com/cst0/rosactive.git',
    download_url='https://github.com/cst0/rosactive.git',
    keywords=['ros', 'cli'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPLv3',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
