# import re

# # 코드가 들어 있는 파일 경로 설정
# input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
# common_variable_file = './CommonQuantity.cs'  # 탐색할 파일

# # 파일 읽기
# with open(input_file, 'r', encoding='utf-8') as file:
#     code = file.read()

# # 정규 표현식을 사용하여 .Set() 또는 .Turns() 내부의 값을 추출
# pattern = r'\.(?:Set|Turns)\((\w+)\)'  # e.g., .Set(eHazardLampReq_Active), .Turns(eHazardLampReq_Active)
# matches = re.findall(pattern, code)

# # 중복 제거 후 정렬
# unique_matches = sorted(set(matches))

# # 존재 여부를 확인할 결과를 저장할 딕셔너리
# value_exists_in_files = {val: False for val in unique_matches}

# # CommonQuantity.cs 파일에서 값이 존재하는지 확인
# with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
#     file_content = cs_file.read()
#     for val in unique_matches:
#         if val in file_content:
#             value_exists_in_files[val] = True

# # 결과 출력
# print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Quantity Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
# for val, exists in value_exists_in_files.items():
#     status = 'exists' if exists else 'does not exist'
#     print(f"{val}: {status}")





# import re
# import pandas as pd

# # 코드가 들어 있는 파일 경로 설정
# input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
# common_variable_file = './CommonQuantity.cs'  # 탐색할 파일
# excel_file = './Quantity_specmgmt.xlsx'  # 탐색할 엑셀 파일
# output_excel_file = './Quantity_Compare_Result.xlsx'  # 결과를 저장할 파일

# # 파일 읽기
# with open(input_file, 'r', encoding='utf-8') as file:
#     code = file.read()

# # 정규 표현식을 사용하여 .Set() 또는 .Turns() 내부의 값을 추출
# pattern = r'\.(?:Set|Turns)\((\w+)\)'  # e.g., .Set(eHazardLampReq_Active), .Turns(eHazardLampReq_Active)
# matches = re.findall(pattern, code)

# # 중복 제거 후 정렬
# unique_matches = sorted(set(matches))

# # 존재 여부를 확인할 결과를 저장할 딕셔너리
# value_exists_in_files = {val: False for val in unique_matches}

# # CommonQuantity.cs 파일에서 값이 존재하는지 확인
# with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
#     file_content = cs_file.read()
#     for val in unique_matches:
#         if val in file_content:
#             value_exists_in_files[val] = True

# # does not exist로 판별된 값들을 추려냄
# non_existent_quantities = [val for val, exists in value_exists_in_files.items() if not exists]

# # 엑셀 파일에서 값 탐색 (2번째 열에서만 탐색)
# df = pd.read_excel(excel_file, engine='openpyxl')  # 엑셀 파일을 읽어옴

# # 모든 값을 문자열로 변환하고 공백 제거
# df = df.applymap(lambda x: str(x).strip() if pd.notnull(x) else '')  # 모든 셀을 문자열로 변환 및 공백 제거

# # 2번째 열에서 non_existent_quantities에 해당하는 값을 찾음
# found_rows = df[df.iloc[:, 1].isin(non_existent_quantities)]  # 두 번째 열에서만 탐색

# # 결과를 새로운 엑셀 파일로 저장
# found_rows.to_excel(output_excel_file, index=False, engine='openpyxl')

# # 결과 출력
# print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Quantity Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
# for val, exists in value_exists_in_files.items():
#     status = 'exists' if exists else 'does not exist'
#     print(f"{val}: {status}")

# if not found_rows.empty:
#     print(f"\nMatching quantities found in the second column of Excel have been saved to '{output_excel_file}'.")
# else:
#     print(f"\nNo matching quantities were found in the second column of the Excel file.")






# 탐색 성공
import re
import pandas as pd

# 코드가 들어 있는 파일 경로 설정
input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
common_variable_file = './CommonQuantity.cs'  # 탐색할 파일
excel_file = './Quantity_specmgmt.xlsx'  # 탐색할 엑셀 파일
output_excel_file = './Quantity_Compare_Result.xlsx'  # 결과를 저장할 파일

# 파일 읽기
with open(input_file, 'r', encoding='utf-8') as file:
    code = file.read()

# 정규 표현식을 사용하여 .Set() 또는 .Turns() 내부의 값을 추출
pattern = r'\.(?:Set|Turns)\((\w+)\)'  # e.g., .Set(eHazardLampReq_Active), .Turns(eHazardLampReq_Active)
matches = re.findall(pattern, code)

