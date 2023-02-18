from classes.Employee import Employee
from classes.News import News
import sqlite3


def insert_data(emp):
    if allowed_id(emp.emp_id) is None:
        with conn:
            c.execute("INSERT INTO Employee VALUES(:emp_id,:name,:lname,:age,:salary,:position,:email)", {"emp_id": emp.emp_id, "name": emp.name, "lname": emp.lname, "age": emp.age,
                                                                                                                                "salary": emp.salary, "position": emp.position, "email": emp.email})
            conn.commit()
        return 1, f"New employee has been added successfully with Employee ID:<b style='color:#32CD32'> {emp.emp_id} </b>"
    else:
        return 0, "Employee ID already exists"


def allowed_id(emp_id, table="Employee"):
    c.execute(f"SELECT * FROM {table} WHERE emp_id=:emp_id",
              {"emp_id": emp_id})
    return c.fetchone()


def create_employee_object(emp_id, emp_name, emp_lname, emp_age, emp_salary, emp_pos, emp_email):
    e = Employee(emp_id, emp_name, emp_lname, emp_age,
                 emp_salary, emp_pos, emp_email)
    return e


def fake_data():

    # Populate Emplyee Table with Fake Data
    import random
    e = Employee(str(random.choice(range(100, 999)))+'An'+str(random.choice(range(100, 999)))+'Do' +
                 str(random.choice(range(10, 99))), 'Andy', 'Doe', 25, 10000, 'Manager', 'Andy.Doe.manager@gmail.com')
    insert_data(e)
    names = ["Andy", "Robert", "William", "Linda", "Christopher", "Betty", "Julie", "Frank", "Gary", "Paul",
             "Donald", "Jessica", "Andrew", "Megan", "Elizabeth", "Andres", "John", "Judy", "Mary", "Michael",
             "Sara", "Penny", "Andrew", "Mike", "Suzan", "Henry", "Shiva", "Evelyn", "Gloria", "Joe", "Billy", "Albert",
             "Rose", "Charlotte", "Bobby", "Johnny", "Eugene", "Diana"]
    lnames = ["Doe", "Jackson", "Anderson", "Silva", "Henderson", 'Defoe', "Terry",
              "Miller", "Hamilton", "Kennedy", "Owen", "Hazard", "Hernandez",
              "Davis", "Puma", "Page", "Robertson", "Martin", "Anderson", "Lee", "Lewis", "Wright",
              "Green", "Carter", "Flores", "Hill", "Walker", "Young", "King", "White", "Moore", "Gonzalez", "Smith"]
    positions = ["Software Engineer",
                 'Marketing Specialist', 'Supervisor']

    for i in range(2, 41):
        pos = random.choices(positions, weights=[0.5, 0.2, 0.2])[0]
        name = random.choice(names)
        lname = random.choice(lnames)
        if pos == "Software Engineer":
            e = Employee(str(random.choice(range(100, 999)))+name[:2]+str(random.choice(range(100, 999)))+lname[:2]+str(random.choice(range(10, 99))), name, lname, random.choice(range(18, 65)), random.choice(range(1000, 4000)), pos,
                         f"{name}.{lname}@email.com")
            insert_data(e)
        else:
            e = Employee(str(random.choice(range(100, 999)))+name[:2]+str(random.choice(range(100, 999)))+lname[:2]+str(random.choice(range(10, 99))), name, lname, random.choice(range(18, 65)), random.choice(range(500, 1500)),
                         pos, f"{name}.{lname}@email.com")
            insert_data(e)

    # Populate News Table with Fake Data
    news = [
        ["""It is crucial to have senior management support for the implementation or modification of a policy, especially where policies relate to employee behaviour. The endorsement and modelling of the behaviour by senior managers and supervisors will encourage staff to take the policies seriously. While management support for a policy is an important first step before actively seeking employee feedback on a proposed policy, the idea for the policy and some of its details may in fact come from staff.""", "Management Support"],
        ["""Using the organisation's computer resources to seek out, access or send any material of an offensive, obscene or defamatory nature is prohibited and may result in disciplinary action.""", "Email policy"],
        ["""Review policies regularly to ensure they are current and in line with any changes within the organisation. Where policies are significantly changed they should be re-issued to all staff and the changes explained to them to ensure they understand the organisation's new directions. These changes should also be widely publicised.""", "Evaluate and review"],
        ["""Involve staff in developing and implementing workplace policies to promote stronger awareness, understanding and ownership of the outcome. Staff involvement also helps to determine how and when the policies might apply, and can assist in identifying possible unintentional outcomes of the policy.""", "Consult with staff"],
        ["""No employee is to commence work, or return to work while under the influence of alcohol or drugs. A breach of this policy is grounds for disciplinary action, up to and including termination of employment. """, "health and safety"],
        ["""To be effective, policies need to be publicised and provided to all existing and new employees. This includes casual, part-time and full-time employees and those on maternity leave or career breaks.Policies should be written in plain English and easily understood by all employees. Consider translating the policies into the appropriate languages for employees whose first language is not English.""", "policies in writing"]

    ]
    for n in range(len(news)):
        content = news[n][0]
        title = news[n][1]
        news_item = News(id=n, content=content, title=title)
        with conn:
            c.execute("INSERT INTO News VALUES(:id,:title,:content)",
                      {"id": n, "content": content, "title": title})


