import csv
import numpy as np
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Configuration parameters
    np.random.seed(0)
    size = 10000
    window_size = 30
    a_coefficient = 0.8
    s1, s2 = 30, 120

    # 1. Generate primary noise and random factors
    w1 = gen.generate_random_values(size)
    w2 = gen.generate_random_values(size)
    g1 = gen.generate_random_values(size)
    g2 = gen.generate_random_values(size)

    # 2. Export raw noise data to CSV
    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2'])
        writer.writerows(zip(w1, w2))

    # 3. Process first dataset (Set 1)
    t1 = gen.generate_t_values(a_coefficient, s1, w1)
    a1 = gen.generate_a_values(t1, g1)
    sm_a1 = proc.generate_smoothed_values(a1, window_size)
    diff1 = proc.calculate_differences(a1)
    sm_diff1 = proc.generate_smoothed_values(diff1, window_size)

    # 4. Process second dataset (Set 2)
    t2 = gen.generate_t_values(a_coefficient, s2, w2)
    a2 = gen.generate_a_values(t2, g2)
    sm_a2 = proc.generate_smoothed_values(a2, window_size)
    diff2 = proc.calculate_differences(a2)
    sm_diff2 = proc.generate_smoothed_values(diff2, window_size)

    # 5. Generate and Save Visualization Outputs
    # Set 1 plots
    plt_mod.plot_and_save(a1, 'a1.pdf', 'Time', 'Value')
    plt_mod.plot_and_save(sm_a1, 'smoothed_a1.pdf', 'Time', 'Value', color='red', smoothed=True)
    plt_mod.plot_and_save(diff1, 'diff1.pdf', 'Time', 'Value')
    plt_mod.plot_autocorr(a1, 'autoc1.pdf')
    plt_mod.plot_autocorr(sm_a1, 'auto1.pdf')

    # Set 2 plots
    plt_mod.plot_and_save(a2, 'a2.pdf', 'Time', 'Value')
    plt_mod.plot_and_save(sm_a2, 'smoothed_a2.pdf', 'Time', 'Value', color='red', smoothed=True)
    plt_mod.plot_autocorr(a2, 'autoc2.pdf')
    plt_mod.plot_autocorr(sm_a2, 'auto2.pdf')

    print("Task completed: Data generated, processed, and plots saved.")

if __name__ == '__main__':
    main()