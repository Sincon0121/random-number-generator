import random

def generate_random_numbers(min_value: int, max_value: int, count: int = 1):
    """
    메르센 트위스터 기반 정수 난수 생성기

    Parameters:
        min_value (int): 생성할 난수의 최소값
        max_value (int): 생성할 난수의 최대값
        count (int): 생성할 난수의 개수 (최대 10개)

    Returns:
        List[int]: 생성된 난수 리스트
    """
    if count < 1 or count > 10:
        raise ValueError("난수 개수는 1개 이상, 10개 이하로 설정해야 합니다.")
    if min_value > max_value:
        raise ValueError("최소값은 최대값보다 클 수 없습니다.")
    
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]
    return random_numbers


# 예시 사용
if __name__ == "__main__":
    min_val = int(input("난수 최소값을 입력하세요: "))
    max_val = int(input("난수 최대값을 입력하세요: "))
    count = int(input("몇 개의 난수를 생성하시겠습니까? (최대 10개): "))

    try:
        numbers = generate_random_numbers(min_val, max_val, count)
        print("생성된 난수:", numbers)
    except ValueError as e:
        print("오류:", e)