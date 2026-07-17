import json
import numpy as np


def save_data():
    numbers = np.array([3.14, 1.5, 9.99, 5.25, 2.71])

    number_list = numbers.tolist()

    data = {
        "numbers": number_list
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


def read_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    numbers = np.array(data["numbers"])
    integers = numbers.astype(int)

    print("\nData from JSON:")
    print("Float Array :", numbers)
    print("Integer Array:", integers)


save_data()
read_data()