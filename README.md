# `rosactive`: manage multiple simultaneous ROS1/ROS2 installations and workspaces

I have a bunch of ROS projects I'm developing side-by-side, and so I end up
having a bunch of ROS workspaces, too. At some point, though, you don't want to
have all of these workspaces active at the same time, but you still want a way
to quickly develop in this systems.

This is where `rosactive` becomes useful. Rather than manually sourcing each
workspace with every new terminal, `rosactive` will track which workspaces you
have set as being activated and make sure that they have been `source`'d for
each new terminal window.

You can also manage multiple ROS distributions this way, too. While you'll only
have one ROS1 installation, you might have that alongside multiple ROS2
versions. Additionally, you can put together different 'projects' to bundle
different configurations together.

I've been using this tool for a while and it's become a part of my regular
workflow, so I'm making it public because of that. However, there's still more
I'd like to do before I would consider this stable enough for a full release.

## Installation

1) Remove any ROS-related `source`'ing you're doing in your `.bashrc`, `.config.fish`, etc.
2) Get this executable (see next section, you've got a few options)
3) run `rosactive` for the first time and the tool should automagically set
    itself up and find catkin workspaces
4) Use the tool.

### Getting from pip
`pip install rosactive`

### Getting from source (catkin)

```
cd ~/<catkin_ws>/src
git clone https://github.com/cst0/rosactive.git
cd ..
catkin_make install
```

### Getting from source (cmake)

```
git clone https://github.com/cst0/rosactive.git
cd rosactive
mkdir build
cd build
cmake ..
make .
sudo make install
```
