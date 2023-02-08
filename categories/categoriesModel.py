from model import Supplier, Type, Category


def get_categories():
    categories = Category.query.all()
    return categories


def get_types_by_category_id(category_id):
    types = Type.query.filter_by(category_id=category_id).all()
    return types


def get_suppliers_by_type_id(type_id):
    suppliers = Supplier.query.filter_by(type_id=type_id).all()
    print(suppliers)
    return suppliers

