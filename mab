delivery-map/
├── index.html       ← 실행할 웹페이지
├── delivery.csv     ← 업로드한 CSV 파일 (Num, Latitude, Longitude)
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Delivery Map</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <style>
    #map { height: 100vh; }
  </style>
</head>
<body>
  <div id="map"></div>

  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
  <!-- PapaParse for CSV parsing -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.3.2/papaparse.min.js"></script>

  <script>
    const map = L.map('map').setView([37.5, 126.75], 11); // 기본 중심 좌표

    // OpenStreetMap 타일 추가
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // CSV 파일 불러오기
    Papa.parse("delivery.csv", {
      download: true,
      header: true,
      complete: function(results) {
        results.data.forEach(row => {
          if (row.Latitude && row.Longitude) {
            const lat = parseFloat(row.Latitude);
            const lon = parseFloat(row.Longitude);
            const label = row.Num || 'No Label';
            L.marker([lat, lon])
              .addTo(map)
              .bindPopup(`Num: ${label}`);
          }
        });
      }
    });
  </script>
</body>
</html>
