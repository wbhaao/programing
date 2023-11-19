public class List {
    public static void main(String1[] args) {
        int[] a = new int[3];
        int b[];
        // 두가지 버전으로 선언 가능

        // 힙 메모리에 개겣 생성하려면 new 각 붙어야 함
        int[] c = new int[3];
        String1 s[] = new String1[5];
    
        // int 자료형 3개를 저장할 수 있는 공간을 힙 메모리에
        // 넣어 두고 어디에 넣었는지를 참조 변수 a에 저장하라!
    
        boolean[] array5 = new boolean[3];
        int[] array6 = new int[5];
        double[] array7 = new double[7];
        String1[] array8 = new String1[9]; 
        
        a[0] = 1;
        a[1] = 2;
        a[2] = 3;
        System.out.println(a[0]);
        // -1, 오버인덱싱은 에러 발생
        
        // 선언이랑 같이 초기화
        int[] h = new int[]{3, 4, 5};
        System.out.println(h);

        int[] k = new int[]{3, 4, 5};
        int[] j;
        j = new int[]{3, 4, 5}; 
        int[] w = {3, 4, 5}; // (O)
        // int[] e; 이건 안됨
        // e = {3, 4, 5}; 

        int[][] u = {{1, 2, 3}, {4, 5, 6}}; // (◯)
        //int[][] l;
        //l = {{1, 2, 3}, {4, 5, 6}}; // (X)

        
    }
}
