class Employee {
    String name;
    public Employee(String name) {
        this.name = name;
    }
}

class SalaryCalculator {
    public void calculateSalary(Employee e) {
        System.out.println("Salary calculated for: " + e.name);
    }
}

public class SRPExample {
    public static void main(String[] args) {
        Employee e = new Employee("Karan");
        SalaryCalculator sc = new SalaryCalculator();
        sc.calculateSalary(e);
    }
}
