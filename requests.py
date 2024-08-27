import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('HW.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = "SELECT * FROM users WHERE id = 9"
print(execute_query(sql))

sql = "SELECT * FROM tasks WHERE status_id=2"
print(execute_query(sql))
sql = "SELECT * FROM tasks INNER JOIN status on tasks.status_id=status.id WHERE status.name='new'"
print(execute_query(sql))

sql = "UPDATE tasks SET status_id=1 WHERE id=4"
print(execute_query(sql))

sql = "SELECT * FROM users where id NOT IN (SELECT tasks.user_id FROM tasks)"
print(execute_query(sql))

sql = "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task for user','Do some work',1,15)"
print(execute_query(sql))

sql = "SELECT * FROM tasks WHERE status_id <> 3"
print(execute_query(sql))

sql = "DELETE FROM tasks WHERE id=5"
print(execute_query(sql))

sql = "SELECT * FROM users WHERE email LIKE 'example@test.com'"
print(execute_query(sql))

sql = "UPDATE users set fullname = 'Anna Kit' WHERE id=7"
print(execute_query(sql))

sql = """SELECT name as Status,COUNT(t.id) as Number_of_tasks from status s
    LEFT join tasks t on s.id = t.status_id  GROUP  by t.status_id,s.id ORDER by s.id"""
print(execute_query(sql))

sql = "SELECT t.* FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%example.org'"
print(execute_query(sql))

sql = "SELECT * FROM tasks WHERE description IS NULL"
print(execute_query(sql))

sql = "SELECT * FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = 2 ORDER BY u.id"
print(execute_query(sql))

sql = "SELECT u.*,COUNT(t.id) AS Number_of_tasks FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY t.user_id"
print(execute_query(sql))