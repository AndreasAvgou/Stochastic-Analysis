import csv
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Simulation Parameters
    SIZE = 1000
    WINDOW_SIZE = 15
    S1, S2 = 2, 120

    # 1. Data Generation
    w1, w2, a_coeffs = gen.generate_ou_noise(SIZE)

    # 2. Export to CSV
    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2', 'a'])
        writer.writerows(zip(w1, w2, a_coeffs))

    # 3. Simulate OU Processes
    t1 = gen.simulate_ou_process(SIZE, S1, w1, a_coeffs)
    t2 = gen.simulate_ou_process(SIZE, S2, w2, a_coeffs)

    # 4. Apply Smoothing to Processes
    sm_t1 = proc.apply_moving_average(t1, WINDOW_SIZE)
    sm_t2 = proc.apply_moving_average(t2, WINDOW_SIZE)

    # 5. Calculate and Smooth Increments (Differences)
    diff1 = proc.calculate_increments(t1)
    diff2 = proc.calculate_increments(t2)
    sm_diff1 = proc.apply_moving_average(diff1, WINDOW_SIZE)
    sm_diff2 = proc.apply_moving_average(diff2, WINDOW_SIZE)

    # 6. Visualizations
    # Process plots (Set 1 & 2)
    plt_mod.plot_smoothed_comparison(t1, sm_t1, 't1', f'OU Process (Sigma={S1}) with Moving Average')
    plt_mod.plot_smoothed_comparison(t2, sm_t2, 't2', f'OU Process (Sigma={S2}) with Moving Average')

    # Difference plots (Set 1 & 2)
    plt_mod.plot_smoothed_comparison(diff1, sm_diff1, 'diff1', 'Increments of t1 - Smoothed')
    plt_mod.plot_smoothed_comparison(diff2, sm_diff2, 'diff2', 'Increments of t2 - Smoothed')

if __name__ == '__main__':
    main()