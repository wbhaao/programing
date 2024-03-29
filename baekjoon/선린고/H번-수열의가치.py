'''
H번 - 수열의 가치 스페셜 저지
시간 제한	메모리 제한
2 초 (추가 시간 없음)	1024 MB (추가 메모리 없음)
문제
어떤 정수 수열 
$X$의 가치는 다음과 같이 정의된다:

 
$X$에서 감소하지 않는 부분 수열 
$P$와 증가하지 않는 부분 수열 
$Q$를 임의로 선택했을 때, (
$P$의 모든 원소의 합) + (
$Q$의 모든 원소의 합)의 최댓값
길이가 
$N$인 정수 수열 
$A$가 주어진다. 
$A$를 원하는 대로 재배열하여 수열의 가치를 최대화하고 싶다. 재배열하여 만들 수 있는 수열의 가치의 최댓값과 이 때의 수열을 찾아보자.

감소/증가하지 않는 부분 수열이 무엇인지 잘 모르는 친구들은 친절한 정휘가 준비한 아래 정의를 읽어보도록 하자.

부분 수열이란 주어진 수열에서 1개 이상의 원소를 골라 원래 순서대로 나열하여 얻은 수열을 말한다.
감소하지 않는 부분 수열은 맨 처음 원소를 제외한 모든 원소가 바로 이전 원소보다 크거나 같은 부분 수열을 말한다.
증가하지 않는 부분 수열은 맨 처음 원소를 제외한 모든 원소가 바로 이전 원소보다 작거나 같은 부분 수열을 말한다.
어떤 수가 두 부분 수열 
$P$와 
$Q$ 모두에 포함되도록 
$P$와 
$Q$를 선택할 수 있으며, 둘 모두에 포함된 수는 
$P$의 원소의 합을 구할 때와 
$Q$의 원소의 합을 구할 때 모두 더해진다.

입력
첫째 줄에 
$N$이 주어진다. 
$(1 \le N \le 1\,000)$ 

둘째 줄에 정수 
$A_1, A_2, \cdots, A_N$이 공백으로 구분되어 주어진다. 
$(1 \le A_i \le N)$ 

출력
 
$A$를 재배열하여 만들 수 있는 수열의 가치의 최댓값을 첫 번째 줄에 출력한다.

그 때의 수열 
$B_1, B_2, \cdots, B_N$을 두 번째 줄에 공백으로 구분하여 출력한다. 가능한 수열이 여러 가지라면 그 중 아무거나 출력한다.

예제 입력 1 
4
2 3 1 2
예제 출력 1 
12
1 3 2 2
'''