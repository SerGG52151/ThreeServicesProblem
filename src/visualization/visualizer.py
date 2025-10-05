import matplotlib.pyplot as plt
from src.geometry.point import Point
from src.geometry.segment import Segment
from src.geometry.torus import Torus

def visualize_solution(torus: Torus, houses, services, paths):
    fig, ax = plt.subplots()
    ax.set_xlim(0, torus.width)
    ax.set_ylim(0, torus.height)
    ax.set_aspect('equal')
    ax.set_xticks(range(torus.width + 1))
    ax.set_yticks(range(torus.height + 1))
    ax.grid(True)

    house_x = [p.x for p in houses]
    house_y = [p.y for p in houses]
    ax.plot(house_x, house_y, 'ro', markersize=10, label='Houses')

    service_x = [p.x for p in services]
    service_y = [p.y for p in services]
    ax.plot(service_x, service_y, 'bs', markersize=10, label='Services')

    if paths:
        colors = ['#FF0000', '#00FF00', '#0000FF']  # Red, Green, Blue for the 3 houses
        num_services = len(services)
        for i, path in enumerate(paths):
            house_index = i // num_services
            color = colors[house_index % len(colors)]
            for segment in path:
                p1 = segment.p1
                p2 = segment.p2
                
                # 
                for i_trans in range(-1, 2):
                    for j_trans in range(-1, 2):
                        dx = i_trans * torus.width
                        dy = j_trans * torus.height
                        ax.plot([p1.x + dx, p2.x + dx], [p1.y + dy, p2.y + dy], color=color)

    ax.legend()
    plt.title("K3,3 on a Torus")
    plt.show()
