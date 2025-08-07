import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class UserController {

    @GetMapping("/hello")
    public String hello() {
        return "Welcome to REST API!";
    }

    @PostMapping("/user")
    public String createUser(@RequestBody User user) {
        return "Received user: " + user.getName() + ", Age: " + user.getAge();
    }
}
