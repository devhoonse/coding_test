# import : built-ins


def count_times_including_digit(n, digit=3):
    """
    [유형 : 완전탐색 (Brute Forcing)]
    0 시  0 분  0 초 부터
    N 시 59 분 59 초 까지 ( N + 1 시 직전까지만 볼 것 )
    시간들 중에서 다음 예시와 같이 3 이 하나라도 포함된 시각의 개수를 반환합니다.
    (ex)
    0 시  0 분  0 초 부터
    1 시 59 분 59 초 까지
        - 0 시  0 분  3 초
        - 0 시 13 분 11 초
        - 0 시 32 분 53 초
        ...

    >>> count_times_including_digit(5)
    11475

    :param n: 몇 시 (N) 까지의 시간 범위를 볼 것인지
    :type n: int
    :param digit: 포함되어야 하는 숫자
    :type digit: int
    :return: 주어진 시간 범위 내에서 숫자 digit 이 포함된 시각의 갯수
    :rtype: int
    """

    # 정답 값을 구합니다.
    count = 0
    sec = 0
    while sec < (n + 1) * (60 ** 2):     # n + 1 시 직전까지만 볼 것.
        hours = sec // (60 ** 2)
        minutes = (sec % (60 ** 2)) // (60 ** 1)
        seconds = (sec % (60 ** 2)) % (60 ** 1)
        count += f'{"%02d" % hours}:{"%02d" % minutes}:{"%02d" % seconds}'.__contains__(str(digit))
        sec += 1

    # 정답 값을 반환합니다.
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
