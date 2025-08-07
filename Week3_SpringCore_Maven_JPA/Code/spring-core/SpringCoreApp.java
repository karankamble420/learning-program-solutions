import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.context.annotation.*;

@Component
class HelloService {
    public String sayHello() {
        return "Hello from Spring Core!";
    }
}

@Component
class HelloApp {
    @Autowired
    HelloService service;

    public void display() {
        System.out.println(service.sayHello());
    }
}

@Configuration
@ComponentScan(basePackages = ".")
class AppConfig {}

public class SpringCoreApp {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        HelloApp app = context.getBean(HelloApp.class);
        app.display();
        context.close();
    }
}
