# Import necessary utilities and functions from SQLAlchemy
from sqlalchemy import create_engine, select, desc, func
from sqlalchemy.orm import Session

# Import user-defined configuration settings and model definitions
from config import DATABASE_URL
from models import Base, Project, Task, Sale

# Create a database connection engine, setting echo to True for logging SQL statements
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database as per the defined models
Base.metadata.create_all(engine)


# Function to add a project and its related tasks
def add_project_with_tasks(_session, title, description, task_descriptions):
    # Create a new Project instance
    project = Project(title=title, description=description)
    # Add the project to the current session
    _session.add(project)
    # Flush the session to obtain any autogenerated fields (like project_id)
    _session.flush()

    # Create associated tasks for the given project
    tasks = [Task(project_id=project.project_id, description=task_desc) for task_desc in task_descriptions]
    # Add these tasks in bulk to the session
    _session.bulk_save_objects(tasks)
    # Commit the changes to the database
    _session.commit()


# Function to print tasks associated with a given project title
def print_tasks_for_project(_session, project_title):
    # Retrieve the project by its title
    project = _session.execute(select(Project).where(Project.title == project_title)).scalar()

    # Fetch tasks associated with the found project
    tasks = _session.execute(select(Task).where(Task.project_id == project.project_id)).all()
    for task in tasks:
        print(task)


# Function to insert sample sales data
def insert_sample_data(_session):
    # Sample data for sales
    data = [
        Sale(order_num=1, order_type="Online", cust_name="John", prod_category="Electronics", prod_number="E123",
             prod_name="Laptop", quantity=2, price=1000, discount=50, order_total=1950),
        Sale(order_num=2, order_type="Online", cust_name="Doe", prod_category="Clothing", prod_number="C456",
             prod_name="T-Shirt", quantity=5, price=20, discount=5, order_total=95),
        Sale(order_num=3, order_type="Online", cust_name="Smith", prod_category="Books", prod_number="B789",
             prod_name="Novel", quantity=3, price=15, discount=0, order_total=45),
        Sale(order_num=4, order_type="Online", cust_name="Davis", prod_category="Electronics", prod_number="E101",
             prod_name="Headphones", quantity=1, price=150, discount=10, order_total=140),
        Sale(order_num=5, order_type="Online", cust_name="White", prod_category="Home", prod_number="H202",
             prod_name="Mixer", quantity=1, price=100, discount=0, order_total=100)
    ]
    # Save the sales data in bulk
    _session.bulk_save_objects(data)
    # Commit changes to the database
    _session.commit()


# Function to find and return the most expensive order
def most_expensive_order(_session):
    # Query for the sale with the highest order total
    return _session.query(Sale).order_by(desc(Sale.order_total)).first()
    # An alternative method is commented out below:
    # max_total = _session.query(func.max(Sale.order_total)).scalar()
    # return _session.query(Sale).filter(Sale.order_total == max_total).first()


# Main execution point

if __name__ == '__main__':
    with Session(engine) as session:
        # Uncomment below lines to add data
        # add_project_with_tasks(session, 'Organize closet', 'Organize closet by color and style', [
        #     'Decide what clothes to donate',
        #     'Organize summer clothes',
        #     'Organize winter clothes'
        # ])

        # print_tasks_for_project(session, 'Organize closet')
        # insert_sample_data(session)
        # Fetch the most expensive order
        expensive_order = most_expensive_order(session)
        # If an order is found, print details. Otherwise, print a default message.
        if expensive_order:
            print(
                f"The most expensive order was made by {expensive_order.cust_name} with a total of {expensive_order.order_total}.")
        else:
            print("No orders found in the database.")
