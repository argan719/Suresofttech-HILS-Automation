### HILS 검증/HILS TC 신호 및 속성 탐색 자동화 도구
 <br>
 HILS 검증 시 Common 파일에 존재하지 않는 신호 및 속성 명을 찾아,<br> 해당 Specmgmt 정보를 엑셀 파일로 생성해 주는 Python 자동화 도구를 개발하여<br>기존 사이클 3회를 0회로 절감, 90퍼센트 이상 시간 단축 효과. <br>
 <br>
 1. TestCase 내 Variable (또는 Quantity)을 전부 추출한다. <br>
 2. CommonVariable.cs (또는 CommonQuantity) 내에 해당 신호 및 속성이 존재하는지 확인한다. <br>
 3. 존재하지 않는다면 Specmgmt.xlsx 파일로 이동하여 정보를 확인한다. <br> 
 4. (Controller, Type, Values / Controller, System, Function, Signal, Values 등) 정보를 복사하여 엑셀 파일에 작성한다. <br>
 5. 모든 Variable 및 Quantity에 대하여 1~4번 과정을 반복한다. <br>
<br>
위 과정을 자동화하여 프로그램 실행 시 최종 결과물인 엑셀 파일이 생성되는 프로그램 개발하였음.
<br>
<br> <br>
HILS 검증 진행 시 CommonVariable.cs, CommonQuantity.cs 파일에 TestCase에 사용되는 모든 신호, 속성값이 선언되어 있어야만 HILS 장비에서 검증이 가능함. <br>
작업자(고객사)가 검증을 진행하며 일일이 채워넣는 방식이다 보니 슈어에서 검증 시 선언되어 있지 않은 신호, 속성이 대부분이라 전부 취합해 검증자에게 정보를 전달해야 검증이 가능했음. 
