import os


folder_main = os.getcwd()
folder_plot = 'plot'
folder_storage = 'storage'

folder_use = os.path.join(folder_main, folder_storage)
folder_use_plot = os.path.join(folder_main, folder_plot)

host = 'localhost'
queue = 'test_queue_3'

string_range = 30
index_begin, index_end = 1, 2000001

value_x = [
    100000, 200000, 300000, 400000, 500000, 600000, 700000, 
    800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 
    1500000, 1600000, 1700000, 1800000, 1900000, 2000000,
]