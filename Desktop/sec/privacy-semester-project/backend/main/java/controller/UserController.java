package com.project.privacy.controller;

import com.project.privacy.model.User;
import com.project.privacy.service.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/users")
@CrossOrigin(origins = {"http://localhost:8081", "http://127.0.0.1:8081"})
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) { this.userService = userService; }

    @GetMapping("/me")
    public ResponseEntity<?> me(Authentication auth) {
        String email = (String) auth.getPrincipal();
        return userService.findByEmail(email)
                .map(u -> ResponseEntity.ok(Map.of(
                        "email", u.getEmail(),
                        "fullName", u.getFullName(),
                        "studentId", u.getStudentId()
                )))
                .orElseGet(() -> ResponseEntity.status(404).body(Map.of("error", "User not found")));
    }

    public static class UpdateRequest {
        public String fullName;
        public String studentId;
    }

    @PutMapping("/me")
    public ResponseEntity<?> updateMe(Authentication auth, @RequestBody UpdateRequest req) {
        String email = (String) auth.getPrincipal();
        return userService.findByEmail(email)
                .map(u -> {
                    User updated = userService.updateOwnData(u, req.fullName, req.studentId);
                    return ResponseEntity.ok(Map.of(
                            "email", updated.getEmail(),
                            "fullName", updated.getFullName(),
                            "studentId", updated.getStudentId()
                    ));
                })
                .orElseGet(() -> ResponseEntity.status(404).body(Map.of("error", "User not found")));
    }
}
