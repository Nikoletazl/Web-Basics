import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="pet_hotel",
    user="postgres",
    password="postgres123")

cursor = connection.cursor()
cursor.execute("""
SELECT CONCAT(p.owner_name),
       CONCAT('(', c.cat_name, ')')
FROM pet.pet_owner p
JOIN pet.cat c 
    ON p.owner_id = c.cat_id
""")


class Owner:
    def __init__(self, name, pet_name):
        self.name = name
        self.pet_name = pet_name

    def __repr__(self):
        return f'{self.name} {self.pet_name}'


owner = [Owner(*row) for row in cursor.fetchall()]

print(owner)
connection.close()
