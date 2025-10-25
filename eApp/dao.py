from eApp.models import Category, Product

def get_categories():
    return Category.query.all()

def get_products(kw=None, category_id=None):
    products = Product.query

    if (kw):
        products = products.filter(Product.name.contains(kw))
    if (category_id):
        products = products.filter(Product.category_id==category_id)

    return products.all()