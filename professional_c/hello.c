/*
C 매크로에 대해서 알아보자
매크로로 인해 가독성이 떨어진다고 하는데
매크로는 실무에서 매우 중요한 기능 중 하나이다

매크로는 다음과 같이 다양하게 활용할 수 있다
- 상수 정의하기
- C 함수를 작성하지 않고 함수로 사용하기
- 루프 풀기
- 헤더 가드
- 코드 생성
- 조건부 컴파일

매크로는 #define 지시자를 이용해 정의
*/

// C에서 매크로 정의하기
#define ABC 5
int main(int argc, char** argv) {
    int x = 2;
    int y = ABC;
    int z = x + y;
    return 0;
}

// C에서 매크로 함수 아닌 매크로 함수 정의하기
#define ADD(x, y) x + y

int main1(int argc, char** argv) {
    int x = 2;
    int y = ABC;
    int z = ADD(x, y);
    return 0;
}

// 선언되지 않은 식별자 오류가 발생하는 매크로 정의
#define CODE \
printf("%d\n", i);

int main() {
    CODE
    return 0;
}

// 여기서 i가 선언되지 않았다고 에러가 표시된다

// 루프를 생성하는 매크로를 사용하기
#include <stdio.h>

#define PRINT(a) printf("%d\n", a);
#define LOOP(v, s, e) for (int v = s; v <= e; v ++) {
#define ENDLOOP }

int main() {
    LOOP(counter, 1, 10)
    PRINT(counter)
    ENDLOOP
    return 0;
}
// 매크로는 존나게 신기하다

// DSL이 무엇인가
/*
DSL(도메인 특화 언어)은 특정 분야나 문제를 해결하기 위해 설계된 프로그래밍 언어나 명령어 집합입니다. 예를 들어, SQL은 데이터베이스 쿼리를 위한 DSL이고, HTML은 웹 페이지 구조를 정의하기 위한 DSL입니다. 일반 프로그래밍 언어보다 특정 작업에 더 효율적이고 이해하기 쉽도록 설계되었습니다.
*/

// 예제 1-4에서 #과 ##을 사용하기
#include <stdio.h>  // 표준 입출력 함수를 사용하기 위한 헤더 파일 포함
#include <string.h>  // 문자열 처리 함수를 사용하기 위한 헤더 파일 포함

// CMD 매크로는 주어진 NAME을 사용하여 두 가지 작업을 수행합니다.
// 1. char NAME_cmd[256]이라는 배열을 선언합니다.
// 2. NAME_cmd 배열에 NAME 문자열을 복사합니다.
#define CMD(NAME) \
char NAME ## _cmd[256] = ""; \
strcpy(NAME ## _cmd, #NAME)

int main() {
    // CMD 매크로를 사용하여 copy_cmd, paste_cmd, cut_cmd 배열을 선언하고
    // 각각에 "copy", "paste", "cut" 문자열을 복사합니다.
    CMD(copy);
    CMD(paste);
    CMD(cut);
    
    char cmd[256];  // 사용자 입력을 저장할 배열 선언
    scanf("%s", cmd);  // 사용자로부터 문자열을 입력받음

    // 입력받은 문자열과 정의된 명령어 문자열을 비교하여 일치하는지 확인합니다.
    if (strcmp(cmd, copy_cmd) == 0) {
        // 입력이 "copy"와 일치할 때 수행할 코드
    }
    if (strcmp(cmd, paste_cmd) == 0) {
        // 입력이 "paste"와 일치할 때 수행할 코드
    }
    if (strcmp(cmd, cut_cmd) == 0) {
        // 입력이 "cut"과 일치할 때 수행할 코드
    }
    return 0;  // 프로그램 종료
}

// 이 코드가 전처리 된다면 이 코드가 된다

/*
... content of stdio.h

... content of string.h
*/
// 전처리 되어서 코드 내용이 바뀐것을 확인 할 수 있다
int main() {
    char copy_cmd[256] = ""; strcpy(copy_cmd, "copy");
    char paste_cmd[256] = ""; strcpy(paste_cmd, "paste");
    char cut_cmd[256] = ""; strcpy(cut_cmd, "cut");
    char cmd[256];
    scanf("%s", cmd);
    if (strcmp(cmd, copy_cmd) == 0)
    {
        /* code */
    }
    if (strcmp(cmd, paste_cmd) == 0)
    {
        /* code */
    }
    if (strcmp(cmd, cut_cmd) == 0)
    {
        /* code */
    }
    return 0;
}

// 가변 인자 매크로에 대해 배워봅시다
// 가변 인자 매크로는 가변 인수를 받을 수 있습니다

/*
간단한 예제를 보겠습니다
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define VERSION "2.3.4"

#define LOG_ERROR(format, ...) \
fprintf(stderr, format, __VA_ARGS__)

int main() {
    
    if (args < 3) {
    LOG_ERROR("Invalid number of arguments for version %s\n.", VERSION);
    exit(1);
    }


    return 0;
}

// 루프를 모방한 가변 인자 매크로 사용하기

#include <stdio.h>

#define LOOP_3(X, ...) \
    printf("%s\n", #X);
#define LOOP_2(X, ...) \
    LOOP_3(__VA_ARGS__)
#define LOOP_1(X, ...) \
    LOOP_2(__VA_ARGS__)
#define LOOP(...) \
    LOOP_1(__VA_ARGS__)

int main() {
    LOOP(copy, paste cut)
    LOOP(copy, paste, cut)
    LOOP(copy, paste, cut, select)
    
    return 0;
}