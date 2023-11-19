class A {
        A() {
            System.out.println("첫 번째 생성자");
        }
        A(int a) {
            this();
            System.out.println("두 번째 생성자");
        }
       /*
        void abc() {
            this();
        }
       */
    }

public class class1 {
    // 클래스는 일반 클래스, 추상 클래스
    // 인터페이스
    // 추상클래스 : 하나 이상의 추상 메서드가 있는 것
    // 인터페이스 : 모든 메서드가 추상메서드인 것

    //[[2023-11-19-19-51-24.png]]
    //[[2023-11-19-19-54-59.png]]
    //[[2023-11-19-20-15-33.png]]

    //가변길이
    // public static void main(String[] args) {
    //     // 가변 길이 int 배열 입력매개변수
    //     method1(1, 2); // 입력매개변수 길이: 2
    //     method1(1, 2, 3); // 입력매개변수 길이: 3
    //     method1(); // 입력매개변수 길이: 0
    //     // 가변 길이 String 배열 입력매개변수
    //     method2("안녕", "방가"); // 입력매개변수 길이: 2
    //     method2("땡큐", "베리", "감사"); // 입력매개변수 길이: 3
    //     method2(); // 입력매개변수 길이: 0
    //    }
    //    public static void method1(int... values) {
    //     System.out.println("입력매개변수 길이 : " + values.length);
    //     for (int i = 0; i < values.length; i++)
    //     System.out.print(values[i] + " ");
    //     System.out.println();
    //    }
    //    public static void method2(String... values) {
    //     System.out.println("입력매개변수 길이 : " + values.length);
    //     for (int i = 0; i < values.length; i++)
    //     System.out.print(values[i] + " ");
    //     System.out.println();
    // }

    // this는 기본적으로 붙여주지만, 
    //[[2023-11-19-20-22-40.png]]
    // 이 경우에는 붙여야한다

    //this()는 그 클래스의 생성자를 호출하는 것이다. this()는 생성자 내부에서 호출하여야 한다.
    
    public static void main(String[] args) {
        // 객체 생성
        A a1 = new A();
        System.out.println();
        A a2 = new A(3);
    }
    //>>>첫 번째 생성자

    //>>>첫 번째 생성자
    //>>>두 번째 생성자

    // 292
}
