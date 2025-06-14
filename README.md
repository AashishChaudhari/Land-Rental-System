# Land Rental Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 📌 Overview
A Python-based console application for managing land rentals and returns, featuring:
- Land inventory management
- Rental/return processing
- Automatic invoice generation
- Data persistence in text files

## 🚀 Features
- **View available lands** with complete details
- **Rent properties** with duration tracking
- **Return lands** with late fee calculation
- **Generate detailed invoices** (TXT format)
- **Maintain availability status** in database

## 📂 File Structure
LandRentalSystem/
├── main.py # Main program controller
├── read.py # File reading operations
├── operations.py # Core business logic
├── write.py # File writing & invoices
├── LandRentalSystem.txt # Land database
└── invoices/ # Generated invoices

text

## ⚙️ Installation
1. Clone repository:
   ```bash
   git clone [repository-url]
Navigate to project directory

Run with Python 3:

bash
python main.py
🖥️ Usage
text
1. Display available lands
2. Rent available lands
3. Return rented lands
4. Exit
📊 Sample Output
text
Techno Property Nepal
---------------------------------
Kitta    City        Direction  Anna  Price    Availability
---------------------------------
101      Kathmandu   South      4     10000    Available
102      Lalitpur    North      5     50000    Available
📚 Documentation
View Full Project Documentation
[Documentation.pdf](https://github.com/user-attachments/files/20737879/Documentation.pdf)


🛠️ Technical Details
Data Structures: Dictionaries, Lists, Strings

File Handling: TXT file persistence

Error Handling: Robust input validation

Modular Design: Separated concerns

📅 Future Enhancements
GUI implementation

Database integration

User authentication

Email notifications
