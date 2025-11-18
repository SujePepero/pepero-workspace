from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# csv 읽기
df = pd.read_csv('train.csv')

# hs4_list = [3038, 2002, 2102, 2501, 2529, 2805, 2807, 2811, 2814, 2825, 2833,
#        2836, 2841, 2846, 2847, 2916, 3006, 3102, 3206, 3207, 3215, 3307,
#        3404, 3806, 3815, 3824, 3904, 3909, 4202, 4601, 4802, 5111, 5205,
#        5309, 5402, 5515, 5602, 5609, 5705, 6101, 6211, 7202, 7207, 8102,
#        8105, 8461, 8467, 8479, 8501, 8505, 8527, 8708, 8714, 9403, 1210,
#        3813, 4408, 4810, 5512, 2701, 7907, 2710, 6006, 5119, 9022, 4403,
#        3003, 2612, 4302, 7142, 3024]

# 중복 제거된 hs4 리스트 추출
hs4_list = df['hs4'].dropna().astype(int).unique().tolist()




driver = webdriver.Chrome()
driver.get("https://www.hs-tariff.com/main/hs_mti_ai_main/?device=pc")
time.sleep(3)


# 결과 저장용 딕셔너리
hs4_dict={}

for i in hs4_list:
    try:
        search_box = driver.find_element(By.ID, 'sh_name')
        
        # 기존 값 지우기
        search_box.clear()
        # 새 값 입력
        search_box.send_keys(str(i))
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)

        # 결과 대기
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".hs4_name"))
        )
        
        # 검색 결과에서 품목명 추출
        name_elem = driver.find_element(By.CSS_SELECTOR, ".hs4_name")
        hs4_name = name_elem.text.strip()

        hs4_dict[i] = hs4_name
        print(f"{i} → {hs4_name}")

        
    except Exception as e:
        print(f'검색 실패')
    
driver.quit()


# DataFrame에 병합
df['hs4_name'] = df['hs4'].map(hs4_dict)

# 새csv로 저장
df.to_csv('hs4_code.csv', index=False, encoding='utf-8-sig')

print('완료 : hs4_code.csv 생성됨')
