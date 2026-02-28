import csv
import generators as gen
import processing as proc
import plotting as plt_mod

def main():
    # Configuration
    DATA_SIZE = 1000
    SIGMA_1 = 30
    SIGMA_2 = 120

    # 1. Generate noise components (w1, w2) and coefficients (a)
    w1, w2, a = gen.generate_noise_signals(DATA_SIZE)

    # 2. Save raw data to CSV for record keeping
    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2', 'a'])
        writer.writerows(zip(w1, w2, a))

    # 3. Simulate and process first instance (Sigma = 30)
    t1 = gen.simulate_ou_process(a, SIGMA_1, w1)
    diff1 = proc.calculate_step_differences(t1)
    
    # 4. Simulate and process second instance (Sigma = 120)
    t2 = gen.simulate_ou_process(a, SIGMA_2, w2)
    diff2 = proc.calculate_step_differences(t2)

    # 5. Visualization
    # Results for Sigma 1
    plt_mod.plot_process_and_diff(t1, diff1, f'OU Process (Sigma={SIGMA_1})')
    plt_mod.plot_autocorrelation(t1)

    # Results for Sigma 2
    plt_mod.plot_process_and_diff(t2, diff2, f'OU Process (Sigma={SIGMA_2})')
    plt_mod.plot_autocorrelation(t2)

if __name__ == '__main__':
    main()