# TrendSetu

## Overview
**TrendSetu** is a modern **Thrifting and Renting Platform** built with **Django**. It connects buyers and renters with quality second-hand fashion, including **clothes, accessories, and more**. TrendSetu offers a seamless experience for users looking to buy, rent, or sell fashion items while promoting sustainable fashion choices.
##Status- In Progress
## Features
- **Thrifting Marketplace** – Buy and sell second-hand clothes and accessories.
- **Rental Service** – Rent fashion items for events or daily use.
- **User Authentication** – Secure login and registration.
- **Search and Filters** – Easily browse and find desired products.
- **Wishlist & Favorites** – Save items for later.
- **Vendor Integration** – Connects with vendors from Chaura Bazaar, Ludhiana.
- **AR Try-On** – Try clothes virtually before purchasing.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Tailwind CSS
- **Database:** PostgreSQL
- **Authentication:** Django Auth
- **Payment Gateway:** (To be integrated if needed)

## Installation
### Prerequisites:
- Python 3.9+
- PostgreSQL
- Virtual Environment (optional but recommended)

### Setup Steps:
```bash
# Clone the repository
git clone https://github.com/your-username/trendsetu.git
cd trendsetu

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

# Install dependencies
pip install -r requirements.txt

# Configure database (update settings.py accordingly)
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## Usage
1. **Sign up/Login** to explore TrendSetu.
2. Browse **thrifted and rental items**.
3. Add items to your **wishlist**.
4. Rent or buy items securely.
5. Vendors can **list products for sale/rent**.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Added new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a Pull Request.

## License
MIT License

---

