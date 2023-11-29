from numpy import load
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='plot numpy .npz file')
parser.add_argument('input_files', type=str, nargs='+')
args = parser.parse_args()

variables_we_like = ['event_id', 'pid', 'position', 'direction', 'energy', 'digi_hit_pmt', 'digi_hit_charge', 'digi_hit_time']

all_variables = ['event_id', 'root_file', 'pid', 'position', 'direction', 'energy', 'digi_hit_pmt', 'digi_hit_charge', 'digi_hit_time', 'digi_hit_trigger', 'true_hit_pmt', 'true_hit_time', 'true_hit_pos', 'true_hit_start_time', 'true_hit_start_pos', 'true_hit_parent', 'track_id', 'track_pid', 'track_start_time', 'track_energy', 'track_start_position', 'track_stop_position', 'track_parent', 'track_flag', 'trigger_time', 'trigger_type']


for f in args.input_files:
    data = load(f)
    lst = data.files # list of variable in file
    print(lst)
    for variable in variables_we_like:
        print(variable)
        print(data[variable])
        if variable == 'energy':
            plt.hist(data[variable])
            plt.show()
        elif variable == 'position':
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            ax.scatter(data[variable][:,0], data[variable][:,1], data[variable][:,2], marker='o')
        elif variable == 'direction':
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            ax.quiver(data['position'][:,0], data['position'][:,1], data['position'][:,2], data[variable][:,0], data[variable][:,1], data[variable][:,2], length=0.1, normalize=True)