# 중복 제거 후 정렬
unique_matches = sorted(set(matches))

# 존재 여부를 확인할 결과를 저장할 딕셔너리
value_exists_in_files = {val: False for val in unique_matches}

# CommonQuantity.cs 파일에서 값이 존재하는지 확인
with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
    file_content = cs_file.read()
    for val in unique_matches:
        if val in file_content:
            value_exists_in_files[val] = True

# does not exist로 판별된 값들을 추려냄
non_existent_quantities = [val for val, exists in value_exists_in_files.items() if not exists]

# "_" 뒷부분 제거하는 함수 정의
def remove_suffix(val):
    return val.split('_')[0]

# non_existent_quantities에서 "_" 뒷부분을 삭제
processed_quantities = [remove_suffix(val) for val in non_existent_quantities]

# 엑셀 파일에서 값 탐색 (엑셀 파일 전체에서 탐색)
df = pd.read_excel(excel_file, engine='openpyxl')  # 엑셀 파일을 읽어옴

# 부분 문자열 탐색 함수 정의
def partial_match(val, cell):
    # 엑셀의 셀 값을 문자열로 변환한 후 탐색
    return val in str(cell)

# 결과를 저장할 DataFrame 생성
found_rows = pd.DataFrame()

# processed_quantities의 각 값에 대해 엑셀 전체를 탐색
for val in processed_quantities:
    # 엑셀 파일의 모든 셀에서 부분 문자열 탐색
    match_mask = df.applymap(lambda cell: partial_match(val, cell))
    
    # 일치하는 값이 있는 행을 found_rows에 추가
    matching_rows = df[match_mask.any(axis=1)]  # 일치하는 셀이 있는 행 추출
    if not matching_rows.empty:
        found_rows = pd.concat([found_rows, matching_rows])

# 결과를 새로운 엑셀 파일로 저장
if not found_rows.empty:
    found_rows.to_excel(output_excel_file, index=False, engine='openpyxl')
    print(f"\nMatching quantities found in the Excel file have been saved to '{output_excel_file}'.")
else:
    print(f"\nNo matching quantities were found in the Excel file.")

# 결과 출력
print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Quantity Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
for val, exists in value_exists_in_files.items():
    status = 'exists' if exists else 'does not exist'
    print(f"{val}: {status}")







# # 부분이라도 일치하면 탐색
# import re
# import pandas as pd

# # 코드가 들어 있는 파일 경로 설정
# input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # 신호.Set(), 신호.Turns()를 확인할 파일
# common_variable_file = './CommonQuantity.cs'  # 탐색할 파일
# excel_file = './Quantity_specmgmt.xlsx'  # 탐색할 엑셀 파일
# output_excel_file = './Quantity_Compare_Result.xlsx'  # 결과를 저장할 파일

# # 파일 읽기
# with open(input_file, 'r', encoding='utf-8') as file:
#     code = file.read()

# # 정규 표현식을 사용하여 .Set() 또는 .Turns() 내부의 값을 추출
# pattern = r'\.(?:Set|Turns)\((\w+)\)'  # e.g., .Set(eHazardLampReq_Active), .Turns(eHazardLampReq_Active)
# matches = re.findall(pattern, code)

# # 중복 제거 후 정렬
# unique_matches = sorted(set(matches))

# # 존재 여부를 확인할 결과를 저장할 딕셔너리
# value_exists_in_files = {val: False for val in unique_matches}

# # CommonQuantity.cs 파일에서 값이 존재하는지 확인
# with open(common_variable_file, 'r', encoding='utf-8') as cs_file:
#     file_content = cs_file.read()
#     for val in unique_matches:
#         if val in file_content:
#             value_exists_in_files[val] = True

# # does not exist로 판별된 값들을 추려냄
# non_existent_quantities = [val for val, exists in value_exists_in_files.items() if not exists]

# # 엑셀 파일에서 값 탐색 (엑셀 파일 전체에서 탐색)
# df = pd.read_excel(excel_file, engine='openpyxl')  # 엑셀 파일을 읽어옴

# # 부분 문자열 탐색 함수 정의
# def partial_match(val, cell):
#     # 엑셀의 셀 값을 문자열로 변환한 후 탐색
#     return val in str(cell)

# # 결과를 저장할 DataFrame 생성
# found_rows = pd.DataFrame()

# # non_existent_quantities의 각 값에 대해 엑셀 전체를 탐색
# for val in non_existent_quantities:
#     # 엑셀 파일의 모든 셀에서 부분 문자열 탐색
#     match_mask = df.applymap(lambda cell: partial_match(val, cell))
    
