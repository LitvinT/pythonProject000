from models import Category, Sex, Brand, Model, Product, ProductImage, ProductSize, Role, User, OrderStatus, Order,\
    OrderItem
from utils import parse_stockx


# async def main():
#     # await parse_stockx(category='sneakers')
#     categories = ['dildo']
#     for category in categories:
#         category = Category(name=category, is_published=True)
#         await category.save()

#
# async def main():
#     sexi = ['s', 'm', 'l']
#     for sex in sexi:
#         sex = Sex(sex=sex, is_published=True)
#         await sex.save()


# async def main():
#     br = ['Nike', 'abibus']
#     for a in br:
#         a = Brand(name=a)
#         await a.save()


# async def main():
#     N = ['Air Jordan I', 'Air Jordan II', 'Air Jordan III', 'Air Jordan IV', 'Air Jordan V', 'Air Jordan VI']
#     for n in N:
#         n = Model(name=n, brand_id=5)
#         await n.save()

#1 /article='' Sneakers Shoes


# async def main():
#     N = ['Air Jordan VI?']
#     for n in N:
#         n = Product(
#             name=n,
#             brand_id=5,
#             model_id=18,
#             price=999,
#             category_id=2,
#             sex_id=4,
#             article='L, Shoes jord6/',
#             title=' Air Jordan VI, Shoes,(L)  ',
#             rating=10
#             )
#         await n.save()

# async def main():
#     N = ['https://sneakerfreak.ru/wp-content/uploads/2021/09/Air-Jordan-6-UNC-University-Blue-CT8529-410-Release-Date-On-Feet-scaled.jpg']
#     for n in N:
#         n = ProductImage(
#             product_id=106,
#             url=n
#         )
#         await n.save()


# async def main():
#     N = ['Размер']
#     for n in N:
#         n = ProductSize(
#             product_id=104,
#             size=n,
#             price=989,
#             sex_id=2
#         )
#         await n.save()

# async def main():
#     N = ['izir']
#     for n in N:
#         n = Role(
#             role=n,
#         )
#         await n.save()

# async def main():
#     n = User(
#         role_id=1
#     )
#     await n.save()
#
# async def main():
#     N = ['Admin']
#     for n in N:
#         n = OrderStatus(
#             status=n
#         )
#         await n.save()

# async def main():
#     n = Order(
#         status_id=1,
#         user_id=1
#     )
#     await n.save()

# async def main():
#     n = OrderItem(
#         order_id=1,
#         product_id=104,
#         product_size_id=1
#     )
#     await n.save()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
