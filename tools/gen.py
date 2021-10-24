import json
import random


output = {
    "pallet_mode": 1,
    "containers": [
	{
        "ID": "d2b0ee39-4b4a-4836-a8c5-c17bc41d9479",
        "TypeName": "20",
        "X": 580,
        "Y": 225,
        "Z": 227,
        "Weight_limmit": 10000,
        "Numbers": 1
    },
    {
        "ID": "c79e2268-5f2a-4a65-a916c-674541ff7dd3",
        "TypeName": "40",
        "X": 1180,
        "Y": 225,
        "Z": 227,
        "Weight_limmit": 10000,
        "Numbers": 1
    }],
    "boxes": [],
    "pallets": [
	{
        "ID": "f5108a0d-2694-4a52-9289-11f976009959",
        "TypeName": "122X102",
        "X": 122,
        "Y": 12,
        "Z": 102,
        "Weight": 22,
        "Numbers": 0
    },
    {
        "ID": "85f94d82-1c2a-4a5d-b9cf-eee8f0349bee",
        "TypeName": "138X89",
        "X": 138,
        "Z": 89,
        "Y": 12,
        "Weight": 18,
        "Numbers": 0
    },
    {
        "ID": "86f94d82-1c2a-4a5d-b9cf-eee8f0349bee",
        "TypeName": "122x90",
        "X": 122,
        "Y": 12,
        "Z": 90,
        "Weight": 20,
        "Numbers": 0
    },
    {
        "ID": "89f94d82-1c2a-4a5d-b9cf-eee8f0349bee",
        "TypeName": "110x75",
        "X": 110,
        "Y": 12,
        "Z": 75,
        "Weight": 12,
        "Numbers": 0
    },
    {
        "ID": "8700b6fb-3472-4aa3-85d5-111868669ee8",
        "TypeName": "140X102",
        "X": 140,
        "Z": 102,
        "Y": 12,
        "Weight": 25,
        "Numbers": 0
    }
	]
}

n = int(input())
c0 = random.randint(0, n);
c1 = n - c0
p_area = c0 * 580 * 227 + c1 * 1180 * 227
volumn = p_area * (225 - 12)
output["containers"][0]["Numbers"] = c0
output["containers"][1]["Numbers"] = c1


while True:
	ty = random.randint(0, 4)
	ar = output["pallets"][ty]["X"] * output["pallets"][ty]["Y"]
	if p_area < ar: break
	p_area -= ar
	output["pallets"][ty]["Numbers"] += 1

cnt = 0
while True:
	limit = random.randint(1, random.randint(1, 140))
	x = random.randint(1, limit)
	y = random.randint(1, limit)
	z = random.randint(1, limit)
	if volumn < x * y * x: break;
	volumn -= x * y * z
	output["boxes"].append(    {
        "ID": "86daecba-d099-4c4b-9602-ef166a120a" + str(cnt),
        "TypeName": str(cnt),
        "X": x,
        "Y": y,
        "Z": z,
        "Weight": random.randint(1, x * y * z),
        "Numbers":1 
    });

with open('data.json', 'w') as f:
    json.dump(output, f)





