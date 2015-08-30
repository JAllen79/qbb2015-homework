import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):       #populates dictionary with provided argument, dm3 len?
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays                            #at this point arrays is populated with dm3 len? should provide template

    def set_bits_from_file( self, fname ):              #should take second provided argument and make "true" its range
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]      
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1     #modifies arrays with "1"s 
        
    def intersect( self, other ):                       #takes third argument "other" and returns new dictionary "rval" 
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )
            
    def a_and_not_b(self):
        roi = []
        for chrom in self.arrays:
            row = self.arrays[chrom]
            for i, x in enumerate(row):
                if i % 2000000 == 0:
                    print len(roi), i, chrom
                if x == 1 and row[i-1] == 0:
                    start = i
                if x == 0 and row[i-1] == 1:
                    stop = i
                    roi.append((chrom, start, stop))
        return roi
            
       