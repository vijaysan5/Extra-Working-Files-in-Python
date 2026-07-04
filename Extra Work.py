import pandas as pan
import sqlite3 as sq

smark = pan.read_csv("San's  DataScience Folder/SQL Program in DataScience/supermarket_sales - Sheet1.csv")


for column in smark.columns:
    print(column)
# Branch,City,Customer type,Gender,Product

con = sq.connect("Supermarket.db")
csr = con.cursor()

# Create Table :
csr.execute("""
    CREATE TABLE IF NOT EXISTS smart (
        Branch TEXT PRIMARY KEY,
        City TEXT,
        Customer TEXT,
        Gender TEXT,
        Product TEXT
    )
""")
con.commit()

# Update :
def Detailz(Branch, City, Customer, Gender, Product):
    csr.execute("""
        INSERT INTO smart (Branch, City, Customer, Gender, Product)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(Branch) DO UPDATE SET
            City = excluded.City,
            Customer = excluded.Customer,
            Gender = excluded.Gender,
            Product = excluded.Product
    """, (Branch, City, Customer, Gender, Product))
    con.commit()
    print(f"Detailz : '{Branch}'s Data is Updated...")

def read_Detz(Branch):
    csr.execute("SELECT * FROM smart WHERE Branch = ?", (Branch,))
    detail = csr.fetchone()

    if detail :
        print(f"Branch : {detail[0]}\n~First Name: {detail[1]}\n~Last Name: {detail[2]}\n~Age: {detail[3]}\n~Email ID: {detail[4]}\n")
        return detail
    else:
        print(f"Branch : '{Branch}' is Not Found.")
        return None
def main():
    Detailz(smark["Branch"], smark["City"], smark["Customer"], smark["Gender"], smark["Product"])
    read_Detz(smark["Branch"])

if __name__ == "__main__":
    main()
    con.close()

    for row in smark.itertuples(index=False):
    csr.execute("""
    INSERT INTO Supermarket VALUES
    (?, ?, ?, ?, ?)
    """, (tuple.row))
    con.commit()