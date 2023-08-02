# RouteMapper

RouteMapper is a Python project that allows you to plot and visualize routes on a map using geographic coordinates. It utilizes the `geopy`, `osmnx`, `folium`, and `networkx` libraries to process coordinates, calculate distances, and create interactive maps with markers and lines representing the routes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Visualizing the routes between them on a map is often useful when working with geographic coordinates or waypoints. RouteMapper makes this task easy by taking a list of coordinates as input and generating an interactive map displaying the route between each pair of consecutive coordinates.

The project utilizes the following Python libraries:

- [geopy](https://geopy.readthedocs.io/): For calculating geographical distances between coordinates.
- [osmnx](https://osmnx.readthedocs.io/): For retrieving OpenStreetMap data and network analysis.
- [folium](https://python-visualization.github.io/folium/): For creating interactive web maps.
- [networkx](https://networkx.github.io/): For graph-based network analysis.

## Features

- Plot routes between a list of geographic coordinates on an interactive map.
- Visualize the start and end points with customizable markers.
- Highlight the route with colored lines on the map.
- Save the map as an HTML file for sharing or embedding in other web applications.

## Installation

To use RouteMapper, you need to have Python installed on your system. The project requires the following libraries, which can be installed using `pip`:

```bash
pip install geopy
pip install osmnx
pip install folium
pip install networkx
pip install tqdm

```
## Contributing

Contributions to RouteMapper are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request. For major changes, it's best to discuss your ideas in an issue before implementing them.

## License

OSMnx is open-source software licensed under the MIT License.
