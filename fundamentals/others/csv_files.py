import csv

def create_csv(file: str, n_rows: int):
    headers = "user,amount,year,month\n"
    with open(file, mode="w") as f:
        f.write(headers)
        for i in range(n_rows):
            line = f"User{i},{i*100},2025,{i%12+1}\n"
            f.write(line)

def read_file(file: str):
    with open(file, "r") as f:
        for row in f.readlines():
            print(row, end="")

def main():
    file_name = "dummy.csv"
    create_csv(file_name, 100)
    read_file(file_name)

if __name__ == "__main__":
    main()