# 📊 무역 데이터 분석 (2025-11-14)

< 김주연, 김종구, 박율영, 하예솔 >


## 최종 요약 및 인사이트 도출
# 데이터 분석에 근거한 가정들
0. 전체 무역량 추세: 22년1월 ~ 25년7월: 전체 trend는 감소
- 년도별
   <img width="1006" height="471" alt="image" src="https://github.com/user-attachments/assets/1ed90b2f-bc26-4239-aa99-81d4dab662d6" />
 <img width="844" height="538" alt="image" src="https://github.com/user-attachments/assets/3032be0b-0f22-49cc-83e9-b6fc53c02002" />

- 월별
<img width="1006" height="471" alt="image" src="https://github.com/user-attachments/assets/9a7d4627-4159-4ad5-9cca-0aa54cba5ef5" />
<img width="844" height="538" alt="image" src="https://github.com/user-attachments/assets/dcf1a1f4-69f7-43bd-9cdd-b707e39fe022" />
<img width="630" height="486" alt="image" src="https://github.com/user-attachments/assets/5ba81269-308d-4226-bef4-647654a81be7" />
<img width="1484" height="505" alt="image" src="https://github.com/user-attachments/assets/b85ea0bc-3405-43ac-86cd-a2ce137762ed" />



1. 무역량 상위 10개 품목
   - <img width="986" height="535" alt="image" src="https://github.com/user-attachments/assets/1f0cc1fb-5a84-4964-97f8-ac1a31f90f8f" />
---
2. 상관관계 히트맵
  - 품목 간 상관관계 히트맵 (트랜드 O)
<img width="1018" height="928" alt="image" src="https://github.com/user-attachments/assets/24a96e44-2918-4d27-8c92-d4320db3255d" />

  - hs4 간의 상관관계 트랜드 제거 x
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/7592706e-dc3e-49f0-b916-4b7f9d69d0d0" />

  -  hs4 간의 상관관계 트랜드 제거 o
<img width="1166" height="1010" alt="image" src="https://github.com/user-attachments/assets/2305d198-8e5c-42b2-9679-405abd322825" />
 ---
3. hs4 크롤링을 통한 hs4_name 확인
   <img width="490" height="154" alt="image" src="https://github.com/user-attachments/assets/29f947ea-fdd8-42fe-90bd-55c054835dc1" /> 
---
4. weight과 value간에 양의 상관관계가 존재한다. -> 상관관계 기울기에 따른 클러스터링 -> categorization Feature Eng. candidate
<img width="690" height="698" alt="image" src="https://github.com/user-attachments/assets/bda9a366-0492-4542-b768-22372bd570a4" />

---
5. weight 범주 내에 item들 간의 상관관계
  - 상관관계 조사 예시 : 기준 아이템 ID(ATLDMDBO), 상관관계 아이템 IDs('DNMPSKTB', 'QRKRBYJL', 'XUOIQPFL')
    <img width="981" height="350" alt="image" src="https://github.com/user-attachments/assets/2261dfb0-7f62-4c19-9d5b-144a6641ac6a" />
  - 상관관계 히트맵
   <img width="643" height="510" alt="image" src="https://github.com/user-attachments/assets/fadd83c5-7abe-4c3a-9364-251c8e920519" />

6. 주목할만한 상관관계 케이스 조사
   - 예시1: 관련이 없는 두 무역자재가 비슷한 시기에 무역량이 상승하는 경우
  <img width="1136" height="658" alt="image" src="https://github.com/user-attachments/assets/cccd426a-80b8-4a28-8557-abea714b026b" />
   - 예시2: 공행성쌍 상관관계가 클 것으로 추정되는 경우
     <img width="1136" height="658" alt="image" src="https://github.com/user-attachments/assets/ea838cae-f79f-48d3-883a-3900c2739341" />


8. hs4 간의 corr_mat (heatmap)에 튀는 조합들이 있다 (자기 자신을 제외하고도 corr>0.5)
    2.1. 전체 감소 trend에 상관관계
    2.2. 이전년도대비로 trend없앴을때 상관관계(주기성/계절성의 상관관계)
9. seq > 1인 무역품들이 인기상품(?)이다.
10. 같은 hs4에 속하는 item_id들중 제품들간에는 상관관계가 높은 조합이 있다(top1, top4, top5, top6, top10(weak), top11 hs4에 속한 아이텝. >0.4). 


# year : 전체 trend, 전체 데이터에서의 상관관계
# month : 이전 년도와 변화된량으로 상관관계(계절성/주기성)
# hs4 : 같은 범주(공통 중분류)에 속하는 제품간에 상관관계
# seq: 같은 범주(공통 구입횟수)에 속하는 제품간에 상관관계
# weight: categorization -> 같은 범주(weight-value기울기)에서의 상관관계 
