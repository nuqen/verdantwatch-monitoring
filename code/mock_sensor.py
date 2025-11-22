import time
import random

print("VerdantWatch Mock Sensor Running – Pulsing real-time environmental data...")
print("Press Ctrl+C to stop\n")

while True:
    pfas_level = round(random.uniform(0.1, 50.0), 2)  # Simulated PFAS in ppt
    aqi = random.randint(20, 150)                   # Air Quality Index
    soil_moisture = round(random.uniform(10, 80), 1) # %
    biodiversity_index = random.randint(50, 100)     # Mock species diversity

    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')} | PFAS: {pfas_level} ppt | AQI: {aqi} | Soil Moisture: {soil_moisture}% | Biodiversity: {biodiversity_index}/100")
    time.sleep(5)  # Pulses every 5 seconds
