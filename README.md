# ConvertMatToCsv
Convert any .mat file in a csv file


if you get: TypeError: Mismatch between array dtype ('object') and format specifier ('%.18e,%.18e')

Just modify the last line as follow:

    np.savetxt(("filesforyou/"+i+".csv"),data[i],fmt='%s',delimiter=',')
