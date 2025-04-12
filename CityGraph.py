# CityGraph.py

graph = {
    1: {
        "id": 1,
        "x": -1200, "y": 750,
        "neighbors": { "right": 2,}
    },
    2: {
        "id": 2,
        "x": 600, "y": 750,
        "neighbors": { "right": 3}
    },
    3: {
        "id": 3,
        "x": 1200, "y": 750,
        "neighbors": { "down": 8 }
    },
    4: {
        "id": 4,
        "x": -1200, "y": 250,
        "neighbors": { "up": 1}
    },
    5: {
        "id": 5,
        "x": -800, "y": 250,
        "neighbors": { "left": 4, "down": 10 }
    },
    6: {
        "id": 6,
        "x": 600, "y": 250,
        "neighbors": { "up": 2, "left": 5 }
    },
    7: {
        "id": 7,
        "x": 800, "y": 250,
        "neighbors": { "left": 6}
    },
    8: {
        "id": 8,
        "x": 1200, "y": 250,
        "neighbors": { "left": 7,"down":14}
    },
    9: {
        "id": 9,
        "x": -1200, "y": -250,
        "neighbors": { "up": 4, "right": 10 }
    },
    10: {
        "id": 10,
        "x": -800, "y": -250,
        "neighbors": { "right": 11}
    },
    11: {
        "id": 11,
        "x": -600, "y": -250,
        "neighbors": { "down": 16, "right": 12}
    },
    12: {
        "id": 12,
        "x": 400, "y": -250,
        "neighbors": { "right": 13}
    },
    13: {
        "id": 13,
        "x": 800, "y": -250,
        "neighbors": { "up": 7, "right": 14}
    },
    14: {
        "id": 14,
        "x": 1200, "y": -250,
        "neighbors": { "down": 18}
    },
    15: {
        "id": 15,
        "x": -1200, "y": -750,
        "neighbors": { "up": 9}
    },
    16: {
        "id": 16,
        "x": -600, "y": -750,
        "neighbors": { "left": 15}
    },
    17: {
        "id": 17,
        "x": 400, "y": -750,
        "neighbors": { "up": 12, "left": 16}
    },
    18: {
        "id": 18,
        "x": 1200, "y": -750,
        "neighbors": { "left": 17}
    }
}