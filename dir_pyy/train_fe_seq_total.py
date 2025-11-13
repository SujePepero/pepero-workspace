##### 상관계수 종류
# a) 피어슨 상관계수 (Pearson correlation coefficient)
#	- 두 변수가 연속형이고, 직선적인(선형) 관계일 때	
#   - 평균과 표준편차를 이용해 계산. 
#   - 정규분포 가정이 있을 때 가장 일반적.
# b) 스피어만 상관계수 (Spearman rank correlation)	
#   - 두 변수가 **순서형(서열형)**이거나, 비선형이지만 단조(monotonic) 관계일 때	실제 
#   - 값 대신 순위를 이용해 계산. 
#   - 극단값(outlier)에 덜 민감.
# c) 켄달의 타우 (Kendall’s tau)	
#   - 표본이 작거나, 순서 정보만 중요할 때	
#   - 데이터 쌍 간의 “일치/불일치” 비율로 계산. 
#   - 순서형 변수에 매우 적합.
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
# 무역 품목 간 공행성(comovement)은 두 개 이상의 무역 품목이 일정 기간 동안 가격, 거래량, 또는 기타 경제적 지표에서 비슷한 방향으로 움직이는 경향을 의미합니다. 즉, 한 품목의 수출입량이나 가격이 오르면 다른 품목의 수출입량이나 가격도 함께 오르는 경향이 있을 때, 두 품목은 **공행성(comovement)**을 가진다고 합니다. 반대로 한 품목이 가격이 오르거나 수출입량이 증가할 때, 다른 품목은 반대로 움직인다면 **역행성(negative comovement)**이 있다고 말할 수 있습니다.
# 공행성을 분석할 때는 주로 상관관계 분석이나 공분산 분석을 사용합니다. 특히 상관계수(Pearson's Correlation Coefficient)를 사용해 두 품목의 수출입량 변화가 얼마나 비례하는지를 측정합니다. 상관계수가 1에 가까우면 두 품목은 강한 공행성을 가진다고 할 수 있고, -1에 가까우면 강한 역행성을 가진다고 할 수 있습니다.
# 상관계수가 높은 품목끼리는 가격 변동성이나 수출입량 변동성이 비슷하다는 것을 의미하므로, 특정 품목의 변동을 기반으로 다른 품목을 예측할 수 있습니다.
#//////////////
# 무역 품목 간 예측 (Cross-commodity Trade Predictions)
# 두 무역 품목 간 공행성을 분석하여, 한 품목의 수출입량 변화를 기반으로 다른 품목의 수출입량을 예측할 수도 있습니다. 예를 들어, 전자기기와 반도체 품목 간에 강한 공행성이 있을 경우, 반도체 수출량을 예측하고, 이를 바탕으로 전자기기의 수출량을 예측할 수 있습니다.
# 연구 사례: 반도체와 컴퓨터 기기의 수출입량 간의 상관관계를 분석하여, 반도체 수출량을 예측하고 이를 기반으로 컴퓨터 기기의 수출량을 예측하는 방법을 사용한 연구도 있습니다.

#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
seq_pivot_df_cnt = pd.pivot_table(train, index='item_id', columns="month", values='seq',aggfunc='count', margins=True, margins_name="seq_total")

tmp_ser = seq_pivot_df_cnt['seq_total'].iloc[:-1]
dct_seq_total = pd.cut(tmp_ser, bins= [0, 40, 80, tmp_ser.max()], labels = ['seq_cnt_low',  'seq_cnt_mid',  'seq_cnt_high'] ).to_dict()
dct_seq_total

train_fe = train.copy()
train_fe['seq_cat'] = train_fe["item_id"].map(dct_seq_total)
train_fe

tmp_df_seq = train_fe.groupby(["seq_cat"], as_index=False)["item_id"].apply(lambda x: np.unique(x))
tmp_df_seq['seq_cat_len'] = train_fe.groupby(["seq_cat"])["item_id"].apply(lambda x: len(np.unique(x))).values#['item_id']#.sort_values(by='item_id', ascending=False, key = lambda x: len(x), axis=1)#.reset_index(drop=True)['item_id']
tmp_df_seq

