import pandas as pd
import numpy as np
import sweetviz as sv
#import warnings
import os
#warnings.simplefilter(action='ignore', category=FutureWarning)

def generate_sweetviz_report():

  df = pd.read_csv('delicatessa.csv', delimiter=';')
  df['data_source_size_value'] = pd.to_numeric(df['data_source_size_value'], errors='coerce')
  df['sap_program_feature'] = pd.to_numeric(df['sap_program_feature'], errors='coerce')
  df['supplier_color'] = pd.to_numeric(df['supplier_color'], errors='coerce')

  sweet_report = sv.analyze(df, pairwise_analysis="off")
  sweet_report.show_html('sweetviz_report.html')

if __name__ == '__main__':
  generate_sweetviz_report()