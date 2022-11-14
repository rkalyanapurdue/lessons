import geopandas as gpd
import fiona
MAX_RECORDS = 1000
def read_file(fileName):
    #just read the file using fiona and check if there are more than 1000 rows.
    fileMeta = fiona.open(fileName)
    if len(fileMeta)>MAX_RECORDS:
        raise MemoryError('Memory Error. Cannot read more than 1000 rows. You might want to use the read_file_stream option instead')
    else:
        return gpd.read_file(fileName)
    
def read_file_stream(fileName,chunkSize=1000):
    fileMeta = fiona.open(fileName)
    if chunkSize>MAX_RECORDS:
        raise Error(f'chunk size cannot be greater than {MAX_RECORDS} records')
    for i in range(0,len(fileMeta),chunkSize):
        yield gpd.read_file(fileName,rows = slice(i,i+chunkSize))
            
    