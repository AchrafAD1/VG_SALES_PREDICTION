import csv

# Open the original CSV file for reading
with open('vgsales_MA.csv', 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Read the header line
    header = next(csv_reader)

    # Define the indices of the columns to keep
    indices_to_keep = [0, 1, 2, 3, 4, 5, 7]

    # Open a new CSV file for writing
    with open('modified_file.csv', 'w', newline='') as new_csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(new_csv_file)

        # Write the modified header
        new_header = [header[i] for i in indices_to_keep]
        csv_writer.writerow(new_header)

        # Iterate through the rows in the original file and write the modified rows to the new file
        for row in csv_reader:
            new_row = [row[i] for i in indices_to_keep]
            csv_writer.writerow(new_row)