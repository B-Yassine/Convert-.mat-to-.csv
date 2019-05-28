# ConvertMatToCsv
Convert any .mat file in a csv file


if you get: Mismatch between array dtype ('object') and format specifier

Just modify the last line as follow:

    np.savetxt(("filesforyou/"+i+".csv"),data[i],fmt='%s',delimiter=',')
