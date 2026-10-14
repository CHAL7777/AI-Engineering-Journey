# Secure Student Data Web Application

A privacy-first web application for managing student data with industry-standard security practices. This project demonstrates secure authentication, data isolation, and minimal data collection principles.

## 🔒 Features

- **Secure Authentication**: JWT-based stateless authentication with secure token management
- **Password Security**: BCrypt one-way hashing - passwords are never stored in plain text
- **Data Isolation**: Users can only access and modify their own data
- **Minimal Data Collection**: Only essential student information is collected
- **Input Validation**: Server-side validation for all user inputs
- **CORS Protection**: Configured frontend origins for secure cross-origin requests

## 🛠️ Technology Stack

### Backend
- **Java 17** with Spring Boot 3.1.5
- **Spring Security** for authentication and authorization
- **Spring Data JPA** for database operations
- **JWT (JSON Web Tokens)** for session management
- **MariaDB** as the relational database
- **BCrypt** for password hashing

### Frontend
- **Vanilla HTML5, CSS3, JavaScript**
- Responsive design with clean UI
- AJAX/Fetch API for backend communication

## 📁 Project Structure

```
privacy-semester-project/
├── README.md
├── backend/
│   ├── pom.xml                          # Maven configuration
│   ├── main/
│   │   ├── java/
│   │   │   ├── MainApplication.java     # Spring Boot entry point
│   │   │   ├── JwtUtil.java             # JWT token generation/validation
│   │   │   ├── PasswordUtil.java        # BCrypt password hashing
│   │   │   ├── controller/
│   │   │   │   ├── AuthController.java  # Auth endpoints (register/login)
│   │   │   │   └── UserController.java  # User profile endpoints
│   │   │   ├── model/
│   │   │   │   └── User.java            # User entity model
│   │   │   ├── repository/
│   │   │   │   └── UserRepository.java  # Database operations
│   │   │   ├── service/
│   │   │   │   ├── AuthService.java     # Authentication logic
│   │   │   │   └── UserService.java     # User management logic
│   │   │   └── security/
│   │   │       ├── JwtAuthFilter.java   # JWT authentication filter
│   │   │       └── SecurityConfig.java  # Security configuration
│   │   └── resources/
│   │       └── application.properties   # Application configuration
│   └── target/                          # Compiled artifacts
└── frontend/
    ├── index.html                       # Landing page
    ├── login.html                       # Login page
    ├── register.html                    # Registration page
    ├── dashboard.html                   # User dashboard
    ├── css/
    │   └── style.css                    # Application styles
    └── app.js                           # Frontend JavaScript logic
```

## 🚀 Getting Started

### Prerequisites

- **Java Development Kit 17** or higher
- **Maven 3.6+**
- **MariaDB** (or MySQL) database server
- **Git** for version control

### Database Setup

1. Install MariaDB if not already installed:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install mariadb-server

   # Start MariaDB
   sudo systemctl start mariadb
   sudo systemctl enable mariadb
   ```

2. Create the database:
   ```bash
   sudo mysql -u root -p
   ```
   Then execute:
   ```sql
   CREATE DATABASE privacydb;
   EXIT;
   ```

### Backend Configuration

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Configure the database connection in `main/application.properties`:
   ```properties
   spring.datasource.url=jdbc:mariadb://localhost:3306/privacydb
   spring.datasource.username=root
   spring.datasource.password=your_password
   ```

3. **Security Note**: Change the JWT secret in `application.properties`:
   ```properties
   app.jwt.secret=use_a_strong_random_secret_in_production
   ```

### Running the Backend

```bash
cd backend
mvn spring-boot:run
```

The backend will start on `http://localhost:8080`

### Running the Frontend

You can serve the frontend using any static file server:

**Using Python:**
```bash
cd frontend
python3 -m http.server 8081
```

**Using Node.js (http-server):**
```bash
cd frontend
npx http-server -p 8081
```

Then open `http://localhost:8081` in your browser.

## 📡 API Documentation

### Authentication Endpoints

#### Register New User
```http
POST /api/auth/register
Content-Type: application/json

{
    "email": "student@university.edu",
    "password": "securePassword123",
    "fullName": "John Doe",
    "studentId": "STU2024001"
}
```

**Response (201 Created):**
```json
{
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "email": "student@university.edu",
    "fullName": "John Doe",
    "studentId": "STU2024001"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
    "email": "student@university.edu",
    "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
    "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Response (401 Unauthorized):**
```json
{
    "error": "Invalid credentials"
}
```

### User Endpoints (Protected)

All user endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

#### Get Current User Profile
```http
GET /api/users/me
```

**Response (200 OK):**
```json
{
    "email": "student@university.edu",
    "fullName": "John Doe",
    "studentId": "STU2024001"
}
```

#### Update Current User Profile
```http
PUT /api/users/me
Content-Type: application/json

{
    "fullName": "John Updated Doe",
    "studentId": "STU2024002"
}
```

**Response (200 OK):**
```json
{
    "email": "student@university.edu",
    "fullName": "John Updated Doe",
    "studentId": "STU2024002"
}
```

## 🔐 Security Features

### Authentication Security
- **JWT Tokens**: Stateless authentication with configurable expiration (default: 24 hours)
- **Secure Token Storage**: Tokens stored in localStorage on frontend
- **Bearer Token Format**: Standard Authorization header format

### Password Security
- **BCrypt Hashing**: Industry-standard password hashing with salt
- **No Plain Text**: Passwords are never stored or transmitted in plain text
- **Server-side Hashing**: Hashing happens on the server, not client

### Data Protection
- **User Data Isolation**: Each user can only access their own data
- **Input Validation**: Email format validation, required field checks
- **SQL Injection Protection**: JPA/Hibernate prevents SQL injection attacks

### Network Security
- **CORS Configuration**: Strict origin control for cross-origin requests
- **HTTPS Recommended**: Should use HTTPS in production
- **CSRF Disabled**: Intentionally disabled for API simplicity (JWT provides protection)

## ⚠️ Production Considerations

Before deploying to production, make these critical changes:

1. **Change JWT Secret**: Use a strong, random secret (at least 256 bits)
   ```properties
   app.jwt.secret=your_very_long_random_secret_string
   ```

2. **Use Environment Variables**:
   ```properties
   app.jwt.secret=${JWT_SECRET:change_this_default}
   spring.datasource.password=${DB_PASSWORD}
   ```

3. **Enable HTTPS**: Configure SSL/TLS certificates

4. **Secure Cookie Settings**: Consider HttpOnly cookies for tokens

5. **Shorter Token Expiration**: Reduce JWT expiration for better security

6. **Rate Limiting**: Add rate limiting to prevent brute force attacks

7. **Logging**: Implement proper audit logging

## 📝 License

This project is created for educational purposes as a semester project focusing on privacy and security best practices.

## 👥 Author

Created as part of a privacy-focused software engineering semester project.

## 📚 Learn More

- [Spring Security Documentation](https://spring.io/projects/spring-security)
- [JWT.io - JSON Web Tokens](https://jwt.io/)
- [BCrypt Password Hashing](https://en.wikipedia.org/wiki/Bcrypt)
- [OWASP Security Guidelines](https://owasp.org/)

