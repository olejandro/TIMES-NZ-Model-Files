import os
import sys
import times_reader

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
input_dir = os.path.dirname(current_dir)
output_dir = os.path.join(os.path.dirname(current_dir), 'TIMES-NZ', 'raw_table_summary')
use_pkl = False

if __name__ == "__main__":
    times_reader.output_raw_tables_from_xl(
        input_dir, output_dir, use_pkl
    )