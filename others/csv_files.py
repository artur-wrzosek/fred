import csv

def create_csv(file: str, n_rows: int):
    headers = "user,amount,year,month\n"
    with open(file, mode="w") as f:
        f.write(headers)
        for i in range(n_rows):
            line = f"User{i},{i*100},2025,{i%12+1}\n"
            f.write(line)

def write_csv(file: str, n_rows: int):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        for i in range(n_rows):
            line = [f"Dummy{i}", 2000+i%25, i*11, i%12+1]
            writer.writerow(line)

def read_file(file: str):
    with open(file, "r") as f:
        for row in f.readlines():
            print(row, end="")

def read_csv(file:str):
    with open(file) as f:
        reader = csv.reader(f, delimiter=",", quotechar='"') # or dialect="excel"
        for row in reader:
            print(row)

def main():
    file_name_1 = "dummy1.csv"
    file_name_2 = "dummy2.csv"
    create_csv(file_name_1, 10)
    read_file(file_name_1)
    write_csv(file_name_2, n_rows=20)
    read_csv(file_name_2)

if __name__ == "__main__":
    main()