import json
import numpy as np


# ==========================================
# 1. POST METHOD (Data Save Karna)
# ==========================================
def post_data_way1():
    # NumPy se ek float array banayi jo unsorted hai
    float_array = np.array([3.14, 1.5, 9.99, 5.25, 2.71])

    # NumPy array ko normal Python list mein convert kiya
    python_list = float_array.tolist()

    # Dictionary banayi JSON mein save karne ke liye
    data_to_save = {"my_floats": python_list}

    # Data ko local json file mein save kar rahe hain
    with open("local_db_way1.json", "w") as file:
        json.dump(data_to_save, file, indent=4)

    print("POST: Unsorted float array JSON file mein save ho gayi hai!")


# ==========================================
# 2. GET METHOD (Data Read aur Convert Karna)
# ==========================================
def get_data_way1():
    # Local JSON file se data read kar rahe hain
    with open("local_db_way1.json", "r") as file:
        loaded_data = json.load(file)

    # JSON se list nikal kar wapas NumPy array banayi
    retrieved_list = loaded_data["my_floats"]
    float_array = np.array(retrieved_list)

    # Float array ko Integer array mein convert kiya (.astype(int) se)
    int_array = float_array.astype(int)

    # Terminal mein result print kar rahe hain
    print("\nGET Result:")
    print("Original loaded floats:", float_array)
    print("Converted Integers:    ", int_array)


# Dono functions ko bari bari chalate hain
post_data_way1()
get_data_way1()