dct_seq_cat = tmp_df_seq[['seq_cat','item_id']].set_index('seq_cat').to_dict()['item_id']
dct_seq_cat

topN_seq_cat = tmp_df_seq['seq_cat'].values
topN_seq_cat

#//////////////////////////////////////////////////////////////
# (최대값 - 최소값) / bins
# plt.hist(scores, bins =10) # bins = 10, 기본값
count, bins, container = plt.hist(seq_pivot_df_cnt['seq_total'].iloc[:-1], bins=20, edgecolor='k', rwidth=.9) # 
print('count :', count) # count : [    1.   2.   1.     3.   3.     3.   2.     5.]
print('bins :', bins)   # bins :  [60. 64.25 68.5  72.75 77.   81.25 85.5  89.75 94.  ]
print('container :', container) # container : <BarContainer object of 8 artists>


for i in range(len(bins)-1):
    print(f'{bins[i]} ~ {bins[i+1]} : {int(count[i])}개')

plt.xlabel('Scores')
plt.ylabel('Count')

plt.title("seq_total(동일 연/월 일련번호 seq 의 총합)")
plt.show()



#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
###
### sel_topN_seq_cat = 2 경우
### 

sel_topN_seq_cat = 2
print(f'top{sel_topN_seq_cat}_seq_cat={topN_seq_cat[sel_topN_seq_cat-1]}, {len(dct_seq_cat[topN_seq_cat[sel_topN_seq_cat-1]])}개 아이템, {dct_seq_cat[topN_seq_cat[sel_topN_seq_cat-1]]}') # top1_hs4 : ['BSRMSVTC' 'DJBLNPNC' 'RCBZUSIM' 'SUOYXCHP' 'WQMVCOEM' 'ZKENOUDA']

df_hm_plot = pd.DataFrame()
j= 0
fig = plt.figure(figsize=(12,4))
for i, group in enumerate(monthly.groupby("item_id")[['item_id','ym', 'value']]):
    if group[0] in dct_seq_cat[topN_seq_cat[sel_topN_seq_cat-1]]:
        j += 1
        #print(f'i = {i}, group name: {group[0]}, df_group: {group[1].head(1)}')
        print(f'index = {i+1}, {j}th item, item name: {group[0]}')

        df_hm_plot = pd.concat([df_hm_plot, group[1]], axis=0)

        ax = plt.gca()
        # 상품별 월별 무역량(월 최대 3회 교역)
        #ax.plot(group[1]["ym"], group[1]["value"], label=f'pid={group[0]}', marker='d')
        #ax.plot(group[1]["ym"], group[1]["value"]/group[1]["value"].max(), label=f'pid={group[0]}', marker='d')
        ax.plot(group[1]["ym"], (group[1]["value"]- group[1]["value"].min())/(group[1]["value"].max()- group[1]["value"].min()), label=f'pid={group[0]}', marker='d')

        ax.set_xlim([monthly['ym'].min(), monthly['ym'].max()])
        ax.legend()
        ax.grid()
        
        #if i==5: break
    
#display(df_hm_plot)
fig_sns = plt.figure(figsize=(8,6))
corr_mat= pd.pivot_table(df_hm_plot, index='ym', columns='item_id', values='value', fill_value=0).corr()
sns.heatmap(corr_mat, annot=True, fmt=".2f",vmin=-1, vmax=1, cbar_kws={'ticks': [-1, -0.5, 0, 0.5, 1]}, center=0 )




#///////////////////////////////////////////////////////////////
high_corr = []
for i, row in enumerate(corr_mat[(corr_mat.abs() > 0.6) & corr_mat[(corr_mat.abs() < 0.99)]].iterrows()):
    if row[1].any():
        print(( row[1][row[1].notna()].name, row[1][row[1].notna()].index.to_list()))
        high_corr.append((row[1][row[1].notna()].name, row[1][row[1].notna()].index.to_list()))

#///////////////////////////////////////////////////////////////
dict_hight_corr = dict(high_corr)
dict_hight_corr


#///////////////////////////////////////////////////////////////
mod_dict_hight_cor = {}
# tmp_dict = {}

