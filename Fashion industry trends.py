import pandas as pd
import matplotlib.pyplot as plt

# Data
pembelian_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Bahan Baku A': [120, 150, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360],
    'Bahan Baku B': [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],
    'Bahan Baku C': [60, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270]
}

produksi_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Pakaian': [80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280],
    'Sepatu': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Tas': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
}

penjualan_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Pakaian': [70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180],
    'Sepatu': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Tas': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
}

persediaan_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Pakaian': [20, 30, 40, 60, 90, 130, 180, 240, 310, 390, 480, 580],
    'Sepatu': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],
    'Tas': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
}

# Create DataFrames
pembelian_df = pd.DataFrame(pembelian_data)
produksi_df = pd.DataFrame(produksi_data)
penjualan_df = pd.DataFrame(penjualan_data)
persediaan_df = pd.DataFrame(persediaan_data)

# Scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(pembelian_df['Bulan'], pembelian_df['Bahan Baku A'], label='Bahan Baku A', color='r')
plt.scatter(pembelian_df['Bulan'], pembelian_df['Bahan Baku B'], label='Bahan Baku B', color='g')
plt.scatter(pembelian_df['Bulan'], pembelian_df['Bahan Baku C'], label='Bahan Baku C', color='b')
plt.xlabel('Bulan')
plt.ylabel('Pembelian (ton)')
plt.title('Scatterplot Pembelian Bahan Baku')
plt.legend()
plt.show()

# Pie chart
plt.figure(figsize=(10, 6))
total_pembelian = pembelian_df[['Bahan Baku A', 'Bahan Baku B', 'Bahan Baku C']].sum()
plt.pie(total_pembelian, labels=total_pembelian.index, autopct='%1.1f%%', colors=['r', 'g', 'b'])
plt.title('Pie Chart Total Pembelian Bahan Baku')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist([produksi_df['Pakaian'], produksi_df['Sepatu'], produksi_df['Tas']], label=['Pakaian', 'Sepatu', 'Tas'], color=['r', 'g', 'b'])
plt.xlabel('Produksi (ton)')
plt.ylabel('Frekuensi')
plt.title('Histogram Produksi')
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
bar_width = 0.25
bar1 = range(len(penjualan_df['Bulan']))
bar2 = [x + bar_width for x in bar1]
bar3 = [x + bar_width for x in bar2]

plt.bar(bar1, penjualan_df['Pakaian'], color='r', width=bar_width, label='Pakaian')
plt.bar(bar2, penjualan_df['Sepatu'], color='g', width=bar_width, label='Sepatu')
plt.bar(bar3, penjualan_df['Tas'], color='b', width=bar_width, label='Tas')

plt.xlabel('Bulan')
plt.ylabel('Penjualan (ton)')
plt.title('Bar Chart Penjualan')
plt.xticks([r + bar_width for r in range(len(penjualan_df['Bulan']))], penjualan_df['Bulan'])
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Data per tahun
data = {
    'Year': list(range(1, 13)),
    'Pembelian A': [120, 150, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360],
    'Pembelian B': [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],
    'Pembelian C': [60, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270],
    'Produksi Pakaian': [80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280],
    'Produksi Sepatu': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Produksi Tas': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Penjualan Pakaian': [70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180],
    'Penjualan Sepatu': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Penjualan Tas': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Persediaan Pakaian': [20, 30, 40, 60, 90, 130, 180, 240, 310, 390, 480, 580],
    'Persediaan Sepatu': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],
    'Persediaan Tas': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the model
model = LinearRegression()

# Function to perform linear regression and make predictions
def predict_future(df, column_name, years_ahead):
    X = np.array(df['Year']).reshape(-1, 1)
    y = np.array(df[column_name])
    
    # Fit the model
    model.fit(X, y)
    
    # Predict future values
    future_years = np.array(range(1, len(df['Year']) + years_ahead + 1)).reshape(-1, 1)
    predictions = model.predict(future_years)
    
    return future_years.flatten(), predictions

# Plotting the results
plt.figure(figsize=(14, 10))

# Define subplots for each category
categories = [
    'Pembelian A', 'Pembelian B', 'Pembelian C',
    'Produksi Pakaian', 'Produksi Sepatu', 'Produksi Tas',
    'Penjualan Pakaian', 'Penjualan Sepatu', 'Penjualan Tas',
    'Persediaan Pakaian', 'Persediaan Sepatu', 'Persediaan Tas'
]

for i, category in enumerate(categories, 1):
    plt.subplot(4, 3, i)
    future_years, predictions = predict_future(df, category, 10)
    plt.plot(df['Year'], df[category], 'o', label='Data Aktual')
    plt.plot(future_years, predictions, '-', label='Prediksi')
    plt.title(category)
    plt.xlabel('Tahun')
    plt.ylabel('Ton')
    plt.legend()

plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Data per tahun
data = {
    'Year': list(range(1, 13)),
    'Pembelian A': [120, 150, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360],
    'Pembelian B': [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],
    'Pembelian C': [60, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270],
    'Produksi Pakaian': [80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280],
    'Produksi Sepatu': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Produksi Tas': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the model
model = LinearRegression()

# Function to perform linear regression and get correlation
def analyze_relationship(pembelian, produksi):
    X = np.array(pembelian).reshape(-1, 1)
    y = np.array(produksi)
    
    # Fit the model
    model.fit(X, y)
    
    # Calculate correlation
    correlation = np.corrcoef(pembelian, produksi)[0, 1]
    
    # Get regression parameters
    slope = model.coef_[0]
    intercept = model.intercept_
    
    # Predict values
    predictions = model.predict(X)
    
    return correlation, slope, intercept, predictions

# Plotting the results
plt.figure(figsize=(18, 6))

# Define pairs for analysis
pairs = [
    ('Pembelian A', 'Produksi Pakaian'),
    ('Pembelian B', 'Produksi Sepatu'),
    ('Pembelian C', 'Produksi Tas')
]

for i, (pembelian, produksi) in enumerate(pairs, 1):
    plt.subplot(1, 3, i)
    correlation, slope, intercept, predictions = analyze_relationship(df[pembelian], df[produksi])
    plt.scatter(df[pembelian], df[produksi], label='Data Aktual')
    plt.plot(df[pembelian], predictions, color='red', label=f'Regresi Linier\nr={correlation:.2f}\nY={slope:.2f}X+{intercept:.2f}')
    plt.title(f'{pembelian} vs {produksi}')
    plt.xlabel(pembelian)
    plt.ylabel(produksi)
    plt.legend()

plt.tight_layout()
plt.show()

# Print the results
for pembelian, produksi in pairs:
    correlation, slope, intercept, _ = analyze_relationship(df[pembelian], df[produksi])
    print(f'{pembelian} vs {produksi}:')
    print(f'  Korelasi: {correlation:.2f}')
    print(f'  Persamaan Regresi: Y = {slope:.2f}X + {intercept:.2f}\n')


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Data per tahun
data = {
    'Year': list(range(1, 13)),
    'Pembelian A': [120, 150, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360],
    'Pembelian B': [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300],
    'Pembelian C': [60, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270],
    'Produksi Pakaian': [80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280],
    'Produksi Sepatu': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],
    'Produksi Tas': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Penjualan Pakaian': [70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180],
    'Penjualan Sepatu': [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Penjualan Tas': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Persediaan Pakaian': [20, 30, 40, 60, 90, 130, 180, 240, 310, 390, 480, 580],
    'Persediaan Sepatu': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125],
    'Persediaan Tas': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the model
model = LinearRegression()

# Function to perform linear regression and get slope
def analyze_trend(data, y):
    X = np.array(data).reshape(-1, 1)
    y = np.array(y)
    
    # Fit the model
    model.fit(X, y)
    
    # Get regression parameters
    slope = model.coef_[0]
    intercept = model.intercept_
    
    # Predict values
    predictions = model.predict(X)
    
    return slope, intercept, predictions

# Plotting the results
plt.figure(figsize=(18, 12))

# Define pairs for analysis
categories = [
    'Pembelian A', 'Pembelian B', 'Pembelian C',
    'Produksi Pakaian', 'Produksi Sepatu', 'Produksi Tas',
    'Penjualan Pakaian', 'Penjualan Sepatu', 'Penjualan Tas',
    'Persediaan Pakaian', 'Persediaan Sepatu', 'Persediaan Tas'
]

for i, category in enumerate(categories, 1):
    plt.subplot(4, 3, i)
    slope, intercept, predictions = analyze_trend(df['Year'], df[category])
    plt.scatter(df['Year'], df[category], label='Data Aktual')
    plt.plot(df['Year'], predictions, color='red', label=f'Tren\nY={slope:.2f}X+{intercept:.2f}')
    plt.title(category)
    plt.xlabel('Tahun')
    plt.ylabel('Ton')
    plt.legend()

plt.tight_layout()
plt.show()

# Print the results
for category in categories:
    slope, intercept, _ = analyze_trend(df['Year'], df[category])
    print(f'{category}:')
    print(f'  Persamaan Tren: Y = {slope:.2f}X + {intercept:.2f}')
    if slope > 0:
        print(f'  Tren: Peningkatan ({slope:.2f} per tahun)')
    elif slope < 0:
        print(f'  Tren: Penurunan ({slope:.2f} per tahun)')
    else:
        print(f'  Tren: Tidak ada perubahan\n')
