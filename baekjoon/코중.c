#include <stdio.h>

int findMax(int N, int M, int boxes[]) {
    int prefix_sum[N + 1];
    prefix_sum[0] = 0;

    // 누적 합 계산
    for (int i = 1; i <= N; i++) {
        prefix_sum[i] = prefix_sum[i - 1] + boxes[i - 1];
    }

    int max_sum = 0;

    // 가장 큰 구간의 합 계산
    for (int i = 0; i <= N - M; i++) {
        int current_sum = prefix_sum[i + M] - prefix_sum[i];
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
    }
    return max_sum;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int boxes[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &boxes[i]);
    }

    int result = findMax(N, M, boxes);
    printf("%d\n", result);

    return 0;
}