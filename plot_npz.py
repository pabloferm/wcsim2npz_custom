from numpy import load
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='plot numpy .npz file')
parser.add_argument('input_files', type=str, nargs='+')
args = parser.parse_args()

variables_we_like = ['event_id', 'pid', 'position', 'direction', 'energy', 'digi_hit_pmt', 'digi_hit_charge', 'digi_hit_time']

all_variables = ['event_id', 'root_file', 'pid', 'position', 'direction', 'energy', 'digi_hit_pmt', 'digi_hit_charge', 'digi_hit_time', 'digi_hit_trigger', 'true_hit_pmt', 'true_hit_time', 'true_hit_pos', 'true_hit_start_time', 'true_hit_start_pos', 'true_hit_parent', 'track_id', 'track_pid', 'track_start_time', 'track_energy', 'track_start_position', 'track_stop_position', 'track_parent', 'track_flag', 'trigger_time', 'trigger_type']


for f in args.input_files:
    data = load(f, allow_pickle = True)
    lst = data.files    #list of variable in file
    print(lst)
    for variable in variables_we_like:
        print(variable)
        print(data[variable].shape)

        if variable == 'energy':
            plt.hist(data[variable])
            plt.xlabel('Energy (MeV)')
            plt.ylabel('counts')
            plt.show()


        if variable == 'direction': 
            x_variable = data[variable][:,0]  #extract the first component of 'variable' to plot it
            y_variable = data[variable][:,1]
            z_variable = data[variable][:,2]
            bins = 25

            fig, ((ax0, ax1),(ax2, ax3)) = plt.subplots(nrows = 2, ncols = 2)


            ax0.hist(x_variable, bins = bins, density  = True,  color = 'coral')
            ax0.set_title('x_component')

            ax1.hist(y_variable, bins = bins, density  = True,  color = 'darkviolet')
            ax1.set_title('y_component')

            ax2.hist(x_variable, bins = bins, density  = True,  color = 'skyblue')
            ax2.set_title('z_component')

            ax3.hist(data[variable], bins = bins, density = True)


            fig.suptitle('Direction')

            fig.tight_layout()
            plt.show()



        if variable == 'digi_hit_pmt':
            #plt.hist(data[variable].flatten)  
            plt.hist(data[variable])
            plt.title('digi_hit_pmt')
            plt.show()


        if variable == 'digi_hit_charge':
            plt.hist(data[variable])
            plt.title('digi_hit_charge')
            plt.show()

    
        if variable == 'digi_hit_time':
            plt.hist(data[variable])
            plt.title('digi_hit_time')
            plt.show()

            




