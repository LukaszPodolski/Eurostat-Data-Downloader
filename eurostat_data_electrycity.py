import eurostat


def download_and_save_data(dataset_code, csv_filename):
    # Pobierz dane z Eurostat
    data = eurostat.get_data_df(dataset_code)

    # Nazwa pliku CSV do zapisu
    csv_filename = f'{csv_filename}.csv'

    # Zapisz dane do pliku CSV
    data.to_csv(csv_filename, index=False)

    print(f"Dane zapisano do pliku {csv_filename}")


# Net electricity generation by type of fuel - monthly data
download_and_save_data('nrg_cb_pem', 'Net_ee_generation')

# Supply, transformation and consumption of electricity - monthly data
download_and_save_data('NRG_CB_EM', 'Consumption_ee')

# Electricity available to internal market
download_and_save_data('NRG_CB_EIM', 'Available_ee_internal_market')
