package com.project.privacy.service;

import com.project.privacy.model.User;
import com.project.privacy.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserService {

    private final UserRepository repo;

    public UserService(UserRepository repo) {
        this.repo = repo;
    }

    public Optional<User> findByEmail(String email) {
        return repo.findByEmail(email);
    }

    public User updateOwnData(User user, String fullName, String studentId) {
        user.setFullName(fullName);
        user.setStudentId(studentId);
        return repo.save(user);
    }
}
