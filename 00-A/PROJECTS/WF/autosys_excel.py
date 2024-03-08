import argparse
import glob
import pandas as pd


class AutoSysFileToExcel:
    def __init__(self, path: str):
        if not path:
            paths = glob.glob(pathname=r"*.txt")
            paths += glob.glob(pathname=r"*.jil")
        elif '.' in path:
            paths = glob.glob(pathname=path)
        else:
            paths = glob.glob(pathname=path+r"/*.txt")
            paths += glob.glob(pathname=path+r"/*.jil")
        self.path = set(paths)

    def process_files(self) -> None:
        for file in set(self.path):
            print(file, 'started to process')
            self._process_file(file)
            print(file, 'has written excel file')

    def _process_file(self, file: str) -> None:
        with open(file, "r") as f:
            data = f.readlines()

        li_dict = []
        for li_data in ("".join(data).replace(" job_type:", "\n job_type:").split("/* -")):
            li_temp = []
            try:
                for _ in li_data.split("\n"):
                    if (_.strip() != "") and ("----------------" not in _):
                        li_temp.append((_.strip('').split(": ", 1)))
                li_dict.append(dict([[r.strip() for r in q] for q in li_temp]))
            except Exception as e:
                print("Error:", e)
                print("Error data:", li_temp)

        file = file.strip(".txt").strip(".jil").replace('/', '\\') + ".xlsx"
        pd.DataFrame.from_dict(li_dict).dropna(how="all")\
            .reset_index(drop=True)\
            .to_excel(file, index=False,)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert .txt/.jil files to .xlsx files.')
    parser.add_argument('path', nargs='?', default='', type=str,
                        help='The location of the .txt/.jil files. If not specified, the current directory is used.')
    args = parser.parse_args()

    converter = AutoSysFileToExcel(path=args.path.strip('.\\'))
    converter.process_files()
    print('Done!')
