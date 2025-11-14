# 📊 무역 데이터 분석 (2025-11-14)

< 김주연, 김종구, 박율영, 하예솔 >


## 🚀 최종 요약 및 인사이트 도출
 
1. 거시적 무역 패턴 (Macro-Level Trends)
데이터의 전체적인 흐름과 계절성을 파악했습니다.<br>
• 전체 추세: 2022년부터 2025년까지 연도별 전체 무역량(value)은 감소하는 추세를 보였습니다.<br>
• 월별 계절성: 월별 무역량(value)은 1월에 가장 높게 나타났으며, 무역 횟수(Count)는 연초(1월)와 연말(12월)에 집중되는 경향을 확인했습니다.

3. '가짜 상관관계' 식별 및 트렌드 제거
시계열 데이터의 함정을 피하고 '진짜' 관계를 식별하는 것이 중요했습니다.<br>
• 문제점: 트렌드를 제거하지 않은 원본 데이터로 상관관계를 분석한 결과, 대부분의 변수가 '가짜 상관관계(Spurious Correlation)'로 인해 높게 나타났습니다.<br>
• 해결책: '전년 대비 성장률'로 데이터를 변환하여 시계열 트렌드를 제거하자, 무분별했던 상관관계가 정리되었고 '진짜' 관계를 식별할 기반이 마련되었습니다.<br>
• 필요성: 전체 상관관계 Pair 중, 소수의 유의미하게 높은 상관관계를 갖는 Pair를 필터링하는 전략이 필요함을 확인했습니다.

4. 주요 변수(Feature) 특성 및 클러스터링
데이터의 분포와 개별 변수 간의 관계를 파악했습니다.<br>
• Value-Weight 관계: value와 weight 간의 관계는 단일 정규분포가 아닌, 4개의 뚜렷한 클러스터로 구분되었습니다. 각 클러스터는 내부적으로 선형적인 상관관계를 보였습니다.<br>
• 아이템 범주화: 무역 거래 횟수를 기준으로 아이템을 '핵심/주기성/비주기성' 등으로 범주화할 수 있었으며, 이는 그룹별 특화 분석의 가능성을 시사합니다.<br>
• 품목명(Domain) 활용: hs4 코드를 실제 분류명과 매핑하여, 통계적으로 유의미한 관계가 '원자재-완제품'과 같은 실제 산업적 연관성에 기인하는지 검증할 수 있었습니다.<br>

6. 공행성(Co-movement) 및 시차(Lag) 관계 분석
• '허브' 품목의 존재: 공행성 쌍의 분포는 '기준 아이템' 대비 '공행성 아이템'의 개수가 우하향(롱테일)하는 패턴을 보였습니다. 이는 소수의 '핵심 품목'이 다수의 품목과 관계를 맺고 있음을 의미합니다.<br>
• '선행/후행' 관계의 다양성: '최적 시차(best lag)'는 특정 값에 쏠리지 않고 균등하게 분포되어, 품목 간에 다양한 '선행/후행' 관계가 존재함을 확인했습니다. (예: 1달 선행, 4달 선행 등)<br>
• 관계의 희소성: 공행성 쌍 간의 상관관계 분포 역시 우하향하며, 대부분의 관계는 약하고 소수의 '강력한 관계'가 존재함을 재확인했습니다.

---


**0. 전체 무역량 추세: 22년1월 ~ 25년7월: 전체 trend는 감소**
- 년도별
   <img width="1006" height="471" alt="image" src="https://github.com/user-attachments/assets/1ed90b2f-bc26-4239-aa99-81d4dab662d6" />
 <img width="844" height="538" alt="image" src="https://github.com/user-attachments/assets/3032be0b-0f22-49cc-83e9-b6fc53c02002" />

- 월별
<img width="1006" height="471" alt="image" src="https://github.com/user-attachments/assets/9a7d4627-4159-4ad5-9cca-0aa54cba5ef5" />
<img width="844" height="538" alt="image" src="https://github.com/user-attachments/assets/dcf1a1f4-69f7-43bd-9cdd-b707e39fe022" />
<img width="630" height="486" alt="image" src="https://github.com/user-attachments/assets/5ba81269-308d-4226-bef4-647654a81be7" />
<img width="1484" height="505" alt="image" src="https://github.com/user-attachments/assets/b85ea0bc-3405-43ac-86cd-a2ce137762ed" />



**1. 무역량 상위 10개 품목**
<img width="986" height="535" alt="image" src="https://github.com/user-attachments/assets/1f0cc1fb-5a84-4964-97f8-ac1a31f90f8f" />

---

**2. 상관관계 히트맵**
  - 품목 간 상관관계 히트맵 (트랜드 O)
