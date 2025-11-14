# 📊 무역 데이터 분석 (2025-11-14)

< 김주연, 김종구, 박율영, 하예솔 >


## 최종 요약 및 인사이트 도출

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
   - <img width="986" height="535" alt="image" src="https://github.com/user-attachments/assets/1f0cc1fb-5a84-4964-97f8-ac1a31f90f8f" />
---
**2. 상관관계 히트맵**
  - 품목 간 상관관계 히트맵 (트랜드 O)
<img width="1018" height="928" alt="image" src="https://github.com/user-attachments/assets/24a96e44-2918-4d27-8c92-d4320db3255d" />

  - hs4 간의 상관관계 트랜드 제거 x
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/7592706e-dc3e-49f0-b916-4b7f9d69d0d0" />

  -  hs4 간의 상관관계 트랜드 제거 o
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/2305d198-8e5c-42b2-9679-405abd322825" />
       - 0.7 <= corr < 0.99로 필터링한 상관관계 변수 예시
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
    
       - 예시:   기준 item ID- 'ATLDMDBO' 높은 상관계를 갖는 item IDs - 'BTMOEMEP', 'DNMPSKTB', 'LRVGFDFM', 'QRKRBYJL', 'QVLMOEYE', 'VBYCLTYZ', 'XUOIQPFL' 7개 항목
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

