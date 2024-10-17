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
import pandas as pd

# 코드가 들어 있는 파일 경로 설정
input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
common_variable_file = './CommonVariable.cs'  # 탐색할 파일
excel_file = './Variable_specmgmt.xlsx'  # 탐색할 엑셀 파일
output_excel_file = './Variable_Compare_Result.xlsx'  # 결과를 저장할 파일

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
            

# does not exist로 판별된 값들을 추려냄
non_existent_variables = [val for val, exists in value_exists_in_files.items() if not exists]

# 엑셀 파일에서 값 탐색 (엑셀 파일 전체에서 탐색)
df = pd.read_excel(excel_file, engine='openpyxl')  # 엑셀 파일을 읽어옴

# 부분 문자열 탐색 함수 정의
def partial_match(val, cell):
    # 엑셀의 셀 값을 문자열로 변환한 후 탐색
    return val in str(cell)

# 결과를 저장할 DataFrame 생성
found_rows = pd.DataFrame()

# non_existent_variables의 각 값에 대해 엑셀 전체를 탐색
for val in non_existent_variables:
    # 엑셀 파일의 모든 셀에서 부분 문자열 탐색
    match_mask = df.applymap(lambda cell: partial_match(val, cell))
    
    # 일치하는 값이 있는 행을 found_rows에 추가
    matching_rows = df[match_mask.any(axis=1)]  # 일치하는 셀이 있는 행 추출
    if not matching_rows.empty:
        found_rows = pd.concat([found_rows, matching_rows])

# # 중복된 행 제거
# found_rows = found_rows.drop_duplicates()

# 결과를 새로운 엑셀 파일로 저장
if not found_rows.empty:
    found_rows.to_excel(output_excel_file, index=False, engine='openpyxl')
    print(f"\nMatching variables found in the Excel file have been saved to '{output_excel_file}'.")
else:
    print(f"\nNo matching variables were found in the Excel file.")

# 결과 출력
print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Variable Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
for val, exists in value_exists_in_files.items():
    status = 'exists' if exists else 'does not exist'
    print(f"{val}: {status}")