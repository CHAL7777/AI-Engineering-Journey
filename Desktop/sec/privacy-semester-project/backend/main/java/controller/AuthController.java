package com.project.privacy.controller;

import com.project.privacy.model.User;
import com.project.privacy.service.AuthService;
import com.project.privacy.util.JwtUtil;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = {"http://localhost:8081", "http://127.0.0.1:8081"})
public class AuthController {

    private final AuthService authService;
    private final JwtUtil jwtUtil;

    public AuthController(AuthService authService, JwtUtil jwtUtil) {
        this.authService = authService;
        this.jwtUtil = jwtUtil;
    }

    public static class RegisterRequest {
        @Email public String email;
        @NotBlank public String password;
        public String fullName;
        public String studentId;
    }

    public static class LoginRequest {
        @Email public String email;
        @NotBlank public String password;
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest req) {
        try {
            User u = authService.register(req.email, req.password, req.fullName, req.studentId);
            String token = jwtUtil.generateToken(u.getEmail());
            return ResponseEntity.ok(Map.of(
                    "token", token,
                    "email", u.getEmail(),
                    "fullName", u.getFullName(),
                    "studentId", u.getStudentId()
            ));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest req) {
        return authService.login(req.email, req.password)
                .map(token -> ResponseEntity.ok(Map.of("token", token)))
                .orElseGet(() -> ResponseEntity.status(401).body(Map.of("error", "Invalid credentials")));
    }
}
