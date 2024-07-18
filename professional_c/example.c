
#include <stdio.h>

// 그냥 출력
#define LOOP_3(X, ...) \
    printf("%s\n", #X);
// 인자 하나 출력한다음 남은 인자 넘기기
#define LOOP_2(X, ...) \
    printf("%s\n", #X); \
    LOOP_3(__VA_ARGS__)
// 인자 하나 출력한다음 남은 인자 넘기기
#define LOOP_1(X, ...) \
    printf("%s\n", #X); \
    LOOP_2(__VA_ARGS__)
// 일단 인자 전부 넘기기
#define LOOP(...) \
    LOOP_1(__VA_ARGS__)

int main() {
    LOOP(copy paste cut)
    LOOP(copy, paste, cut)
    LOOP(copy, paste, cut, select)
    
    return 0;
}

// 조건부 컴파일 예 예제 1-7
#define CONDITION

int main() {
    #ifdef CONDITION
        int i = 0;
        i++;
    #endif
        int j=0;
    return 0;
}

// 포인터 변수
// C에서 포인터 변수를 선언하고 사용하는 방법
int main() {
    int var = 100;
    int* ptr = 0;
    // 참조 연산자
    ptr = &var;
    // 역참조 연산자
    *ptr = 200;
    return 0;
}

// 모두 올바른 포인터 선언 방법
int* ptr;
int * ptr;
int *ptr;

// 메모리 프로파일러

// 산술연산 간격

// 두포인터의 산술연산 간격

#include <stdio.h>

int main(int argc, char** argv) {
    int var = 1;

    int* int_ptr = NULL;
    int_ptr = &var;

    char* char_ptr = NULL;
    char_ptr = (char*)&var;
}

// 제네릭 포인터, 제네릭이란 void르,ㄹ 말하는듯
// 평소 제네릭 포인터는 쓸모없지만 제네릭 함수와 같이 쓰면 유용해진다

