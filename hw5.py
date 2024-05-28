from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date, ForeignKey
from sqlalchemy import or_, and_, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+pg8000://{db_user}:{db_password}@localhost:5432/Sales'
engine = create_engine(db_url)

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    salesman = relationship("Salesman", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")

class Salesman(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)

    sales = relationship("Sale", back_populates="salesman")

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)

    sales = relationship("Sale", back_populates="customer")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

salesman1 = Salesman(surname="Іванов", name="Іван")
salesman2 = Salesman(surname="Петров", name="Петро")
session.add_all([salesman1, salesman2])
session.commit()

customer1 = Customer(surname="Сидорова", name="Олена")
customer2 = Customer(surname="Ковальчук", name="Олексій")
session.add_all([customer1, customer2])
session.commit()

sale1 = Sale(amount=1000, salesman=salesman1, customer=customer1)
sale2 = Sale(amount=1500, salesman=salesman1, customer=customer2)
sale3 = Sale(amount=2000, salesman=salesman2, customer=customer1)
session.add_all([sale1, sale2, sale3])
session.commit()

while True:
    print("Введіть команду")
    print("1. Відобразити усі угоди")
    print("2. Відобразити угоди конкретного продавця")
    print("3. Відобразити максимальну за сумою угоду")
    print("4. Відобразити мінімальну за сумою угоду")
    print("5. Відобразити максимальну суму угоди для конкретного продавця")
    print("6. Відобразити мінімальну за сумою угоду для конкретного продавця")
    print("7. Відобразити максимальну за сумою угоду для конкретного покупця")
    print("8. Відобразити мінімальну за сумою угоду для конкретного покупця")
    print("9. Відобразити продавця з максимальною сумою продажів за всіма угодами")
    print("10. Відобразити продавця з мінімальною сумою продажів за всіма угодами")
    print("11. Відобразити покупця з максимальною сумою покупок за всіма угодами")
    print("12. Відобразити середню суму покупки для конкретного покупця")
    print("13. Відобразити середню суму покупки для конкретного продавця")
    print("14. Додати нову угоду")
    print("15. Внести зміни до угоди")
    print("16. Видалити угоду")

    command = input('Номер команди:')

    if command == 'exit':
        break

    if command == '1':
        result = session.query(Sale).all()
        for sale in result:
            print(
                f"ID: {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.surname} {sale.salesman.name}, Клієнт: {sale.customer.surname} {sale.customer.name}")

    elif command == '2':
        salesman_id = input('ID продавця: ')
        result = session.query(Sale).filter_by(salesman_id=salesman_id).all()
        for sale in result:
            print(f"ID: {sale.id}, Сума: {sale.amount}, Клієнт: {sale.customer.surname} {sale.customer.name}")

    elif command == '3':
        max_amount = session.query(func.max(Sale.amount)).scalar()
        max_sale = session.query(Sale).filter_by(amount=max_amount).first()
        print(f"ID: {max_sale.id}, Сума: {max_sale.amount}, Продавець: {max_sale.salesman.surname} {max_sale.salesman.name}, Клієнт: {max_sale.customer.surname} {max_sale.customer.name}")

    elif command == '4':
        min_amount = session.query(func.min(Sale.amount)).scalar()
        min_sale = session.query(Sale).filter_by(amount=min_amount).first()
        print(f"ID: {min_sale.id}, Сума: {min_sale.amount}, Продавець: {min_sale.salesman.surname} {min_sale.salesman.name}, Клієнт: {min_sale.customer.surname} {min_sale.customer.name}")

    elif command == '5':
        salesman_id = input('ID продавця: ')
        max_amount = session.query(func.max(Sale.amount)).filter_by(salesman_id=salesman_id).scalar()
        max_sale = session.query(Sale).filter_by(amount=max_amount, salesman_id=salesman_id).first()
        print(f"ID: {max_sale.id}, Сума: {max_sale.amount}, Клієнт: {max_sale.customer.surname} {max_sale.customer.name}")

    elif command == '6':
        salesman_id = input('ID продавця: ')
        min_amount = session.query(func.min(Sale.amount)).filter_by(salesman_id=salesman_id).scalar()
        min_sale = session.query(Sale).filter_by(amount=min_amount, salesman_id=salesman_id).first()
        print(f"ID: {min_sale.id}, Сума: {min_sale.amount}, Клієнт: {min_sale.customer.surname} {min_sale.customer.name}")

    elif command == '7':
        customer_id = input('ID покупця: ')
        max_amount = session.query(func.max(Sale.amount)).filter_by(customer_id=customer_id).scalar()
        max_sale = session.query(Sale).filter_by(amount=max_amount, customer_id=customer_id).first()
        print(f"ID: {max_sale.id}, Сума: {max_sale.amount}, Продавець: {max_sale.salesman.surname} {max_sale.salesman.name}")

    elif command == '8':
        customer_id = input('ID покупця: ')
        min_amount = session.query(func.min(Sale.amount)).filter_by(customer_id=customer_id).scalar()
        min_sale = session.query(Sale).filter_by(amount=min_amount, customer_id=customer_id).first()
        print(f"ID: {min_sale.id}, Сума: {min_sale.amount}, Продавець: {min_sale.salesman.surname} {min_sale.salesman.name}")

    elif command == '9':
        max_salesman = session.query(Salesman).join(Sale).group_by(Salesman.id).order_by(func.sum(Sale.amount).desc()).first()
        total_sales = session.query(func.sum(Sale.amount)).filter_by(salesman_id=max_salesman.id).scalar()
        print(f"Продавеець: {max_salesman.surname} {max_salesman.name}, Загальний обсяг продажів: {total_sales}")

    elif command == '10':
        min_salesman = session.query(Salesman).join(Sale).group_by(Salesman.id).order_by(func.sum(Sale.amount)).first()
        total_sales = session.query(func.sum(Sale.amount)).filter_by(salesman_id=min_salesman.id).scalar()
        print(f"Продавець: {min_salesman.surname} {min_salesman.name}, Загальний обсяг продажів: {total_sales}")

    elif command == '11':
        max_customer = session.query(Customer).join(Sale).group_by(Customer.id).order_by(func.sum(Sale.amount).desc()).first()
        total_purchases = session.query(func.sum(Sale.amount)).filter_by(customer_id=max_customer.id).scalar()
        print(f"Клієнт: {max_customer.surname} {max_customer.name}, Загальна кількість покупок: {total_purchases}")

    elif command == '12':
        customer_id = input('ID покупця: ')
        avg_purchase = session.query(func.avg(Sale.amount)).filter_by(customer_id=customer_id).scalar()
        print(f"Середня сума покупки: {avg_purchase}")

    elif command == '13':
        salesman_id = input('ID продавця: ')
        avg_sale = session.query(func.avg(Sale.amount)).filter_by(salesman_id=salesman_id).scalar()
        print(f"Середня сума продажу: {avg_sale}")

    elif command == '14':
        amount = input('Сума угоди: ')
        salesman_id = input('ID продавця: ')
        customer_id = input('ID покупця: ')
        new_sale = Sale(amount=int(amount), salesman_id=int(salesman_id), customer_id=int(customer_id))
        session.add(new_sale)
        session.commit()
        print("Угода додана.")

    elif command == '15':
        sale_id = input('ID угоди: ')
        sale = session.query(Sale).get(int(sale_id))
        if sale:
            sale.amount = int(input('Нова сума угоди: '))
            session.commit()
            print("Угода оновлена.")
        else:
            print("Угода не знайдена.")

    elif command == '16':
        sale_id = input('ID угоди: ')
        sale = session.query(Sale).get(int(sale_id))
        if sale:
            session.delete(sale)
            session.commit()
            print("Угода видалена.")
        else:
            print("Угода не знайдена.")








