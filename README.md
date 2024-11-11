### HILS 검증/HILS TC 신호 및 속성 탐색 자동화 도구
 <br>
 HILS 검증 시 Common 파일에 존재하지 않는 신호 및 속성 명을 찾아 해당 Specmgmt 정보를 엑셀 파일로 생성해 주는 Python 자동화 도구를 개발하여 기존 사이클 3회를 0회로 절감, 90퍼센트 이상 시간 단축 효과. <br>
 <br>
 1. TC 내 Variable (또는 Quantity)을 전부 추출한다.
 2. CommonVariable.cs (또는 CommonQuantity) 내에 존재하는지 확인한다.
 3. 존재하지 않는다면 Specmgmt.xlsx 파일로 이동하여 해당 신호 및 속성의 정보를 확인한다.
 4. (Controller, Type, Values / Controller, System, Function, Signal, Values 등) 정보를 복사하여 엑셀 파일에 작성한다.
 5. 모든 Variable 및 Quantity에 대하여 1~4번 과정을 반복한다.
<br>
위 과정을 자동화하여 프로그램 실행 시 최종 결과물인 엑셀 파일이 생성되는 프로그램 개발하였음.
