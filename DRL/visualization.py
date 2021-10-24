"""
Transpose 2d-array to json for visulization

Input:
box_list.npy: AI model input data
obs_list.npy: AI model output data

Output:
container_output.json: write for https://github.com/skjolber/3d-bin-container-packing/tree/master/visualization/viewer
"""

import numpy as np
import json
import copy

N = 10


class Placement:
    def __init__(self, step) -> None:
        self.step = step
        self.x = None
        self.y = None
        self.z = None
        self.dx = None
        self.dy = None
        self.dz = None


def transform() -> Placement:
    placements = []
    containers = np.load("obs_list.npy")
    containers = np.insert(containers, 0, np.zeros((10, 10)), 0)

    for each_layer in range(len(containers)-3):
        layer = containers[each_layer+1] - containers[each_layer]
        placement = Placement(each_layer + 1)
        for i in range(N-1, -1, -1):
            for j in range(0, N):
                if layer[i][j] != 0:
                    placement.x = i
                    placement.y = j
                    placement.z = containers[each_layer][i][j]
                    break
        placements.append(placement)

    boxs = np.load("box_list.npy")[:-1]
    for i, placement in enumerate(placements):
        box_xyz = boxs[i]
        placement.dx = box_xyz[0]
        placement.dy = box_xyz[1]
        placement.dz = box_xyz[2]

    return placements


def save_to_json(placements) -> None:
    sample_place = {
        "step": 2,
        "id": 0,
        "name": 0,
        "plugins": [],
        "x": 0,
        "y": 0,
        "z": 0,
        "stackable": {
            "step": 2,
            "id": "4",
            "name": "4",
            "plugins": [],
            "dx": 4,
            "dy": 3,
            "dz": 1,
            "type": "box"
        }
    }

    with open('container_sample.json', 'r') as f:
        data = json.load(f)
        data_place = data["containers"][0]["stack"]["placements"]
        for i, placement in enumerate(placements):
            this_place = copy.deepcopy(sample_place)
            this_place["step"] = int(placement.step + 1)
            this_place["x"] = int(placement.x)
            this_place["y"] = int(placement.y)
            this_place["z"] = int(placement.z)
            this_place["stackable"]["dx"] = int(placement.dx)
            this_place["stackable"]["dy"] = int(placement.dy)
            this_place["stackable"]["dz"] = int(placement.dz)
            this_place["stackable"]["step"] = int(placement.step + 1)
            this_place["stackable"]["id"] = str(int(placement.step + 1))
            this_place["stackable"]["name"] = str(int(placement.step + 1))
            data_place.append(this_place)

    with open('container_output.json', 'w') as f:
        json.dump(data, f)


placements = transform()
save_to_json(placements)
