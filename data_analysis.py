import os
import json
import statistics
import matplotlib.pyplot as plt
from data_develop import (
    check_folder,
    get_file_name_json,
    merge_callback_result
)
from config import (
    value_x,
    queue,
    folder_use, 
    folder_use_plot
)


def value_selected_file_plot(delta:str, name:str) -> str:
    return os.path.join(folder_use_plot, f"{queue}_{delta}_{name}.png")

def develop_stats_delta(delta:str):
    with open(os.path.join(folder_use, get_file_name_json(False)), 'r') as file:
        value_revision = [f.get(delta, -1) for f in json.load(file)]
    return {
        "Maximum Value": max(value_revision),
        "Minimum Value": min(value_revision),
        "Mean Value of it": statistics.mean(value_revision),
        "Median Value of it": statistics.median(value_revision),
        "Mode Value of it": statistics.mode(value_revision),
        "Standard Deviation Value of it": statistics.stdev(value_revision),
        "Variance": statistics.variance(value_revision),
        "Length": len(value_revision),
    }

def develop_stats_plot(delta:str):
    with open(os.path.join(folder_use, get_file_name_json(False)), 'r') as file:
        value_delta = [f.get(delta, -1) for f in json.load(file)]
    value_plot_mean = plt.scatter(
        value_x, 
        [
            statistics.mean(value_delta[:i])
            for i in value_x
        ]
    )
    
    if delta == 'delta_full':
        k = "Between send and inserting values"
    elif delta == 'delta_send':
        k = "Between sent and receive of the consumer"
    elif delta == 'delta_proccessed':
        k = "Between receive of the consumer and insert"
    
    plt.title(f'{k}: mean')
    plt.ylabel("Seconds")
    plt.xlabel("Number of elements")
    plt.close()
    
    value_plot_var = plt.scatter(
        value_x, 
        [
            statistics.variance(value_delta[:i])
            for i in value_x
        ]
    )

    plt.title(f'{k}: variance')
    plt.ylabel("Seconds")
    plt.xlabel("Number of elements")
    plt.close()

    value_plot_dev = plt.scatter(
        value_x, 
        [
            statistics.stdev(value_delta[:i])
            for i in value_x
        ]
    )

    plt.title(f'{k}: deviation')
    plt.ylabel("Seconds")
    plt.xlabel("Number of elements")
    plt.close()

    value_plot_mean.figure.savefig(value_selected_file_plot(delta, 'mean'))
    value_plot_var.figure.savefig(value_selected_file_plot(delta, 'variance'))
    value_plot_dev.figure.savefig(value_selected_file_plot(delta, 'deviation'))

def develop_stats():
    value_use = {
        "Between send and inserting values": develop_stats_delta('delta_full'),
        "Between sent and receive of the consumer": develop_stats_delta('delta_send'),
        "Between receive of the consumer and insert": develop_stats_delta('delta_proccessed'),
    }
    with open(os.path.join(folder_use, get_file_name_json('1')), 'w') as file_write:
        json.dump(
            value_use, 
            file_write,
            indent=4
        )
    return value_use

    
def develop_plot():
    if not os.path.exists(os.path.join(folder_use, get_file_name_json(False))):
        check_folder(folder_use)
        merge_callback_result()
    check_folder(folder_use_plot)
    for f in ['delta_full', 'delta_send', 'delta_proccessed']:
        develop_stats_plot(f)
    develop_stats()


if __name__ == '__main__':
    develop_plot()