from sqlalchemy import create_engine, select
from sqlalchemy import Table, Column, Integer, Float, String, MetaData

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/red30', echo=True)
metadata = MetaData()

# sales_table = Table('Sales',
#                     metadata,
#                     Column('order_num', Integer, primary_key=True),
#                     Column('cust_name', String),
#                     Column('prod_number', String),
#                     Column('prod_name', String),
#                     Column('quantity', Float),
#                     Column('price', Float),
#                     Column('discount', Float),
#                     Column('order_total', Float)
#                     )

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)

with engine.connect() as conn:
    # Read
    for row in conn.execute(select(sales_table)):
        print(row)

    insert_statement = sales_table.insert().values(order_num=1105910,
                                                   cust_name='Or Hasson',
                                                   prod_number='EB521',
                                                   prod_name='Understanding AI',
                                                   quantity=3,
                                                   price=19.5,
                                                   discount=0,
                                                   order_total=58.5)

    conn.execute(insert_statement)

    # Update
    update_statement = sales_table.update().where(sales_table.c.order_num == 1105910).values(quantity=2, order_total=37)
    conn.execute(update_statement)

    # Confirm Update
    reselect_statement = sales_table.select().where(sales_table.c.order_num == 1105910)
    updated_sale = conn.execute(reselect_statement).first()

    # Delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num == 1105910)
    conn.execute(delete_statement)

    # Confirm Delete
    not_found_set = conn.execute(reselect_statement)
    print(not_found_set.rowcount)
