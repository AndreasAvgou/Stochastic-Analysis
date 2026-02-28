import csv
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Simulation Parameters
    SIZE = 1000
    S1 = 2
    S2 = 120

    # 1. Generate noise signals
    w1, w2 = gen.generate_wiener_noise(SIZE)

    # 2. Export noise data to CSV
    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2'])
        writer.writerows(zip(w1, w2))

    # 3. Compute Wiener Processes
    t1 = gen.compute_wiener_process(SIZE, S1, w1)
    t2 = gen.compute_wiener_process(SIZE, S2, w2)

    # 4. Calculate Differences (Increments)
    diff1 = proc.calculate_differences(t1)
    diff2 = proc.calculate_differences(t2)

    # 5. Visualizations
    # Process Plots
    plt_mod.plot_wiener_series(t1, 'Original t1', f'Wiener Process (Sigma={S1})', color='blue')
    plt_mod.plot_wiener_series(t2, 'Original t2', f'Wiener Process (Sigma={S2})', color='green')

    # Difference Plots
    plt_mod.plot_difference_series(diff1, 'Original diff1', 'Increments of t1', color='red')
    plt_mod.plot_difference_series(diff2, 'Original diff2', 'Increments of t2', color='purple')

    print("Wiener Process simulation and plotting completed.")

if __name__ == '__main__':
    main()