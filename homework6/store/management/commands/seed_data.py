from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Наполняет базу данных начальными категориями и товарами'

    def handle(self, *args, **kwargs):
        # 1. Создаем категории
        # get_or_create удобен тем, что не создает дубликаты при повторном запуске
        electronics, _ = Category.objects.get_or_create(
            name="Электроника", 
            description="Гаджеты и девайсы"
        )
        home, _ = Category.objects.get_or_create(
            name="Дом", 
            description="Всё для уюта"
        )

        # 2. Создаем товары
        # Привязываем их к созданным категориям через ForeignKey
        products_data = [
            {"name": "Смартфон", "price": 45000, "category": electronics, "desc": "Флагман"},
            {"name": "Ноутбук", "price": 95000, "category": electronics, "desc": "Для работы"},
            {"name": "Лампа", "price": 1500, "category": home, "desc": "Светодиодная"},
        ]

        for item in products_data:
            Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "price": item["price"],
                    "category": item["category"],
                    "description": item["desc"]
                }
            )

        self.stdout.write(self.style.SUCCESS('База данных успешно наполнена товарами!'))