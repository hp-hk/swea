import sys
import os
# import fire
from helpers import generate_files

def main():
    # (1) 명령어 핸들링
    option = sys.argv[-1]
    valid_options = ['d1', 'd2', 'd3', 'd4']
    
    if option in valid_options:
        print(f'{option} 문제를 생성합니다.')
        generate_files(option)
    else:
        print('d1과 같이 생성할 난이도 단계를 입력해주세요.')
    
if __name__ == '__main__':
    main()