for i, (k, v) in enumerate(dict_hight_corr.items()):
    print(f'index = {i+1}, item, item name: {k} : {v}')
    
    fig = plt.figure(figsize=(12,4))
    df_hm_plot = pivot.loc[k].to_frame(name=k)
    ax = plt.gca()
    # 상품별 월별 무역량(월 최대 3회 교역)
    # ax.plot((pivot.loc[k] - pivot.loc[k].min()) / (pivot.loc[k].max()- pivot.loc[k].min()), label=f'key: {k}', marker='s')
    #key_name1 = f'{k}\n{hs4_name_dict.get(str(k))}'
    key_name1 = f'{k}'     

    lbl_hmap = []
    lbl_hmap.append(key_name1)
    
    ax.plot((pivot.loc[k] - pivot.loc[k].min()) / (pivot.loc[k].max()- pivot.loc[k].min()), label=key_name1)
    
    df_hm_plot = pd.concat([df_hm_plot, pivot.loc[k]], axis=0)
    #df_hm_plot[f'{k}'] = pivot_monthly[k].values
    #display(df_hm_plot.reset_index())
    
    for j, item in enumerate(v):
        #key_name2 = f'{item}\n{hs4_name_dict.get(str(item))}'
        key_name2 = f'{item}'
        lbl_hmap.append(key_name2)
        
        #ax.plot(pivot.loc[item]/pivot.loc[item].max(), label=f'item: {item}')
        ax.plot((pivot.loc[item]- pivot.loc[item].min())/(pivot.loc[item].max()- pivot.loc[item].min()), label=key_name2, marker='d')
        
        #df_hm_plot = pd.concat([df_hm_plot, pivot_monthly[item]], axis=0)
        df_hm_plot[f'{item}'] = pivot.loc[item]
    
    
    fig_sns = plt.figure(figsize=(8,6))
    
    corr_mat= df_hm_plot.corr()
    ax.legend()
    
    sns.heatmap(corr_mat, annot=True, fmt=".2f", xticklabels=lbl_hmap, yticklabels= lbl_hmap, vmin=-1, vmax=1, center=0)
    
    tmp_dict = {}
    for m, item in enumerate(dict_hight_corr[k]): # [ v1, v2]
        tmp_dict[item] = round(float(corr_mat.iloc[0, m+1]), 2)
    
    mod_dict_hight_cor[k] = tmp_dict
        
ax.set_xlim([monthly['ym'].min(), monthly['ym'].max()])
ax.grid()
plt.show()


#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt

# 최대 weight 값 기준 정규화 (0~1 범위로 맞추면 시각화 깔끔)
x = train_fe['weight'] / train_fe['weight'].max()
y = train_fe['value'] / train_fe['value'].max()

# 기준선 설정
x_split = 0.04     # x=0.3 경계선
a = 1.2            # y = a*x 기준선 (기울기)
train_fe['cluster_manual'] = 0  # 기본값

# 조건별 군집 분류
train_fe.loc[(x <= x_split), 'cluster_manual'] = 0 # 분홍색 군집
train_fe.loc[(x > x_split) & (y < a * x), 'cluster_manual'] = 1 # 노란색 군집
train_fe.loc[(x > x_split) & (y >= a * x), 'cluster_manual'] = 2 # 초록색 군집



############################################################################
# 시각화
plt.figure(figsize=(8,8))
colors = ['#FF9999','#FFCC66','#99CC99']
for i, color in enumerate(colors):
    plt.scatter(x[train_fe['cluster_manual']==i],
                y[train_fe['cluster_manual']==i],
                label=f'Cluster {i}', s=40, color=color, alpha=0.7)


# 기준선들 시각화
plt.axvline(x=x_split, color='gray', linestyle='--', label=f'x={x_split}')
plt.plot(np.linspace(0,1,100),
         a * np.linspace(0,1,100),
         color='black', linestyle='--', label=f'y={a}x')

plt.xlabel('weight (normalized)')
plt.ylabel('value (normalized)')
plt.title('Manual Clustering by x-split and y=ax line')
plt.legend()
plt.show()


