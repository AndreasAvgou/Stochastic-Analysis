import csv
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Parameters
    SIZE = 1000
    SIGMA_1 = 30
    SIGMA_2 = 120
    INITIAL_VAL = 1

    # 1. Generate the shared noise signal (w)
    w_signal = gen.generate_random_noise(SIZE)

    # 2. Save noise data to CSV
    with open('WData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w'])
        for val in w_signal:
            writer.writerow([val])

    # 3. Compute Random Walk values (t1, t2)
    t1 = gen.compute_random_walk(INITIAL_VAL, SIGMA_1, w_signal)
    t2 = gen.compute_random_walk(INITIAL_VAL, SIGMA_2, w_signal)

    # 4. Calculate differences
    diff1 = proc.calculate_differences(t1)
    diff2 = proc.calculate_differences(t2)

    # 5. Visualizations
    # Plotting t1 and t2 together for comparison
    plt_mod.plot_time_series(
        [t1, t2], 
        ['t1 values', 't2 values'], 
        labels=[f'Sigma={SIGMA_1}', f'Sigma={SIGMA_2}']
    )

    # Plotting differences
    plt_mod.plot_differences(
        diff1, 
        diff2, 
        'Differences between successive values'
    )

if __name__ == '__main__':
    main()