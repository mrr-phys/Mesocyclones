#!/usr/bin python3
"""
converts grb2 files to CSV for readability
"""
import os
import subprocess
# os.path.dirname(os.path.realpath(__file__)
def nam_grb2():
    """ return directory of NAM grb2 data """
    return './data/NAM_grb2'
def nam_csv():
    """ return directory of NAM csv data """
    return './data/NAM_csv'


def main():
    # wgrib2 namanl_218_20170701_0000_000.grb2 -match "TMP:50 mb:" -csv data.csv
    # for cur_dir, sub_dirs, file_list in os.walk(nam_grb2()):
    #     for single_file in file_list:
    #         TMP_filter = 
    #         cmd = """wgrib2 {} -match "{}" -csv data.csv""".format(single_file, )
    #         subprocess.run()
    # print(list(range(50,1025,25)))
    cmd_string = 'wgrib2 namanl_218_20170701_0000_000.grb2 -s | grep TMP > nam.txt'.split(' ')
    cmd_process = subprocess.Popen(cmd_string, cwd=nam_grb2(), stdout=subprocess.PIPE)
    print(cmd_process.stdout)
    print(cmd_process.stderr)

if __name__ == '__main__':
    main()

        # file_name = file_name[:file_name.index('.')]
        # csv_filename = '{}/{}.csv'.format(nam_dir('csv'), file_name)
        # print(file_name)
        # print(csv_filename)

# def grb2tocsv():
#     """ main scripts to convert grb2 to csv """
#     for curr_dir, sub_dirs, file_list in os.walk(nam_dir('grb2')):
#         # wgrib2 file.grb2 -csv file.csv
#         # print('Current Directory: %s' % curr_dir)
#         print()
#         for file_name in file_list:
#             file_name = file_name[:file_name.index('.')]
#             grb2_filename = '{}/{}.grb2'.format(curr_dir, file_name)
#             csv_filename = '{}/{}.csv'.format(nam_dir('csv'), file_name)
#             wgrib2_cmd = 'wgrib2' + ' ' + grb2_filename + ' ' + '-csv' + ' ' + csv_filename
#             wgrib2_process = subprocess.run(wgrib2_cmd.split(' '), stdout=subprocess.PIPE)
#             print(file_name)
#             print(grb2_filename)
#             print(csv_filename)
#             print(wgrib2_process)
