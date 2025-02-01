from GPUtil import getGPUs
import GPUtil

gpus = getGPUs()
for gpu in gpus:
	print(f"ID: {gpu.id}, Name: {gpu.name}, Load: {gpu.load*100}%")
	print(f"Memory Usage: {gpu.memoryUsed}MB / {gpu.memoryTotal}MB")
	print(f"Temperature: {gpu.temperature} °C")

