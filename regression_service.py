import pandas as pd
from datetime import datetime, timedelta
import math
from scipy.stats import pearsonr, spearmanr, kendalltau
import matplotlib.pyplot as plt


class DataConverter:
    @staticmethod
    def convert_to_datetime(date_string, time_string):
        return datetime.strptime(f"{date_string} {time_string}", "%d.%m.%Y %H:%M")

    @staticmethod
    def convert_to_float(value):
        return float(value)


class CorrelationCalculator:
    @staticmethod
    
    def calculate_correlation(seq1, seq2, correlation_type):
        correlation_functions = {
            'pearson': pearsonr,
            'spearman': spearmanr,
            'kendall': kendalltau
        }
        correlation_function = correlation_functions.get(correlation_type.lower())
        if correlation_function is None:
            raise ValueError("Invalid correlation type. Choose from 'pearson', 'spearman', or 'kendall'.")

        return correlation_function(seq1, seq2)[0]


class ArrayMatcher:
    @staticmethod
    def match_arrays(array, array_values, divisor):
        result = []
        for val in array:
            divided_value = val / divisor
            matched_array = [item for item in array_values if item[2] == str(divided_value)]
            result.append(matched_array)
        return result


class RegressionProcessor:
    @staticmethod

    def filter_arrays(arr, max_val):
        second_elements = {}
        for sublist in arr:
            if sublist[1] not in second_elements:
                second_elements[sublist[1]] = 1
            else:
                second_elements[sublist[1]] += 1

        max_count = max(second_elements.values())
        most_common_elements = [key for key, value in second_elements.items() if value == max_count]
        return [sub_arr for sub_arr in arr if sub_arr[1] == most_common_elements[0]]


class TimeDeltaCalculator:
    @staticmethod

    def calculate_min_time_diff(time_diff_dict):
        min_diff_days = min(value['time_diff'].days for value in time_diff_dict.values())
        return [value['time_diff'] for value in time_diff_dict.values() if value['time_diff'].days == min_diff_days]


class ValueFilter:
    @staticmethod
    def filter_values(arr, threshold):

        return [item for item in arr if item[1] >= threshold]



class RegressionImplementation:
    @staticmethod
    def implement_regression(regression_la, regression_kip):
        filtered_regression_la = RegressionProcessor.filter_arrays(regression_la,len(regression_la))
        regression_kip_values = [int(float(item[2]) * 10**7) for item in regression_kip]
        filtered_regression_la_values = [int(float(item[2]) * 10**2) for item in filtered_regression_la]

        sub_seq_length = len(regression_la)
        correlation_type = 'spearman'

        best_correlation = None
        best_indices = None

        for i in range(len(filtered_regression_la_values) - sub_seq_length + 1):

            sub_seq2 = filtered_regression_la_values[i:i + sub_seq_length]
            for j in range(len(regression_kip_values) - sub_seq_length + 1):

                sub_seq1 = regression_kip_values[j:j + sub_seq_length]
                correlation = CorrelationCalculator.calculate_correlation(sub_seq1, sub_seq2, correlation_type)
                if best_correlation is None or correlation > best_correlation:
                    best_correlation = correlation
                    best_indices = (i, i + sub_seq_length), (j, j + sub_seq_length)

        if best_indices:
            best_sub_seq1 = regression_kip_values[best_indices[1][0]:best_indices[1][1]]
            best_sub_seq2 = filtered_regression_la_values[best_indices[0][0]:best_indices[0][1]]

            result_regression_kip = ArrayMatcher.match_arrays(best_sub_seq1, regression_kip, 10**7)
            result_regression_la = ArrayMatcher.match_arrays(best_sub_seq2, filtered_regression_la, 10**2)

            result_regression_kip_converted = [[(DataConverter.convert_to_datetime(item[0], item[1]), DataConverter.convert_to_float(item[2])) for item in sublist] for sublist in result_regression_kip]
            result_regression_la_converted = [[(DataConverter.convert_to_datetime(item[0], item[1]), DataConverter.convert_to_float(item[2])) for item in sublist] for sublist in result_regression_la]

            kip_dict = {item[0]: item[1] for sublist in result_regression_kip_converted for item in sublist}
            la_dict = {item[0]: item[1] for sublist in result_regression_la_converted for item in sublist}

            time_diff_dict = {}
            for kip_time, kip_value in kip_dict.items():
                for la_time, la_value in la_dict.items():
                    time_diff = abs(kip_time - la_time)
                    time_diff_dict[(kip_time, la_time)] = {'kip_value': kip_value, 'la_value': la_value, 'time_diff': time_diff}

            min_time_diffs = TimeDeltaCalculator.calculate_min_time_diff(time_diff_dict)
            return [delta.total_seconds() for delta in min_time_diffs]
        else:
            return []


