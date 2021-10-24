import numpy as np
import json


output = {
    "status": 130,
    "total_container_types": 1,
    "total_pallet_types": 1,
    "total_box_types": 1,
    "containers": [
        {
            "ID": "73bd0306-ccef-4e58-b9f3-7b73b263dc87",
            "TypeName": "helloContainer_0",
            "TypeIndex": 0,
            "X": 20.0,
            "Y": 20.0,
            "Z": 20.0,
            "Weight_limmit": 20000.0,
            "Fitted_items": [
                {
                    "ID": "b2c12820-e92e-4eb7-a38d-143b417f6112",
                    "TypeName": "122X102_0",
                    "X": 10.0,
                    "Y": 2.0,
                    "Z": 10.0,
                    "Weight": 23.0,
                    "position_x": 0.0,
                    "position_y": 0.0,
                    "position_z": 0.0,
                    "RotationType": 0,
                    "TypeIndex": 1,
                    "Fitted_items": []
                }
            ],
            "UnFitted_items": []
        }
    ]
}
N = 10
arr = np.load("obs_list.npy")
pre = np.array([[0] * N] * N)
cnt = 0
for it in arr:
	layer = it - pre
	for i in range(0, N):
		flag = 0
		for j in range(0, N):
			if layer[i][j] != 0:
				data = layer[~np.all(layer == 0, axis=1)]
				mask = (data == 0).all(0)
				column_indices = np.where(mask)[0]
				data = data[:,~mask]
				box = { "position_x": i,
						"position_y": int(pre[i][j] + 1),
						"position_z": j,
						"X" : len(data),
						"Y" : int(layer[i][j]),
						"Z" : len(data[0]),
						"ID": "00d2edf9-2fc8-4c25-a063-b608504270f4" + str(i) + str(j),
						"TypeName": "test_0" + str(i) + str(j),
						"Weight": 1.0,
						"RotationType": 0,
						"TypeIndex": cnt,
				}
				output["containers"][0]["Fitted_items"][0]["Fitted_items"].append(box)
				flag = 1
				cnt += 1
				break
		if flag : break
	pre = it
output["total_box_types"] = cnt

with open('trans.json', 'w') as f:
    json.dump(output, f)
