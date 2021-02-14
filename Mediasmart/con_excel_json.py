import pandas

excel_data_df = pandas.read_excel('Peer39_Taxonomy_Mediasmart_012721.xlsx', sheet_name='Single Tab Taxonomy')

# json_str = excel_data_df.to_json()
json_str = excel_data_df.to_json(orient='records', indent=2)

print('Excel Sheet to JSON:\n', json_str)

with open("output.txt", 'w') as file:
    file.write(json_str)
