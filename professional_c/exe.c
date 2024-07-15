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
        printf("copy\n");
    }
    if (strcmp(cmd, paste_cmd) == 0) {
        printf("paste\n");
    }
    if (strcmp(cmd, cut_cmd) == 0) {
        printf("cut\n");
    }
    return 0;  // 프로그램 종료
}