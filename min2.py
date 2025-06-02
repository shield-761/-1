import pandas as pd
import folium
from sklearn.cluster import KMeans
folium

# CSV 불러오기
df = pd.read_csv("Delivery.csv")

# 결측치 제거
df = df.dropna(subset=["Latitude", "Longitude"])

# KMeans 군집화
k = 5  # 군집 수 조정 가능
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Latitude', 'Longitude']])

# 지도 중심 설정
center_lat = df["Latitude"].mean()
center_lon = df["Longitude"].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# 색상 팔레트
colors = ['red', 'blue', 'green', 'purple', 'orange']

# 군집별 마커 추가
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        color=colors[row["Cluster"] % len(colors)],
        fill=True,
        fill_color=colors[row["Cluster"] % len(colors)],
        fill_opacity=0.7,
        popup=f"Num: {row['Num']} (Cluster {row['Cluster']})"
    ).add_to(m)

# 결과 저장
m.save("delivery_cluster_map.html")
print("✅ 'delivery_cluster_map.html' 파일이 생성되었습니다.")