#     # 일치하는 값이 있는 행을 found_rows에 추가
#     matching_rows = df[match_mask.any(axis=1)]  # 일치하는 셀이 있는 행 추출
#     if not matching_rows.empty:
#         found_rows = pd.concat([found_rows, matching_rows])

# # 결과를 새로운 엑셀 파일로 저장
# if not found_rows.empty:
#     found_rows.to_excel(output_excel_file, index=False, engine='openpyxl')
#     print(f"\nMatching quantities found in the Excel file have been saved to '{output_excel_file}'.")
# else:
#     print(f"\nNo matching quantities were found in the Excel file.")

# # 결과 출력
# print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Quantity Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
# for val, exists in value_exists_in_files.items():
#     status = 'exists' if exists else 'does not exist'
#     print(f"{val}: {status}")






# import pandas as pd

# # 엑셀 파일 경로 설정
# excel_file = './Quantity_specmgmt.xlsx'  # 탐색할 엑셀 파일


# # 엑셀 파일을 읽어옴
# df = pd.read_excel(excel_file, engine='openpyxl')  # 'openpyxl' 엔진을 사용하여 엑셀 파일 읽기

# # 모든 열의 이름 확인
# print("Column Names:", df.columns)

# # 데이터 타입 확인
# print("Data Types:\n", df.dtypes)


# # 랜덤으로 10개의 샘플 행 추출
# sample_rows = df.sample(n=10)  # n=10은 추출할 행의 개수

# # 샘플 행 출력
# print("Sample Rows from Excel:\n", sample_rows)






# 새로운 방식으로 다시 해봤으나 여전히 탐색 아무것도 안됨
# import re
# import pandas as pd

# # 파일 경로 설정
# input_file = './BDC_C_TurnSignalAndHazardLamp.cs'  # .Set(), .Turns()를 확인할 파일
# common_variable_file = './CommonQuantity.cs'  # 탐색할 파일
# excel_file = './Quantity_specmgmt.xlsx'  # 엑셀 파일
# output_excel_file = './Quantity_Compare_Result.xlsx'  # 결과 저장할 파일

# # 정규 표현식으로 .Set() 또는 .Turns() 내부 값을 추출하는 함수 (pure function)
# def extract_values_from_code(code):
#     pattern = r'\.(?:Set|Turns)\((\w+)\)'  # e.g., .Set(eHazardLampReq_Active)
#     return sorted(set(re.findall(pattern, code)))

# # 파일에서 값을 읽어들이는 함수 (pure function)
# def read_file(filepath):
#     with open(filepath, 'r', encoding='utf-8') as file:
#         return file.read()

# # 엑셀 파일을 읽고, 두 번째 열을 set으로 변환하는 함수 (pure function)
# def read_excel_column_to_set(filepath):
#     df = pd.read_excel(filepath, engine='openpyxl')  # 엑셀 파일 읽기
#     return set(df.iloc[:, 1].dropna().apply(lambda x: str(x).strip()))  # 2번째 열의 값을 set으로 변환

# # .cs 파일 내용 추출
# code_content = read_file(input_file)
# unique_matches = extract_values_from_code(code_content)

# # CommonQuantity.cs 파일에서 추출한 값과 비교
# common_quantity_content = read_file(common_variable_file)
# value_exists_in_files = {val: val in common_quantity_content for val in unique_matches}

# # 존재하지 않는 값들만 추려냄 (pure function)
# non_existent_quantities = list(filter(lambda val: not value_exists_in_files[val], unique_matches))

# # 엑셀 파일에서 두 번째 열을 set으로 변환
# excel_values_set = read_excel_column_to_set(excel_file)

# # non_existent_quantities와 엑셀 값의 교집합을 찾음 (pure function)
# found_quantities = set(non_existent_quantities) & excel_values_set

# # 교집합에 해당하는 값을 새로운 DataFrame으로 만들어 엑셀에 저장
# found_rows = pd.DataFrame(found_quantities, columns=['Matching Quantities'])
# found_rows.to_excel(output_excel_file, index=False, engine='openpyxl')

# # 결과 출력
# print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RESULT Quantity Search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
# for val, exists in value_exists_in_files.items():
#     status = 'exists' if exists else 'does not exist'
#     print(f"{val}: {status}")

# if found_quantities:
#     print(f"\nMatching quantities found in the second column of Excel have been saved to '{output_excel_file}'.")
# else:
#     print(f"\nNo matching quantities were found in the second column of the Excel file.")
