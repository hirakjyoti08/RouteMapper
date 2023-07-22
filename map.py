from geopy.distance import geodesic
import osmnx as ox
import folium
import networkx as nx
from tqdm import tqdm

coordinates = []
with open("D:\VS code\Python\modified220.txt", 'r') as file:
    for line in file:
        if 'POINT' in line:
            parts = line.split()
            latitude = float(parts[1].split('(')[1])
            longitude = float(parts[2].split(')')[0])
            coordinates.append((latitude, longitude))

m = folium.Map(location=coordinates[0], zoom_start=14)

start_marker = folium.Marker(
    location=coordinates[0], popup="Start Point", icon=folium.Icon(color="green"))
start_marker.add_to(m)

end_marker = folium.Marker(
    location=coordinates[-1], popup="End Point", icon=folium.Icon(color="red"))
end_marker.add_to(m)

highlight_group = folium.FeatureGroup()
interval_distance = 1000 
accumulated_distance = 0

for i in tqdm(range(len(coordinates) - 1), desc="Processing"):
    try:
        graph = ox.graph_from_point(
            coordinates[i], dist=1000, network_type='all', simplify=False)
        node1 = ox.distance.nearest_nodes(
            graph, coordinates[i][1], coordinates[i][0])
        node2 = ox.distance.nearest_nodes(
            graph, coordinates[i + 1][1], coordinates[i + 1][0])

        if node1 is None or node2 is None:
            continue

        path = nx.shortest_path(graph, node1, node2, weight='travel_time')
        path_coordinates = []

        prev_coord = None
        for node in path:
            node_coordinates = (graph.nodes[node]['y'], graph.nodes[node]['x'])
            path_coordinates.append(node_coordinates)
            node_distance = graph.nodes[node].get('travel_time', 0)

            if prev_coord is not None:
                distance = geodesic(prev_coord, node_coordinates).meters
                accumulated_distance += distance

                if accumulated_distance >= interval_distance:
                    marker = folium.Marker(location=node_coordinates, icon=folium.Icon(
                        color='blue'), popup=str(node_coordinates))
                    marker.add_to(highlight_group)
                    accumulated_distance = 0
                    
                    with open('coordinates2.txt', 'a') as file:
                        file.write(str(node_coordinates) + '\n')

            prev_coord = node_coordinates

        highlight_line = folium.PolyLine(
            locations=path_coordinates, color='red', weight=5)
        highlight_line.add_to(highlight_group)

    except nx.NetworkXNoPath:
        print(
            f"No path between {node1} and {node2}. Skipping this pair of coordinates.")

highlight_group.add_to(m)

m.save('map.html')
