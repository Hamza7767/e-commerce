"""Seed the database with sample categories, products, and an admin user."""

from app import create_app
from extensions import db
from models import Category, Product, User


def seed():
    app = create_app()
    with app.app_context():
        if User.query.filter_by(username="admin").first():
            print("Database already seeded. Skipping.")
            return

        admin = User(username="admin", email="admin@shop.com", is_admin=True)
        admin.set_password("admin123")
        db.session.add(admin)

        demo = User(username="demo", email="demo@shop.com")
        demo.set_password("demo123")
        db.session.add(demo)

        categories_data = [
            ("Electronics", "electronics"),
            ("Clothing", "clothing"),
            ("Books", "books"),
            ("Home & Garden", "home-garden"),
        ]

        categories = {}
        for name, slug in categories_data:
            cat = Category(name=name, slug=slug)
            db.session.add(cat)
            categories[slug] = cat

        db.session.flush()

        products_data = [
            {
                "name": "Wireless Headphones",
                "description": "Premium noise-cancelling wireless headphones with 30-hour battery life.",
                "price": 79.99,
                "stock": 50,
                "category": "electronics",
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
            },
            {
                "name": "Smart Watch",
                "description": "Fitness tracking smartwatch with heart rate monitor and GPS.",
                "price": 149.99,
                "stock": 30,
                "category": "electronics",
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
            },
            {
                "name": "Laptop Stand",
                "description": "Ergonomic aluminum laptop stand for better posture.",
                "price": 34.99,
                "stock": 100,
                "category": "electronics",
                "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400",
            },
            {
                "name": "Classic T-Shirt",
                "description": "100% cotton comfortable t-shirt available in multiple colors.",
                "price": 19.99,
                "stock": 200,
                "category": "clothing",
                "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
            },
            {
                "name": "Denim Jeans",
                "description": "Slim fit denim jeans with stretch comfort.",
                "price": 49.99,
                "stock": 80,
                "category": "clothing",
                "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400",
            },
            {
                "name": "Running Shoes",
                "description": "Lightweight running shoes with cushioned sole.",
                "price": 89.99,
                "stock": 60,
                "category": "clothing",
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
            },
            {
                "name": "Python Programming Book",
                "description": "Complete guide to Python programming for beginners and experts.",
                "price": 39.99,
                "stock": 45,
                "category": "books",
                "image_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400",
            },
            {
                "name": "Web Development Guide",
                "description": "Modern web development with HTML, CSS, JavaScript and Flask.",
                "price": 44.99,
                "stock": 35,
                "category": "books",
                "image_url": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400",
            },
            {
                "name": "Indoor Plant Set",
                "description": "Set of 3 low-maintenance indoor plants with decorative pots.",
                "price": 29.99,
                "stock": 25,
                "category": "home-garden",
                "image_url": "https://images.unsplash.com/photo-1416879595882-3373a048049b?w=400",
            },
            {
                "name": "Desk Lamp",
                "description": "LED desk lamp with adjustable brightness and color temperature.",
                "price": 24.99,
                "stock": 70,
                "category": "home-garden",
                "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400",
            },
        ]

        for pdata in products_data:
            product = Product(
                name=pdata["name"],
                description=pdata["description"],
                price=pdata["price"],
                stock=pdata["stock"],
                category_id=categories[pdata["category"]].id,
                image_url=pdata["image_url"],
            )
            db.session.add(product)

        db.session.commit()
        print("Database seeded successfully!")
        print("  Admin: admin / admin123")
        print("  Demo user: demo / demo123")


if __name__ == "__main__":
    seed()