def display_table(table="Employee"):
    c.execute(f"SELECT * FROM {table}")
    return c.fetchall()


def search_employee(search, search_field='name', **kwargs):
    if search_field == "*":
        c.execute("""
        SELECT *
        FROM Employee
        WHERE lname LIKE ('%' || ? || '%') OR
        name LIKE ('%' || ? || '%') OR
        position LIKE ('%' || ? || '%') OR
        email LIKE ('%' || ? || '%') OR
        emp_id LIKE ('%' || ? || '%')

        """, (search, search, search, search, search))
    elif search_field == "salary":
        min_value, max_value = search
        c.execute(f"""
        SELECT *
        FROM Employee
        WHERE salary > {min_value} AND salary < {max_value}
        """)
    else:
        c.execute(
            """SELECT * FROM Employee WHERE ({}) LIKE ('%' || ? || '%') """.format(search_field), (search,))
    return c.fetchall()


def total_salary_per_position():
    c.execute("""SELECT position,SUM(salary) FROM Employee GROUP BY position """)
    return c.fetchall()


def total_salary():
    c.execute("""SELECT SUM(salary) FROM Employee """)
    return c.fetchone()[0]


def employee_per_position():
    c.execute("""SELECT position,COUNT(position) FROM Employee GROUP BY position """)
    return c.fetchall()


def avg_age_per_position():
    c.execute(
        """SELECT position,ROUND(AVG(age),2) FROM Employee GROUP BY position """)
    return c.fetchall()


def avg_age():
    c.execute(
        """SELECT ROUND(AVG(age),2) FROM Employee""")
    return c.fetchone()[0]


def avg_salary():
    c.execute(
        """SELECT ROUND(AVG(salary),2) FROM Employee""")
    return c.fetchone()[0]


def avg_salary_per_position():
    c.execute(
        """SELECT position,ROUND(AVG(salary),2) FROM Employee GROUP BY position """)
    return c.fetchall()


def get_top_n_by_field(field='salary', n=3):

    c.execute("""
        SELECT name,lname,({}) FROM Employee ORDER BY ({}) DESC LIMIT ?
    """.format(field, field), (n,))
    return c.fetchall()


def update_employee(changing_field, new_value, emp_id):
    """
    update a field by a new value
    example: update_employee('name','Helen',0)
    """
    # print(changing_field,new_value,emp_id)
    with conn:
        c.execute("""UPDATE Employee set ({})=?  WHERE emp_id=? """.format(
            changing_field), (new_value, emp_id))
    conn.commit()


def delete_employee(del_value, del_field='emp_id'):
    """
    update a field by a new value
    example: delete_employee(0)
    or delete_employee('Doe','lname')
    """
    with conn:
        c.execute("""DELETE FROM Employee WHERE ({})=? """.format(
            del_field), (del_value,))
        conn.commit()


conn = sqlite3.connect(':memory:')  # in memory database
c = conn.cursor()

c.execute(""" CREATE TABLE Employee(
emp_id PRIMARY KEY,
name VARCHAR(50),
lname VARCHAR(50),
age INTEGER,
salary INTEGER,
position VARCHAR(50),
email VARCHAR(100)
)
""")

c.execute(""" CREATE TABLE News(
id PRIMARY KEY,
title VARCHAR(30),
content VARCHAR(100)
)
""")

# fake_data()
# print(get_top_n_by_salary(3))
# print(display_table("News"))
# print(allowed_emp_id(45) is  None)
# update_employee('emp_id',2,1)


if __name__ == "__main__":

    conn.close()
