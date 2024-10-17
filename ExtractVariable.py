# import re

# # 코드가 들어 있는 파일 경로 설정
# input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
# common_variable_file = './CommonVariable.cs'  # 탐색할 파일

# # 파일 읽기
# with open(input_file, 'r', encoding='utf-8') as file:
#     code = file.read()

# # 정규 표현식을 사용하여 .Set() 또는 .Turns() 앞의 값을 추출
# # e.g., sADASHDPHazardLampReq.Set(eHazardLampReq_Active), sTurnLampMode.Turns(eHazardLampReq_Active)
# pattern = r'(\w+)\.(?:Set|Turns)\('  # .Set 또는 .Turns 앞에 있는 변수명을 추출
# matches = re.findall(pattern, code)

# # 중복 제거 후 정렬
# unique_matches = sorted(set(matches))

# # 존재 여부를 확인할 결과를 저장할 딕셔너리
# value_exists_in_files = {val: False for val in unique_matches}

# # CommonVariable.cs 파일에서 값이 존재하는지 확인
# with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
#     file_content = cs_file.read()
#     for val in unique_matches:
#         if val in file_content:
#             value_exists_in_files[val] = True

# # 결과 출력
# print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Variable Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
# for val, exists in value_exists_in_files.items():
#     status = 'exists' if exists else 'does not exist'
#     print(f"{val}: {status}")




# 주석 처리된 신호 제외하고 추출

import re

# 코드가 들어 있는 파일 경로 설정
input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
common_variable_file = './CommonVariable.cs'  # 탐색할 파일

# 주석을 제거하는 함수
def remove_comments(code):
    # 여러 줄 주석 제거 (/* ... */)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # 한 줄 주석 제거 (// ...)
    code = re.sub(r'//.*', '', code)
    return code

# 파일 읽기
with open(input_file, 'r', encoding='utf-8') as file:
    code = file.read()

# 주석 제거
code_no_comments = remove_comments(code)

# 정규 표현식을 사용하여 .Set() 또는 .Turns() 앞의 값을 추출
# e.g., sADASHDPHazardLampReq.Set(eHazardLampReq_Active), sTurnLampMode.Turns(eHazardLampReq_Active)
pattern = r'(\w+)\.(?:Set|Turns)\('  # .Set 또는 .Turns 앞에 있는 변수명을 추출
matches = re.findall(pattern, code_no_comments)

# 중복 제거 후 정렬
unique_matches = sorted(set(matches))

# 존재 여부를 확인할 결과를 저장할 딕셔너리
value_exists_in_files = {val: False for val in unique_matches}

# CommonVariable.cs 파일에서 값이 존재하는지 확인
with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
    file_content = cs_file.read()
    for val in unique_matches:
        if val in file_content:
            value_exists_in_files[val] = True

# 결과 출력
print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Variable Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
for val, exists in value_exists_in_files.items():
    status = 'exists' if exists else 'does not exist'
    print(f"{val}: {status}")
