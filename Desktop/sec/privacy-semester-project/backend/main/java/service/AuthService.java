package com.project.privacy.service;

import com.project.privacy.model.User;
import com.project.privacy.repository.UserRepository;
import com.project.privacy.util.JwtUtil;
import com.project.privacy.util.PasswordUtil;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class AuthService {

    private final UserRepository userRepository;
    private final JwtUtil jwtUtil;

    public AuthService(UserRepository userRepository, JwtUtil jwtUtil) {
        this.userRepository = userRepository;
        this.jwtUtil = jwtUtil;
    }

    public User register(String email, String rawPassword, String fullName, String studentId) {
        userRepository.findByEmail(email).ifPresent(u -> {
            throw new IllegalArgumentException("Email already in use");
        });
        String hash = PasswordUtil.hash(rawPassword);
        User user = new User(email, hash, fullName, studentId);
        return userRepository.save(user);
    }

    public Optional<String> login(String email, String rawPassword) {
        Optional<User> userOpt = userRepository.findByEmail(email);
        if (userOpt.isPresent() && PasswordUtil.matches(rawPassword, userOpt.get().getPasswordHash())) {
            String token = jwtUtil.generateToken(userOpt.get().getEmail());
            return Optional.of(token);
        }
        return Optional.empty();
    }
}
