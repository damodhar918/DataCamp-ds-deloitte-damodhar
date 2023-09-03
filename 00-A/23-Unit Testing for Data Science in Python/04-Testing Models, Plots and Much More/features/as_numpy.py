import numpy as np


def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.strip().split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None


def row_to_list(row):
    row = row.rstrip("\n")
    separated_entries = [x.strip() for x in row.split("\t")]
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    return None


def get_data_as_numpy_array(clean_data_file_path, num_columns):
    result = np.empty((0, num_columns))
    with open(clean_data_file_path, "r") as f:
        rows = f.readlines()
        for row_num in range(len(rows)):
            try:
                row = np.array([rows[row_num].rstrip(
                    "\n").split("\t")], dtype=float)
            except ValueError:
                raise ValueError("Line {0} of {1} is badly formatted".format(
                    row_num + 1, clean_data_file_path))
            else:
                if row.shape != (1, num_columns):
                    raise ValueError(
                        "Line {0} of {1} does not have {2} columns".format(
                            row_num + 1,
                            clean_data_file_path,
                            num_columns
                        )
                    )
            result = np.append(result, row, axis=0)
    return result
