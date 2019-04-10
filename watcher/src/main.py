import os
import time
import datetime
import pandas as pd
from pathlib import Path

# search_dir = "../csv/"
# os.chdir(search_dir)
# files = filter(os.path.isfile, os.listdir(search_dir))
# files = [os.path.join(search_dir, f) for f in files]
# files.sort(key=lambda x: os.path.getmtime(x))

# with codecs.open(files[-1], 'r', 'latin_1') as t1, codecs.open(files[-2], 'r', 'latin_1') as t2:
#     fileone = t1.readlines()
#     filetwo = t2.readlines()

# diff = ''
# for line in filetwo:
#     if line not in fileone:
#         diff += line

# file = codecs.open("update.csv", "w", "latin_1")
# file.write(diff)
# file.close()

# import pandas as pd
# from pathlib import Path


def excel_diff(path_OLD, path_NEW):

    df_OLD = pd.read_excel(path_OLD, header = 1).fillna(0)
    df_NEW = pd.read_excel(path_NEW, header = 1).fillna(0)
    dfDiff = pd.DataFrame()

    count_row = df_NEW.shape[0]
    cols_OLD = df_OLD.columns
    cols_NEW = df_NEW.columns
    sharedCols = list(set(cols_OLD).intersection(cols_NEW))

    for row in df_NEW.index:
        print('>>> Progresso: {}/{}'.format(row + 1, count_row))
        if (row in df_OLD.index) and (row in df_NEW.index):
            diffRow = df_NEW.loc[row, :]
            shoudlAddRow = False
            for col in sharedCols:
                value_OLD = df_OLD.loc[row, col]
                value_NEW = df_NEW.loc[row, col]
                if value_OLD != value_NEW:
                    shoudlAddRow = True
                    diffRow.loc[col] = ('{}→{}').format(value_OLD, value_NEW)

            if (shoudlAddRow):
                dfDiff = dfDiff.append(diffRow)
        if row not in df_OLD.index:
            dfDiff = dfDiff.append(df_NEW.loc[row, :])

    dfDiff = dfDiff.sort_index().fillna('')

    # Save output and format
    temp_name = datetime.datetime.fromtimestamp(
        time.time()).strftime('%Y-%m-%d_%H:%M:%S')
    writer = pd.ExcelWriter(temp_name + '.xlsx', engine='xlsxwriter')

    dfDiff.to_excel(writer, sheet_name='DIFF', index=False)
    # df_NEW.to_excel(writer, sheet_name=path_NEW.stem, index=False)
    # df_OLD.to_excel(writer, sheet_name=path_OLD.stem, index=False)

    # get xlsxwriter objects
    workbook = writer.book
    worksheet = writer.sheets['DIFF']
    worksheet.hide_gridlines(2)
    worksheet.set_default_row(15)

    highlight_fmt = workbook.add_format({'font_color': '#FF0000'})

    # set format over range
    # highlight changed cells
    worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                               'criteria': 'containing',
                                               'value': '→',
                                               'format': highlight_fmt})

    # save
    writer.save()
    print('\nDone.\n')


def main():
    os.chdir('csv')
    path_OLD = os.path.abspath(
        'Extrato de Contrato - Janeiro_2016 a Julho_2018.xls')
    path_NEW = os.path.abspath(
        'Extrato de Contrato - Janeiro_2016 a Fevereiro_2019.xls')

    os.chdir('../output')
    excel_diff(path_OLD, path_NEW)


if __name__ == '__main__':
    main()
