import csv
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Simulation Parameters
    SIZE = 1000
    WINDOW_SIZE = 15
    S1, S2 = 2, 120

    # 1. Generate Noise Data
    w1, w2 = gen.generate_wiener_noise(SIZE)

    # 2. Export Noise to CSV
    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2'])
        writer.writerows(zip(w1, w2))

    # 3. Simulate Wiener Processes
    t1 = gen.simulate_wiener_process(SIZE, S1, w1)
    t2 = gen.simulate_wiener_process(SIZE, S2, w2)

    # 4. Process and Smooth the Series
    sm_t1 = proc.apply_moving_average(t1, WINDOW_SIZE)
    sm_t2 = proc.apply_moving_average(t2, WINDOW_SIZE)

    # 5. Process and Smooth the Increments (Differences)
    diff1 = proc.calculate_increments(t1)
    diff2 = proc.calculate_increments(t2)
    sm_diff1 = proc.apply_moving_average(diff1, WINDOW_SIZE)
    sm_diff2 = proc.apply_moving_average(diff2, WINDOW_SIZE)

    # 6. Generate Visual Comparisons
    # Wiener Process Results
    plt_mod.plot_smoothed_comparison(t1, sm_t1, 't1', f'Wiener Process (Sigma={S1}) with Moving Average')
    plt_mod.plot_smoothed_comparison(t2, sm_t2, 't2', f'Wiener Process (Sigma={S2}) with Moving Average')

    # Increments (Difference) Results
    plt_mod.plot_smoothed_comparison(diff1, sm_diff1, 'diff1', 'Wiener Increments (Set 1) - Smoothed')
    plt_mod.plot_smoothed_comparison(diff2, sm_diff2, 'diff2', 'Wiener Increments (Set 2) - Smoothed')

    print("Wiener Process simulation with Smoothing completed successfully.")

if __name__ == '__main__':
    main()