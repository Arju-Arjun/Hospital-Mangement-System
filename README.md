

# **LLAI Hostel Management System**

## **Introduction**
The **LLAI Hostel Management System** is a web-based application designed to efficiently manage hostel operations, including student registrations, room allocations, complaints, and user authentication. Built using **Flask**, the system utilizes an **SQLite** database to securely store all hostel-related information.

---

## **Project Description**
This project provides an automated and streamlined solution for hostel management, minimizing manual efforts in handling student records, room assignments, and complaint resolutions. It offers a seamless experience for both administrators and students through a user-friendly web interface.

---

## **Key Features**
- **User Authentication** (Admin & Students)  
- **Student Registration & Management**  
- **Room Allocation & Tracking**  
- **Complaint Management System**  
- **Database Integration** (SQLite)  
- **Responsive Web Interface**

---

## **Technologies Used**
- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Other:** Jinja Templating, Flask-WTF (Forms)

---

## **Installation & Setup**

### **Prerequisites**
Ensure Python 3.7 or later is installed on your system.

### **Step-by-Step Setup**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/visxnu/LLAI-Hostel-Management-System.git
   cd LLAI-Hostel-Management-System
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```bash
   python database.py
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   The application will be accessible at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## **Project Structure**
```
LLAI-Hostel-Management-System/
│── app.py                  # Main application file
│── database.py             # Database initialization script
│── requirements.txt        # Python dependencies
│── instance/
│   └── hostel.db           # SQLite database file
│── models/                 # Data models
│   ├── complaint.py
│   ├── room.py
│   ├── student.py
│   ├── user.py
│── templates/              # HTML templates
│── static/                 # CSS, JavaScript, and images
└── README.md               # Project documentation
```

---

## **Usage**

- **Admin Dashboard**:  
  Manage student records, room allocations, and handle complaints.

- **Student Portal**:  
  Submit complaints and view assigned room details.

---

## **Contributing**
Feel free to fork the repository and submit pull requests to suggest enhancements or bug fixes.

---

## **License**
This project is licensed under the **MIT License**.

---

## **Contact**
For any inquiries or support, please contact the project maintainer via the GitHub repository.
