import math
from datetime import datetime

class DataProcessor:
    @staticmethod
    def process_mixing_data(mixing):
        differences = []
        for i in range(len(mixing) - 1):
            diff = [mixing[i][0]]  
            for j in range(1, len(mixing[i])):
                value_diff = abs(mixing[i+1][j] - mixing[i][j])
                diff.append(value_diff)
            differences.append(diff)

        return differences


class DelayCalculator:
    @staticmethod
    def calculate_delay(L, D, Q):
        f_value = 0.648 * 10**6
        ans = (f_value * L**2 * D) / (16 * math.pi * Q**2) 
        return ans


class MixingProcessor:
    @staticmethod
    def process_mixing(mixing):
        data = []
        for item in mixing:
            item[0] = datetime.strptime(item[0], '%Y-%m-%d')
            item[1] = datetime.strptime(item[1], '%H:%M:%S')
            item[2:] = [float(i) for i in item[2:]]

        return mixing

class МixingService:
    @staticmethod
    def mixing_implementation(mixing,L,d,D):
        mixing = MixingProcessor.process_mixing(mixing)
        differences = DataProcessor.process_mixing_data(mixing)
        
        data = []
        i = 0
        for item in differences:
            Q = item[2] * 3600
            D[i] = (D[i] - 2 * d[i]) / 10 / 100
            data.append(int(DelayCalculator.calculate_delay(L[i], D[i], Q)))
            i+=1
        
        return data




