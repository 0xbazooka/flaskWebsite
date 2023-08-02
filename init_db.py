import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Add some sample users
cur.execute("INSERT INTO users (user_name, password, email, balance) VALUES ('user1', 'password1', 'user1@example.com', 100)")
cur.execute("INSERT INTO users (user_name, password, email, balance) VALUES ('user2', 'password2', 'user2@example.com', 200)")

connection.commit()

# Add some sample products for each user
cur.execute("INSERT INTO products (user_id, stock, price, title) VALUES (1, 10, 50, 'Product 1')")
cur.execute("INSERT INTO products (user_id, stock, price, title) VALUES (1, 5, 75, 'Product 2')")
cur.execute("INSERT INTO products (user_id, stock, price, title) VALUES (2, 3, 100, 'Product 3')")

connection.commit()

# Add some sample comments for each product
cur.execute("INSERT INTO comments (product_id, user_name, content) VALUES (1, 'user1', 'This product is awesome!')")
cur.execute("INSERT INTO comments (product_id, user_name, content) VALUES (1, 'user2', 'I agree, this product is great!')")
cur.execute("INSERT INTO comments (product_id, user_name, content) VALUES (2, 'user2', 'I just bought this product and it works great!')")
cur.execute("INSERT INTO comments (product_id, user_name, content) VALUES (3, 'user1', 'I think this product could be better')")

connection.commit()

connection.close()