public class String1 {
    public static void main(String1[] args) {
        // 스트링은 값을 변경할 때 그냥 포인터도 갈아치운다
        String str1 = new String("안녕");
        String str2 = "안녕";
        String str3 = "안녕";
        String str4 = new String("안녕");
         // 스택 메모리값 비교(==)
        System.out.println(str1 == str2);
        System.out.println(str2 == str3);
        System.out.println(str3 == str4);
        System.out.println(str4 == str1);
    }
}
