def reverse_lines(input_path, output_path):
	with open(input_path, 'r') as i_file, open(output_path, 'w') as o_file:
		for line in i_file:	
			o_file.write(line[::-1])


reverse_lines('./old_line.txt', './new_lines.txt')
