import json
import jsonschema
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, REAL, ForeignKey
from sqlalchemy.orm.session import sessionmaker

engine = create_engine("sqlite:///Treatment_of_goods.db", echo=True)

with open("goods.schema.json", "r", encoding="UTF-8") as file_json_schema:
    data_schema = json.load(file_json_schema)
with open("goods.json", "r", encoding="UTF-8") as file_json:
    data = json.load(file_json)

validate = jsonschema.validate(data, schema=data_schema)

base = declarative_base()


class Good(base):  # type: ignore
    """Создает таблицу goods с именем и параметрами товара."""

    __tablename__: str = "goods"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    package_height = Column(REAL)
    package_width = Column(REAL)
    shops = relationship("Shop", backref="good")


class Shop(base):  # type: ignore
    """Создает таблицу shops с количеством и расположением товара."""

    __tablename__: str = "shops"
    location = Column(String, primary_key=True)
    amount = Column(Integer)
    good_id = Column(Integer, ForeignKey("goods.id"), primary_key=True)


base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()


def load_in_base(parsed_json: dict, engine: Engine) -> None:
    """Парсит и загружает данные в БД."""
    local_json = parsed_json.copy()

    shops = local_json.pop("location_and_quantity")
    params = local_json.pop("package_params")

    local_json["package_width"] = params["width"]
    local_json["package_height"] = params["height"]
    good = Good(**local_json)

    with Session(bind=engine) as db:
        db.merge(good)
        db.commit()

    for shop in shops:
        shop_obj = Shop(**shop, good_id=good.id)
        db.merge(shop_obj)
        db.commit()
    return None


load_in_base(data, engine)
