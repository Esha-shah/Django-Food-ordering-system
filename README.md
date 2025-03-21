# 🛒 Online Food Ordering System  

## 📌 Overview  
This is an **online food ordering system** built using **Django** that allows users to browse a categorized menu, add items to a cart, place orders, and track order history. It includes **bulk menu import from Excel, order cancellation, and authentication.**  

---

## 🚀 Features  

### **1️⃣ Food Item Management**  
- Users can browse **food items categorized by type** (e.g., Vegan, Vegetarian, etc.).  
- Each food item has **a name, price, description, image, and dietary labels.**  
- **Data validation** prevents duplicate food items.  

### **2️⃣ Bulk Menu Import (Excel Upload)**  
- Admins can upload menus via an **Excel file instead of manually adding items.**  
- Uses **Pandas and Django ORM** to process the uploaded data.  
- **Error handling and validation** ensure correct formatting.  

### **3️⃣ Shopping Cart & Ordering**  
- Users can **add food items** to their cart.  
- The cart allows updating **quantities, removing items, and reviewing the total price.**  
- Orders are placed after reviewing the cart.  

### **4️⃣ Order Management**  
- Users can track their **current and past orders.**  
- Orders have the following statuses:  
  - **Pending** - Order placed  
  - **Completed** - Order fulfilled  
  - **Canceled** - If canceled within 2 minutes  

### **5️⃣ Order Cancellation Feature**  
- Users can cancel an order within **2 minutes** after placing it.  
- The status updates to **"Canceled"** instead of deleting the order.  

### **6️⃣ Authentication & User Management**  
- Users **must log in** to add items to the cart or place an order.  
- Orders are linked to the **logged-in user.**  

### **7️⃣ Data Validation & Constraints**  
- Enforced **unique constraints** to prevent duplicate food items.  
- Prevented incorrect order placements using **backend validation.**  

---

## 🛠 Tech Stack  

- **Backend:** Django, Python  
- **Database:** PostgreSQL / SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Other Tools:** Django ORM, Pandas (for Excel import), Django Messages  
- **Deployment:** Compatible with **Heroku / AWS / DigitalOcean**  

---

## ⚙️ Usage  

### **Uploading Menu via Excel (Admin Only)**  
1. Navigate to the Admin Panel (`/admin`).  
2. Upload an Excel file with food item details (**name, category, price, description**).  
3. The system validates the file and adds the items to the database.  

### **Placing an Order**  
1. Browse food items and add them to the cart.  
2. Go to the cart page, adjust quantities, and proceed to checkout.  
3. The order is placed, and order history becomes available.  

### **Canceling an Order**  
1. Users can cancel an order within **2 minutes** of placing it.  
2. The order status updates to **"Canceled"** instead of being deleted.  

---

## 🔮 Future Enhancements  

✅ **Payment Integration** (Stripe, Razorpay, PayPal)  
✅ **Live Order Tracking**  
✅ **User Reviews & Ratings for Food Items**  
✅ **Admin Dashboard for Order & Menu Management**  

---
