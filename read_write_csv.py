import csv

def passwd_to_csv(input_path, output_path):
	with open(input_path, 'r') as i_file:
		r = csv.reader(i_file, delimiter = ':')

		with open(output_path, 'w') as o_file:
			o = csv.writer(o_file, delimiter = '\t')
			for row in r:
				if not row[0].startswith('#'):
					print(row[0])
					o.writerow([row[0], row[2]])


passwd_to_csv('./password_input.csv', './passwd_output.csv')
