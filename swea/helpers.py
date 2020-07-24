import os
import csv
import sys
import json
import shutil
import requests
from pathlib import Path

def get_file_contents(number, title, level):
    file_contents = f'''"""
    {number}: {title} [{level}]
    """

    import sys
    sys.stdin = open('{number}_input'.txt)

    '''
    return file_contents

def generate_files(level):
    user_path = os.getcwd()
    # print(user_path)

    script_path = os.path.dirname(os.path.realpath(__file__))
    # print(script_path)

    # Get root path without pathlib
    # parent_path = os.path.abspath(os.path.join(script_path, os.pardir, os.pardir))
    # abs_path_list = script_path.split(os.sep)
    # package_root_path = os.path.join(*abs_path_list[1:-2])

    root_path = Path(script_path).parent

    data_path = os.path.join(root_path, 'data')

    problems = []
    with open(os.path.join(data_path, f'{level}.json'), 'r') as json_data:
        print(json_data)
        dict_data = json.loads(json_data.read())
    for data in dict_data:
        problems.append(data)

    # 함수가 불려진 경로 확인
    # print(problems)
    os.chdir(user_path)
    # print(user_path)
        
    try:
        os.makedirs(level)
    except FileExistsError:
        print(f'{level} 이름의 폴더가 이미 존재합니다.')
        user_input = input('기존 폴더를 삭제하고 계속 진행하시겠습니까? (y/n) ')
        while (not (user_input == 'y' or user_input == 'n')):
            print('y 또는 n을 입력하셔야 합니다.')
            user_input = input('기존 폴더를 삭제하고 계속 진행하시겠습니까? (y/n) ')
        if user_input == 'y':
            shutil.rmtree(level)
            os.makedirs(level)
        elif user_input == 'n':
            sys.exit(1) 

    # 폴더 이동
    # print(os.getcwd())
    os.chdir('d1')
    # print(os.getcwd())

    # for problem in problems:
    #     with open(f'{problem}.py', 'w') as f:
    #         f.write(get_file_contents(problem['number'], problem['title'], problem['level']))
    
    for idx, problem in enumerate(problems):
        input_url = f'https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=in&contestProbId={problem["id"]}&_menuId=AVtnUz06AA3w6KZN&_menuF=true'
        output_url = f'https://swexpertacademy.com/main/common/contestProb/contestProbDown.do?downType=out&contestProbId={problem["id"]}&_menuId=AVtnUz06AA3w6KZN&_menuF=true'

        cnt = '0' + str(idx) if idx < 10 else str(idx)
        with open(f'{cnt}_{problem["number"]}_input.txt', 'w') as f:
            f.write(requests.get(input_url).text)
        with open(f'{cnt}_{problem["number"]}_out.txt', 'w') as f:
            f.write(requests.get(output_url).text)
        with open(f'{cnt}_{problem["number"]}.py', 'w') as f:
            f.write(get_file_contents(problem['number'], problem['title'], problem['level']))