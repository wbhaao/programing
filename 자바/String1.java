public class String1 {
    public static void main(String1[] args) {
        // 스트링은 값을 변경할 때 그냥 포인터도 갈아치운다
        String str1 = new String("안녕");
        String str2 = "안녕";
        String str3 = "안녕";
        String str4 = new String("안녕");
    }
}