<img width="1018" height="928" alt="image" src="https://github.com/user-attachments/assets/24a96e44-2918-4d27-8c92-d4320db3255d" />

  - hs4 간의 상관관계 트랜드 제거 x
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/7592706e-dc3e-49f0-b916-4b7f9d69d0d0" />

  -  hs4 간의 상관관계 트랜드 제거 o
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/2305d198-8e5c-42b2-9679-405abd322825" />
       -> 0.7 <= corr < 0.99로 필터링한 상관관계 변수 예시
     <img width="1136" height="658" alt="image" src="https://github.com/user-attachments/assets/9344bae6-1c84-4ccc-ae1d-20bd33234655" />
     <img width="1044" height="936" alt="image" src="https://github.com/user-attachments/assets/9b74616c-aa28-495b-a278-e92a95be9293" />

 ---
 
**3. hs4 크롤링을 통한 hs4_name 확인**

   <img width="490" height="154" alt="image" src="https://github.com/user-attachments/assets/29f947ea-fdd8-42fe-90bd-55c054835dc1" /> 

---

**4. weight과 value간에 양의 상관관계 및 클러스터링(Feature Engineering)**

<img width="690" height="698" alt="image" src="https://github.com/user-attachments/assets/bda9a366-0492-4542-b768-22372bd570a4" />


- 각 클러스터 별 weight, value 상관관계

  <img width="1192" height="284" alt="image" src="https://github.com/user-attachments/assets/88b1b205-d8ae-474a-84ac-20ab4111f759" />

---

**5. weight 범주 내에 item들 간의 상관관계**
  - 상관관계 조사 예시 : 기준 아이템 ID(ATLDMDBO), 상관관계 아이템 IDs('DNMPSKTB', 'QRKRBYJL', 'XUOIQPFL')
    <img width="981" height="350" alt="image" src="https://github.com/user-attachments/assets/2261dfb0-7f62-4c19-9d5b-144a6641ac6a" />
    <br>
  - 상관관계 히트맵
   <img width="643" height="510" alt="image" src="https://github.com/user-attachments/assets/fadd83c5-7abe-4c3a-9364-251c8e920519" />

---

**6. 주목할만한 상관관계 케이스 조사**

 - 예시1: 관련이 없는 두 무역자재가 비슷한 시기에 무역량이 상승하는 경우
  <img width="1136" height="658" alt="image" src="https://github.com/user-attachments/assets/cccd426a-80b8-4a28-8557-abea714b026b" />
  
  - 예시2: 공행성쌍 상관관계가 클 것으로 추정되는 경우
     <img width="1136" height="658" alt="image" src="https://github.com/user-attachments/assets/ea838cae-f79f-48d3-883a-3900c2739341" />
     
---

**7. hs4 와 item_id간의 관계(71개 hs4 코드와 100개 아이템간의 1:n 관계) 및 같은 hs4코드내 아이템들간의 상관관계**
   - 예시: hs4 = 8505 에 item_id= 'GYHKIVQT' 'ROACSLMG' 'VBYCLTYZ' 3개 아이템 포함 
   <img width="981" height="350" alt="image" src="https://github.com/user-attachments/assets/2a168755-e308-4e29-9a64-460010b70d29" />
   <img width="654" height="528" alt="image" src="https://github.com/user-attachments/assets/8f3e271a-622e-4669-82a5-2a63a7bad582" />

---

**8. 무역 거래 회수(seq)에 따른 아이템들 범주화 (seq-cat)**

 - 40, 80을 기준으로 3 범주로 나눔: (seq_cnt_low,  seq_cnt_mid,  seq_cnt_high)
 <img width="560" height="452" alt="image" src="https://github.com/user-attachments/assets/8ec90157-6c3a-46ed-a2f2-58ae116a752d" />
 
  - 각 범주에 포함되는 아이템들간의 상관관계
    - 예시: 기준 item ID- 'ATLDMDBO' 높은 상관계를 갖는 item IDs - 'BTMOEMEP', 'DNMPSKTB', 'LRVGFDFM', 'QRKRBYJL', 'QVLMOEYE', 'VBYCLTYZ', 'XUOIQPFL' 7개 항목
   <img width="981" height="350" alt="image" src="https://github.com/user-attachments/assets/384411f6-8b1a-4eb8-afa2-6b398540934d" />
   <img width="711" height="577" alt="image" src="https://github.com/user-attachments/assets/f8532c14-ef69-4f88-affd-739607275598" />

---

**9. 공행성쌍 데이터 변수 분포**
 - 한 item에 대한 following_item 갯수 분포 히스토그램:
<img width="560" height="452" alt="image" src="https://github.com/user-attachments/assets/2083bef3-0f19-4347-883e-875c98ddcfbf" />

 - "best_lag 분포 히스토그램"
<img width="568" height="452" alt="image" src="https://github.com/user-attachments/assets/84c3cac6-8160-4d41-9c53-7ff33b58068a" />

 - max_corr 분포 히스토그램
<img width="577" height="451" alt="image" src="https://github.com/user-attachments/assets/ac895eac-2627-49ed-867e-5923e282c279" />

