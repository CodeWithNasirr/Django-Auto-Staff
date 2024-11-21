from faker import Faker
import random
import os
import csv
fake = Faker('en_IN')

def xyzx(record=1000,file_path="OutPut.csv") -> None:
    if not os.path.exists(file_path):
        with open(file_path,mode='w',newline="",encoding='utf-8')as file:
            write=csv.writer(file)
            write.writerow(["First Name", "Age", "Roll"])
    with open(file_path,mode='a',newline="",encoding='utf-8')as f:
        write=csv.writer(f)
        for i in range(record):
            first_name = fake.first_name()
            age = random.randint(18, 60)
            roll = random.randint(1, 100)
            # print(f"First Name: {first_name}, Age: {age}, Roll: {roll}")
            write.writerow([first_name,age,roll])
    print(f"Successfully saved {record} records to {file_path}!")


xyzx(1000)
